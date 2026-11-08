"""
AmiFarmer Groundwater Hydrology, Irrigation Water Budgeting, and Solar Pump Sizing Engine.
Integrates Central Ground Water Board (CGWB) classifications and Penman-Monteith evapotranspiration models.
"""

import math
from typing import Dict, Any, List, Optional
from amifarmer.models.farm_profile import WaterProfile, GroundwaterCategory, IrrigationSource
from amifarmer.data import load_groundwater_zones


class HydrologyEngine:
    """
    Simulates water table dynamics, calculates crop irrigation demand,
    and sizes solar-powered pumping infrastructure.
    """

    def __init__(self):
        self.gw_guidelines = load_groundwater_zones().get("depth_guidelines", {})
        self.aquifers = load_groundwater_zones().get("aquifer_typologies", {})

    def evaluate_groundwater_status(self, depth_mbgl: float) -> Dict[str, Any]:
        """
        Classifies water table depth in meters below ground level (mbgl).
        """
        if depth_mbgl <= 5.0:
            key = "0-5 mbgl"
            category = GroundwaterCategory.SAFE
            sustainability_score = 92.0
            recharge_ease = "High"
        elif depth_mbgl <= 15.0:
            key = "5-15 mbgl"
            category = GroundwaterCategory.SAFE
            sustainability_score = 85.0
            recharge_ease = "High"
        elif depth_mbgl <= 30.0:
            key = "15-30 mbgl"
            category = GroundwaterCategory.SEMI_CRITICAL
            sustainability_score = 65.0
            recharge_ease = "Moderate"
        elif depth_mbgl <= 60.0:
            key = "30-60 mbgl"
            category = GroundwaterCategory.CRITICAL
            sustainability_score = 40.0
            recharge_ease = "Low"
        else:
            key = ">60 mbgl"
            category = GroundwaterCategory.OVER_EXPLOITED
            sustainability_score = 20.0
            recharge_ease = "Severely Depleted"

        info = self.gw_guidelines.get(key, {})
        return {
            "depth_mbgl": depth_mbgl,
            "category": category.value if hasattr(category, "value") else str(category),
            "sustainability_score": sustainability_score,
            "recharge_ease": recharge_ease,
            "status_title": info.get("status", "Standard Table"),
            "drainage_risk": info.get("drainage_risk", ""),
            "solar_pump_baseline": info.get("solar_pump_spec", "")
        }

    def calculate_crop_water_balance(
        self,
        crop_water_demand_mm: float,
        rainfall_during_cycle_mm: float,
        irrigation_efficiency: float = 0.85
    ) -> Dict[str, Any]:
        """
        Calculates Net Irrigation Requirement (NIR) and Gross Irrigation Requirement (GIR).
        Uses USDA Soil Conservation Service effective rainfall formula:
        P_eff = Rainfall * 0.7 if Rainfall < 250 else (Rainfall * 0.5 + 50)
        """
        if rainfall_during_cycle_mm < 250.0:
            effective_rainfall_mm = max(0.0, rainfall_during_cycle_mm * 0.7)
        else:
            effective_rainfall_mm = max(0.0, rainfall_during_cycle_mm * 0.5 + 50.0)

        net_deficit_mm = max(0.0, crop_water_demand_mm - effective_rainfall_mm)
        gross_irrigation_needed_mm = net_deficit_mm / max(0.4, irrigation_efficiency)

        # 1 mm of water over 1 acre = 4,046.86 Litres ≈ 4.05 cubic meters
        water_volume_liters_per_acre = gross_irrigation_needed_mm * 4047.0

        return {
            "crop_water_demand_mm": crop_water_demand_mm,
            "effective_rainfall_mm": round(effective_rainfall_mm, 1),
            "net_irrigation_deficit_mm": round(net_deficit_mm, 1),
            "gross_irrigation_required_mm": round(gross_irrigation_needed_mm, 1),
            "water_volume_cubic_meters_per_acre": round(water_volume_liters_per_acre / 1000.0, 1),
            "water_volume_liters_per_acre": round(water_volume_liters_per_acre, 0)
        }

    def size_solar_irrigation_pump(
        self,
        water_depth_mbgl: float,
        farm_area_acres: float,
        peak_daily_water_liters: float = 35000.0,
        sunlight_peak_hours: float = 6.0
    ) -> Dict[str, Any]:
        """
        Sizes solar photovoltaic pump array under PM-KUSUM guidelines.
        Total Dynamic Head (TDH) = Static Head + Friction Loss (15%) + Delivery Pressure Head (10m for drip).
        P_hydraulic (W) = (rho * g * Q * H) / eta_pump
        """
        static_lift_m = water_depth_mbgl + 3.0  # drawdown factor
        friction_head_m = static_lift_m * 0.15
        operating_head_drip_m = 10.0  # 1.0 bar pressure for drip emitter operation
        total_dynamic_head_m = static_lift_m + friction_head_m + operating_head_drip_m

        # Daily discharge needed
        daily_target_m3 = (peak_daily_water_liters * min(5.0, farm_area_acres)) / 1000.0
        flow_rate_m3_per_hour = daily_target_m3 / sunlight_peak_hours
        flow_rate_liters_per_sec = (flow_rate_m3_per_hour * 1000.0) / 3600.0

        # Hydraulic power = rho * g * Q * H
        # rho = 1000 kg/m3, g = 9.81 m/s2
        # P = 9.81 * flow_m3_per_s * Head_m (in kW)
        flow_m3_per_s = flow_rate_m3_per_hour / 3600.0
        p_hydraulic_kw = (9.81 * 1000.0 * flow_m3_per_s * total_dynamic_head_m) / 1000.0

        # Typical combined wire-to-water efficiency of submersible motor-pump = 55%
        p_electrical_kw = p_hydraulic_kw / 0.55
        motor_hp = p_electrical_kw * 1.341

        # Standard commercial solar pump ratings: 2HP, 3HP, 5HP, 7.5HP, 10HP
        if motor_hp <= 2.2:
            recommended_hp = 3.0
            pv_array_watts = 3000
        elif motor_hp <= 3.8:
            recommended_hp = 5.0
            pv_array_watts = 4800
        elif motor_hp <= 6.2:
            recommended_hp = 7.5
            pv_array_watts = 7200
        else:
            recommended_hp = 10.0
            pv_array_watts = 9600

        # PM-KUSUM benchmark capital cost (approx ₹52,000 per HP)
        estimated_capex = recommended_hp * 52000.0
        subsidy_amount = estimated_capex * 0.60  # 60% standard subsidy
        farmer_out_of_pocket = estimated_capex - subsidy_amount

        annual_diesel_saved_liters = round(farm_area_acres * 140.0 * (total_dynamic_head_m / 25.0))
        annual_fuel_savings_inr = round(annual_diesel_saved_liters * 92.0)  # ₹92/L diesel

        return {
            "total_dynamic_head_m": round(total_dynamic_head_m, 1),
            "flow_rate_m3_per_hour": round(flow_rate_m3_per_hour, 1),
            "calculated_motor_hp": round(motor_hp, 2),
            "recommended_pump_hp": recommended_hp,
            "recommended_solar_pv_array_wp": pv_array_watts,
            "estimated_system_cost_inr": estimated_capex,
            "pm_kusum_subsidy_inr": subsidy_amount,
            "net_farmer_cost_inr": farmer_out_of_pocket,
            "annual_diesel_saved_liters": annual_diesel_saved_liters,
            "annual_cost_savings_inr": annual_fuel_savings_inr,
            "payback_period_years": round(farmer_out_of_pocket / max(1.0, annual_fuel_savings_inr), 1)
        }

    def recommend_irrigation_method(self, soil_texture: str, water_depth_mbgl: float) -> Dict[str, Any]:
        """
        Recommends best irrigation technique based on soil porosity and water scarcity.
        """
        if water_depth_mbgl > 25.0 or "Sandy" in soil_texture:
            method = "Micro Drip Irrigation (Pressure Compensating)"
            water_savings_pct = 55.0
            yield_increase_pct = 40.0
            reasons = [
                "Deep water table requires strict conservation to avoid aquifer depletion.",
                "High soil percolation rates in sandy textures cause fertilizer leaching with furrow methods.",
                "Eligible for 55% PMKSY Per Drop More Crop government subsidy."
            ]
        elif "Black" in soil_texture or "Clay" in soil_texture:
            method = "Broad Bed Furrow (BBF) + Inline Drip"
            water_savings_pct = 45.0
            yield_increase_pct = 30.0
            reasons = [
                "Heavy black cotton soils swell and cause water stagnation during heavy rains.",
                "BBF provides dual advantage of drainage during monsoon and precision watering in dry spells."
            ]
        else:
            method = "Drip or Micro-Sprinkler System"
            water_savings_pct = 40.0
            yield_increase_pct = 25.0
            reasons = [
                "Maximizes water application efficiency above 85% compared to flood irrigation (35-40%).",
                "Permits automated soluble fertilizer fertigation directly to root feeding zone."
            ]

        return {
            "recommended_method": method,
            "water_savings_pct": water_savings_pct,
            "yield_increase_pct": yield_increase_pct,
            "justification": reasons
        }
