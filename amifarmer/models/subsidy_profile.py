"""
Government subsidies, schemes, financial benefits, and eligibility models.
"""

from enum import Enum
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field


class SchemeLevel(str, Enum):
    CENTRAL = "Central Government (GoI)"
    STATE = "State Government"
    JOINT = "Centrally Sponsored / State Shared"


class SchemeTargetCategory(str, Enum):
    DIRECT_INCOME = "Direct Income Support"
    IRRIGATION = "Micro-Irrigation & Water Infrastructure"
    SOLAR_ENERGY = "Solar Pumps & Green Energy"
    MECHANIZATION = "Farm Machinery & Custom Hiring"
    INFRASTRUCTURE = "Post-Harvest Infrastructure & Cold Storage"
    INSURANCE = "Crop Insurance & Risk Mitigation"
    HORTICULTURE = "Horticulture & Protected Agriculture"
    ORGANIC = "Organic & Natural Farming"
    CREDIT_SUBSIDY = "Interest Subvention & KCC"


class GovernmentScheme(BaseModel):
    scheme_id: str
    scheme_name: str
    official_acronym: str
    administering_ministry: str
    level: SchemeLevel
    category: SchemeTargetCategory
    max_subsidy_amount_inr: float
    subsidy_percentage: float  # e.g., 55.0 for 55%
    eligibility_criteria: List[str]
    documents_required: List[str]
    application_portal_url: str
    how_to_apply_steps: List[str]
    special_benefits_for_sc_st_women: Optional[str] = None


class FarmerSubsidyEligibility(BaseModel):
    scheme_id: str
    scheme_name: str
    is_eligible: bool
    estimated_subsidy_benefit_inr: float
    confidence_score_pct: float
    qualification_reasons: List[str]
    action_items_to_apply: List[str]
    direct_portal: str
