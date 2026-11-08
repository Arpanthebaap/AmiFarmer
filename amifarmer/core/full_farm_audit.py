"""
AmiFarmer Full 360° Farm Master Audit and Advisory Engine.
Orchestrates soil pedology, hydrology, crop optimization, market intelligence,
plant protection, mechanization, and government subsidies into a unified master dossier.
Zero-Knowledge Beginner Mode natively supported.
"""

from typing import Dict, Any, List, Optional
from amifarmer.models.farm_profile import (
    FarmProfile,
    SoilProfile,
    SoilNutrients,
    SoilTexture,
    WaterProfile,
    ClimateProfile,
    GroundwaterCategory,
    IrrigationSource
)
from amifarmer.core.soil_analyzer import SoilAnalyzer
from amifarmer.core.hydrology_engine import HydrologyEngine
from amifarmer.core.crop_recommender import CropRecommender
from amifarmer.core.market_intelligence import MarketIntelligence
from amifarmer.core.agronomy_calendar import AgronomyCalendar
from amifarmer.core.plant_protection import PlantProtection
from amifarmer.core.mechanization_advisor import MechanizationAdvisor
from amifarmer.core.subsidy_matcher import SubsidyMatcher
from amifarmer.core.agribusiness_incubator import AgribusinessIncubator
from amifarmer.data import get_zone_by_state_and_district, load_soil_benchmarks


