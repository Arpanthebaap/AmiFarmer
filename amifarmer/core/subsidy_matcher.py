"""
AmiFarmer Government Subsidies, Schemes, and Financial Assistance Matcher.
Identifies eligible Central & State schemes, computes financial benefits,
and generates step-by-step application documentation checklists.
"""

from typing import Dict, Any, List, Optional
from amifarmer.models.farm_profile import FarmProfile
from amifarmer.data import load_subsidies_database


class SubsidyMatcher:
    """
    Intelligent qualification engine for government agriculture and rural development schemes.
    """

    def __init__(self):
        self.subsidies = load_subsidies_database()

    def evaluate_eligibility(self, farm: FarmProfile, target_crop_category: Optional[str] = None) -> Dict[str, Any]:
        """
        Matches the farm profile against all schemes in the registry.
        """
        matched_schemes = []
        total_potential_benefit_inr = 0.0

        for scheme in self.subsidies:
            sid = scheme["scheme_id"]
            is_eligible = True
            reasons = []
            benefit = 0.0

            if sid == "PM-KISAN":
                # Eligible for all individual landholders
                is_eligible = True
                benefit = 6000.0
                reasons.append("Farmer owns cultivable agricultural land.")
                reasons.append("Direct Benefit Transfer (DBT) directly into bank account in 3 installments of ₹2,000.")

            elif sid == "PMKSY-PER-DROP":
                # Micro-irrigation subsidy
                if farm.cultivable_area_acres > 0.1:
                    is_eligible = True
                    # ₹26,000 - ₹35,000 per acre subsidy
                    subsidy_per_acre = 30000.0
                    benefit = min(75000.0, farm.cultivable_area_acres * subsidy_per_acre)
                    reasons.append("Farmer has cultivable land suitable for Drip/Sprinkler micro-irrigation installation.")
                    reasons.append("Small and marginal farmers receive 55% direct capital assistance.")

            elif sid == "PM-KUSUM-SOLAR":
                # Solar pump
                if not farm.water.solar_pump_installed:
                    is_eligible = True
                    benefit = 156000.0  # Approx 60% of 5HP pump
                    reasons.append("Eligible for Component-B standalone off-grid solar agriculture pump.")
                    reasons.append("Replaces expensive diesel engine or eliminates reliance on intermittent grid power.")

            elif sid == "SMAM-MECHANIZATION":
                is_eligible = True
                benefit = 95000.0  # Average tractor / rotavator subsidy benefit
                reasons.append("Eligible for subsidized purchase of rotavators, power tillers, and sowing equipment.")
                reasons.append("50% subsidy for smallholders and women farmers.")

            elif sid == "AIF-INFRA-FUND":
                # Post-harvest infra
                is_eligible = True
                benefit = 150000.0  # 3% interest subvention savings over 7 years
                reasons.append("Eligible for setting up post-harvest storage, primary cleaning, grading, or farm-gate sorting units.")
                reasons.append("3% interest rate subvention on bank term loans with CGTMSE credit guarantee.")

            elif sid == "MIDH-HORTICULTURE":
                if target_crop_category and any(w in target_crop_category for w in ["Vegetable", "Fruit", "Protected", "Mushroom", "Spice"]):
                    is_eligible = True
                    benefit = 450000.0
                    reasons.append("Approved for high-value horticulture crops, polyhouse structures, and shade net houses.")
                else:
                    is_eligible = True
                    benefit = 200000.0
                    reasons.append("Eligible upon diversifying into commercial vegetables, fruits, or mushrooms.")

            elif sid == "PKVY-ORGANIC":
                is_eligible = True
                benefit = min(50000.0, farm.cultivable_area_acres * 20000.0)
                reasons.append("Eligible when joining an organic farming cluster (PGS-India certified).")

            if is_eligible:
                total_potential_benefit_inr += benefit
                matched_schemes.append({
                    "scheme_id": sid,
                    "scheme_name": scheme["scheme_name"],
                    "acronym": scheme["official_acronym"],
                    "ministry": scheme["administering_ministry"],
                    "category": scheme["category"],
                    "estimated_benefit_inr": round(benefit, 0),
                    "qualification_highlights": reasons,
                    "documents_required": scheme["documents_required"],
                    "official_portal": scheme["application_portal_url"],
                    "application_steps": scheme["how_to_apply_steps"]
                })

        return {
            "total_schemes_eligible": len(matched_schemes),
            "total_potential_benefit_inr": round(total_potential_benefit_inr, 0),
            "matched_schemes": matched_schemes,
            "universal_checklist": [
                "Aadhaar Card linked to active mobile number",
                "Updated Land Records (Patta / 7/12 / Khatoni / Jamabandi)",
                "Bank Account Passbook with IFSC (Aadhaar Seeded / NPCI Mapped)",
                "Passport Size Photographs",
                "Soil Health Card (AmiFarmer report accepted as baseline)"
            ]
        }
