"""
AmiFarmer Farm Mechanization, Machinery Sizing, and Custom Hiring Center (CHC) Advisor.
Calculates capital expenditure vs. rental economics and models SMAM subsidies.
"""

from typing import Dict, Any, List, Optional
from amifarmer.models.farm_profile import FarmProfile
from amifarmer.data import load_equipment_catalog


class MechanizationAdvisor:
    """
    Advises farmers on optimal machinery investments, prevents over-capitalization debt,
    and identifies local Custom Hiring Center (CHC) rental opportunities.
    """

    def __init__(self):
        self.catalog = load_equipment_catalog()

    def get_mechanization_plan(self, farm: FarmProfile, primary_crop: str) -> Dict[str, Any]:
        """
        Builds a customized machinery and mechanization strategy.
        """
        area = farm.total_area_acres
        category = farm.farmer_category

        recommended_tools = []
        total_capex = 0.0
        total_subsidies = 0.0
        total_farmer_share = 0.0
        rental_recommendations = []

        for item in self.catalog:
            ideal = item.get("ideal_farm_size", "")
            cost = item.get("estimated_purchase_cost_inr", 0.0)
            subsidy_pct = item.get("subsidy_available_pct", 50.0)
            subsidy_amount = cost * (subsidy_pct / 100.0)
            farmer_cost = cost - subsidy_amount

            # Strategic decision rule:
            # Smallholders (<5 acres) should NOT buy heavy 50HP tractors, harvesters, or laser levelers
            if area < 5.0 and ("Heavy Utility" in item["name"] or "Laser" in item["name"] or "Drone" in item["name"]):
                verdict = "Rent from CHC / Uber-for-Tractors"
                reason = f"Farm size ({area} acres) is insufficient to amortize high capital cost. Renting saves approx ₹4,500/acre annually."
                rental_recommendations.append({
                    "equipment": item["name"],
                    "chc_rate": item.get("chc_rental_rate_per_acre_or_hour", ""),
                    "reason": reason
                })
            elif "Compact" in item["name"] and (area >= 2.0 or "Vegetable" in primary_crop or "Horticulture" in primary_crop):
                verdict = "Buy with SMAM Subsidy"
                recommended_tools.append({
                    "name": item["name"],
                    "verdict": verdict,
                    "cost_inr": cost,
                    "subsidy_inr": subsidy_amount,
                    "farmer_share_inr": farmer_cost,
                    "rationale": item["rationale"]
                })
                total_capex += cost
                total_subsidies += subsidy_amount
                total_farmer_share += farmer_cost
            elif "Rotavator" in item["name"] or "Drip" in item["name"] or "Solar" in item["name"]:
                verdict = "Buy with Subsidy"
                recommended_tools.append({
                    "name": item["name"],
                    "verdict": verdict,
                    "cost_inr": cost,
                    "subsidy_inr": subsidy_amount,
                    "farmer_share_inr": farmer_cost,
                    "rationale": item["rationale"]
                })
                total_capex += cost
                total_subsidies += subsidy_amount
                total_farmer_share += farmer_cost

        return {
            "farm_area_acres": area,
            "farmer_holding_class": category,
            "mechanization_index": "High-Efficiency Precision Model",
            "recommended_purchases": recommended_tools,
            "rental_from_chc_strategy": rental_recommendations,
            "financial_summary": {
                "total_equipment_cost_inr": round(total_capex, 0),
                "total_government_subsidy_inr": round(total_subsidies, 0),
                "net_farmer_capital_required_inr": round(total_farmer_share, 0),
                "subsidy_absorption_pct": round((total_subsidies / max(1.0, total_capex)) * 100.0, 1)
            },
            "chc_app_advisory": "Download the FARMS (Farm Machinery Solutions) App by the Ministry of Agriculture to book nearby Custom Hiring Center tractors and harvesters at government-capped rates."
        }