class FullFarmAuditor:
    """
    Main orchestrator for AmiFarmer. Runs comprehensive diagnostic on a farm
    and produces an actionable 360-degree road map.
    """

    def __init__(self):
        self.soil_analyzer = SoilAnalyzer()
        self.hydrology_engine = HydrologyEngine()
        self.crop_recommender = CropRecommender()
        self.market_intel = MarketIntelligence()
        self.calendar_engine = AgronomyCalendar()
        self.protection_engine = PlantProtection()
        self.mechanization_advisor = MechanizationAdvisor()
        self.subsidy_matcher = SubsidyMatcher()
        self.agribusiness_incubator = AgribusinessIncubator()

    @classmethod
    def create_beginner_profile(
        cls,
        farmer_name: str,
        state: str,
        district: str,
        farm_area_acres: float = 2.5,
        experience_level: str = "Beginner (Zero Knowledge)"
    ) -> FarmProfile:
        """
        Creates an intelligent baseline farm profile for a total beginner
        using official ICAR & CGWB regional baseline data.
        """
        zone = get_zone_by_state_and_district(state, district)
        predom_soil = zone.get("soil_type_predominant", "Alluvial")

        # Map predominant string to SoilTexture enum
        texture_enum = SoilTexture.ALLUVIAL
        for t in SoilTexture:
            if t.value.lower() in predom_soil.lower() or predom_soil.lower() in t.value.lower():
                texture_enum = t
                break

        # Benchmarks
        gw_depth = zone.get("groundwater_depth_mbgl", 12.0)
        rainfall = zone.get("annual_rainfall_mm", 950.0)

        # Baseline nutrients typical of the zone
        nutrients = SoilNutrients(
            nitrogen_kg_ha=260.0,
            phosphorus_kg_ha=16.0,
            potassium_kg_ha=190.0,
            organic_carbon_pct=0.58,
            ph=7.2,
            electrical_conductivity_ds_m=0.55,
            zinc_ppm=0.75,
            boron_ppm=0.48
        )

        gw_cat = GroundwaterCategory.SAFE
        if gw_depth > 30.0:
            gw_cat = GroundwaterCategory.OVER_EXPLOITED
        elif gw_depth > 20.0:
            gw_cat = GroundwaterCategory.CRITICAL
        elif gw_depth > 14.0:
            gw_cat = GroundwaterCategory.SEMI_CRITICAL

        farm = FarmProfile(
            farm_id=f"AMIFARM-{state[:3].upper()}-{district[:3].upper()}-001",
            farmer_name=farmer_name,
            state=state,
            district=district,
            total_area_acres=farm_area_acres,
            cultivable_area_acres=max(0.5, farm_area_acres * 0.92),
            farmer_category="Small (1-2 ha)" if 2.5 <= farm_area_acres <= 5.0 else ("Marginal (<1 ha)" if farm_area_acres < 2.5 else "Medium"),
            farming_experience_level=experience_level,
            soil=SoilProfile(texture=texture_enum, nutrients=nutrients),
            water=WaterProfile(groundwater_depth_mbgl=gw_depth, groundwater_category=gw_cat),
            climate=ClimateProfile(
                annual_rainfall_mm=rainfall,
                kharif_rainfall_mm=rainfall * 0.75,
                agro_climatic_zone_id=zone.get("zone_id", 4),
                agro_climatic_zone_name=zone.get("name", "Gangetic Plain")
            )
        )
        return farm

    def run_full_audit(
        self,
        farm: FarmProfile,
        season_filter: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Executes complete multi-disciplinary audit and compiles master report.
        """
        # 1. Soil Diagnostic
        soil_analysis = self.soil_analyzer.analyze_soil(farm.soil)

        # 2. Groundwater & Hydrological Analysis
        gw_status = self.hydrology_engine.evaluate_groundwater_status(farm.water.groundwater_depth_mbgl)
        solar_pump_sizing = self.hydrology_engine.size_solar_irrigation_pump(
            water_depth_mbgl=farm.water.groundwater_depth_mbgl,
            farm_area_acres=farm.cultivable_area_acres
        )
        irrigation_method = self.hydrology_engine.recommend_irrigation_method(
            soil_texture=soil_analysis["texture"],
            water_depth_mbgl=farm.water.groundwater_depth_mbgl
        )

        # 3. Crop Recommendations (Top 8 Pareto-optimal crops)
        crop_recommendations = self.crop_recommender.get_recommendations(
            farm=farm,
            season_filter=season_filter,
            top_n=8
        )

        top_crop = crop_recommendations[0] if crop_recommendations else None

        # 4. Market Intelligence for Top Recommended Crop
        market_dossier = None
        if top_crop:
            market_dossier = self.market_intel.analyze_market_options(
                crop_name=top_crop["crop_name"],
                yield_quintals_per_acre=top_crop["expected_yield_quintals_per_acre"],
                modal_mandi_price_inr=top_crop["market_modal_price_per_quintal_inr"],
                d2c_price_inr=top_crop.get("potential_d2c_net_profit_per_acre_inr", top_crop["market_modal_price_per_quintal_inr"] * 1.5),
                msp_inr=top_crop.get("msp_price_per_quintal_inr")
            )

        # 5. Operational 7-Stage Agronomy Roadmap for Top Crop
        agronomy_schedule = None
        if top_crop:
            agronomy_schedule = self.calendar_engine.generate_crop_roadmap(
                crop_name=top_crop["crop_name"],
                category=top_crop["category"],
                growth_days=top_crop["growth_cycle_days"]
            )

        # 6. Integrated Pest Management (IPM) for Top Crop
        plant_protection = None
        if top_crop:
            plant_protection = self.protection_engine.get_plant_protection_guide(top_crop["crop_name"])

        # 7. Machinery & Custom Hiring Plan
        mechanization_plan = self.mechanization_advisor.get_mechanization_plan(
            farm=farm,
            primary_crop=top_crop["crop_name"] if top_crop else "Mixed Crops"
        )

        # 8. Government Subsidies & Eligibility
        subsidy_report = self.subsidy_matcher.evaluate_eligibility(
            farm=farm,
            target_crop_category=top_crop["category"] if top_crop else None
        )

        # 9. Turnkey Agribusiness DPR (Top relevant model)
        agribusiness_models = self.agribusiness_incubator.list_available_models()
        top_dpr = self.agribusiness_incubator.generate_bankable_dpr(
            model_id=agribusiness_models[0]["model_id"],
            farmer_name=farm.farmer_name,
            farm_location=f"{farm.district}, {farm.state}"
        )

        # Executive Summary & Farmer Wealth Strategy
        projected_annual_farm_profit_inr = (
            (top_crop["net_profit_per_acre_inr"] * farm.cultivable_area_acres)
            if top_crop else 0.0
        )
        total_subsidies_unlocked_inr = subsidy_report["total_potential_benefit_inr"]

        executive_summary = (
            f"Farm Audit Dossier for {farm.farmer_name} ({farm.total_area_acres} acres in {farm.district}, {farm.state}). "
            f"Soil Health Score is {soil_analysis['soil_health_score']}/100 ({soil_analysis['soil_health_grade']}). "
            f"Groundwater table is at {farm.water.groundwater_depth_mbgl} mbgl ({gw_status['status_title']}). "
            f"Highest-ranking crop is '{top_crop['crop_name']}' with an estimated net profit of ₹{top_crop['net_profit_per_acre_inr']:,}/acre "
            f"(Total farm net income: ₹{projected_annual_farm_profit_inr:,.0f}). "
            f"Eligible for {subsidy_report['total_schemes_eligible']} Government Subsidies unlocking ₹{total_subsidies_unlocked_inr:,.0f} in capital benefits."
        )

        return {
            "dossier_id": f"AUDIT-{farm.farm_id}",
            "executive_summary": executive_summary,
            "farm_profile": farm.model_dump(),
            "soil_analysis": soil_analysis,
            "hydrology_and_water_security": {
                "groundwater_status": gw_status,
                "solar_pump_sizing": solar_pump_sizing,
                "irrigation_recommendation": irrigation_method
            },
            "top_crop_recommendations": crop_recommendations,
            "market_intelligence_and_arbitrage": market_dossier,
            "agronomy_operational_roadmap": agronomy_schedule,
            "integrated_pest_management": plant_protection,
            "mechanization_and_equipment_plan": mechanization_plan,
            "government_subsidies_and_schemes": subsidy_report,
            "turnkey_agribusiness_dpr": top_dpr
        }
