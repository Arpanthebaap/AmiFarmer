"""
AmiFarmer Multi-Objective Crop, Vegetable, and Agribusiness Optimization Engine.
Evaluates agro-pedological affinity, groundwater sustainability, market economics,
and price risk to deliver Pareto-optimal recommendations for farmers.
"""

from typing import List, Dict, Any, Optional
from amifarmer.models.farm_profile import FarmProfile, SoilTexture, GroundwaterCategory
from amifarmer.models.crop_profile import CropRecommendation, CropCategory, FarmingSeason
from amifarmer.data import load_crops_database


class CropRecommender:
    """
    Ranks crops using multi-criteria decision analysis (MCDA) combining
    biophysical suitability and micro-economic return on investment.
    """

    def __init__(self):
        self.raw_crops = load_crops_database()

    def evaluate_crop_suitability(self, crop: Dict[str, Any], farm: FarmProfile) -> Dict[str, Any]:
        """
        Evaluates a single crop profile against the farm's soil, climate, and water characteristics.
        Produces sub-scores (0-100) and overall weighted suitability.
        """
        req = crop.get("requirements", {})
        soil = farm.soil
        nutrients = soil.nutrients
        water = farm.water
        climate = farm.climate

        # 1. Soil pH Suitability (Weight: 25%)
        crop_min_ph = req.get("min_ph", 6.0)
        crop_max_ph = req.get("max_ph", 7.8)
        crop_opt_ph = req.get("optimal_ph", 6.8)
        farm_ph = nutrients.ph

        if crop_min_ph <= farm_ph <= crop_max_ph:
            dist = abs(farm_ph - crop_opt_ph)
            ph_score = max(70.0, 100.0 - dist * 25.0)
        else:
            deviation = min(abs(farm_ph - crop_min_ph), abs(farm_ph - crop_max_ph))
            ph_score = max(10.0, 70.0 - deviation * 40.0)

        # 2. Soil Texture Compatibility (Weight: 20%)
        farm_texture = soil.texture.value if hasattr(soil.texture, "value") else str(soil.texture)
        compatible_textures = req.get("soil_textures_compatible", [])

        if any(farm_texture.lower() in t.lower() or t.lower() in farm_texture.lower() for t in compatible_textures):
            texture_score = 100.0
        elif "alluvial" in farm_texture.lower() or "clay loam" in farm_texture.lower():
            texture_score = 80.0  # highly adaptable soils
        else:
            texture_score = 50.0

        soil_affinity = (ph_score * 0.6) + (texture_score * 0.4)

        # 3. Climate / Temperature Suitability (Weight: 25%)
        crop_min_t = req.get("min_temp_c", 15.0)
        crop_max_t = req.get("max_temp_c", 35.0)
        summer_t = climate.summer_max_temp_c
        winter_t = climate.winter_min_temp_c

        # Protected cultivation (polyhouse / indoor mushroom) bypasses external ambient limits
        if crop.get("category") in ["Protected Cultivation (Polyhouse/Hydroponics)", "Fungi / Mushroom Cultivation"]:
            climate_score = 95.0
        else:
            temp_penalty = 0.0
            if summer_t > crop_max_t:
                temp_penalty += (summer_t - crop_max_t) * 4.0
            if winter_t < crop_min_t:
                temp_penalty += (crop_min_t - winter_t) * 4.0
            climate_score = max(20.0, 100.0 - temp_penalty)

        # 4. Water Sustainability Score (Weight: 30%)
        crop_water_mm = req.get("water_requirement_mm", 500.0)
        gw_depth = water.groundwater_depth_mbgl

        if crop_water_mm <= 350.0:
            # Low water crop: highly resilient even in overexploited areas
            water_score = 98.0
        elif crop_water_mm <= 650.0:
            if gw_depth > 30.0:
                water_score = 70.0  # requires micro-irrigation
            else:
                water_score = 90.0
        else:  # High water crop (>650mm, e.g. Paddy, Sugarcane, Ginger)
            if gw_depth > 30.0:
                water_score = 35.0  # Heavily penalized in deep water basins
            elif gw_depth > 15.0:
                water_score = 60.0
            else:
                water_score = 85.0

        # Overall Composite Suitability Score
        composite_score = (soil_affinity * 0.35) + (climate_score * 0.30) + (water_score * 0.35)

        # Economic Returns Calculation (per acre)
        avg_yield = crop.get("average_yield_quintals_per_acre", 10.0)
        cost_per_acre = crop.get("estimated_cost_of_cultivation_per_acre_inr", 15000.0)
        modal_price = crop.get("market_modal_price_per_quintal_inr", 3000.0)
        d2c_price = crop.get("direct_to_consumer_price_per_quintal_inr", 4500.0)
        msp_price = crop.get("msp_price_per_quintal_inr")

        # Yield adjustment based on soil health & experience
        shs_factor = max(0.7, min(1.25, (farm.soil.nutrients.organic_carbon_pct / 0.6)))
        expected_yield = round(avg_yield * shs_factor, 1)

        # Wholesale gross revenue
        gross_revenue_wholesale = expected_yield * modal_price
        gross_revenue_d2c = expected_yield * d2c_price
        net_profit_wholesale = gross_revenue_wholesale - cost_per_acre
        roi_wholesale = (net_profit_wholesale / max(1.0, cost_per_acre)) * 100.0

        # Risk Classification
        if crop.get("category") in ["Cereal & Grain", "Pulse / Legume"] and msp_price:
            risk_level = "Low (Protected by MSP)"
        elif crop.get("category") in ["Vegetable"]:
            risk_level = "Moderate to High (Perishable / Market Price Volatility)"
        elif crop.get("category") in ["Protected Cultivation (Polyhouse/Hydroponics)"]:
            risk_level = "Moderate (High CapEx, High Controlled Margin)"
        elif crop.get("category") in ["Superfood Millet (Nutri-Cereal)"]:
            risk_level = "Low (Climate Resilient, High Shelf Life)"
        elif crop.get("category") in ["Agroforestry / Timber"]:
            risk_level = "Low (Long Gestation, High Capital Appreciation)"
        else:
            risk_level = "Moderate"

        # Advantages and precautions
        advantages = []
        precautions = []

        for tag in crop.get("special_suitability_tags", []):
            advantages.append(tag)

        if water_score < 60.0:
            precautions.append(f"High water demand ({crop_water_mm} mm) in water-stressed groundwater zone. Install drip irrigation to prevent crop failure.")
        if ph_score < 70.0:
            precautions.append(f"Soil pH ({farm_ph:.1f}) is slightly outside optimal ({crop_opt_ph:.1f}). Apply recommended soil amendment before sowing.")
        if crop.get("category") == "Vegetable":
            precautions.append("Stagger planting dates by 15 days to avoid dumping entire harvest during market glut.")

        # Recommended marketing channel
        if d2c_price > modal_price * 1.5 and crop.get("category") in ["Vegetable", "Superfood Millet (Nutri-Cereal)", "Spice & Condiment"]:
            channel = "Direct to Consumer (D2C) / Urban Farmers Market / FPO"
        elif msp_price and modal_price < msp_price * 1.05:
            channel = "Government MSP Procurement Center (e-NAM / FCI / NAFED)"
        elif crop.get("category") == "Protected Cultivation (Polyhouse/Hydroponics)":
            channel = "Quick-Commerce / HORECA Direct Contract (Blinkit, Hotels, Supermarkets)"
        else:
            channel = "APMC Mandi Wholesale with Post-Harvest Cleaning"

        return {
            "crop_id": crop.get("crop_id"),
            "crop_name": crop.get("common_name"),
            "hindi_name": crop.get("hindi_name"),
            "scientific_name": crop.get("scientific_name"),
            "category": crop.get("category"),
            "seasons": crop.get("seasons", []),
            "suitability_score_pct": round(composite_score, 1),
            "soil_affinity_score": round(soil_affinity, 1),
            "climate_affinity_score": round(climate_score, 1),
            "water_sustainability_score": round(water_score, 1),
            "expected_yield_quintals_per_acre": expected_yield,
            "cost_of_cultivation_per_acre_inr": cost_per_acre,
            "market_modal_price_per_quintal_inr": modal_price,
            "msp_price_per_quintal_inr": msp_price,
            "gross_revenue_per_acre_inr": round(gross_revenue_wholesale, 0),
            "net_profit_per_acre_inr": round(net_profit_wholesale, 0),
            "potential_d2c_net_profit_per_acre_inr": round(gross_revenue_d2c - cost_per_acre, 0),
            "return_on_investment_pct": round(roi_wholesale, 1),
            "growth_cycle_days": crop.get("growth_duration_days", 100),
            "risk_level": risk_level,
            "primary_advantages": advantages,
            "limiting_factors_or_precautions": precautions,
            "recommended_channel": channel,
            "agronomy_notes": crop.get("agronomy_notes", "")
        }

    def get_recommendations(
        self,
        farm: FarmProfile,
        season_filter: Optional[str] = None,
        top_n: int = 10
    ) -> List[Dict[str, Any]]:
        """
        Evaluates and ranks all crops in the database.
        Sorts primarily by Multi-Objective Score: (Suitability * 0.5) + (Normalized Profit * 0.5).
        """
        results = []
        for crop in self.raw_crops:
            # Check season filter if provided
            if season_filter:
                crop_seasons = [str(s) for s in crop.get("seasons", [])]
                if not any(season_filter.lower() in s.lower() for s in crop_seasons) and not any("year-round" in s.lower() for s in crop_seasons):
                    continue

            eval_res = self.evaluate_crop_suitability(crop, farm)
            results.append(eval_res)

        # Normalize profit to calculate combined Pareto score
        max_profit = max((r["net_profit_per_acre_inr"] for r in results), default=1.0)
        for r in results:
            norm_profit = max(0.0, min(100.0, (r["net_profit_per_acre_inr"] / max(1.0, max_profit)) * 100.0))
            # Pareto composite: 50% biophysical feasibility + 50% economic profitability
            r["pareto_composite_score"] = round((r["suitability_score_pct"] * 0.45) + (norm_profit * 0.55), 1)

        # Sort descending by Pareto composite score
        results.sort(key=lambda x: x["pareto_composite_score"], reverse=True)
        return results[:top_n]
