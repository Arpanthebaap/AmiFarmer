"""
Agribusiness incubation, DPR (Detailed Project Report), and financial viability models.
"""

from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field


class AgribusinessModel(BaseModel):
    model_id: str
    business_title: str
    target_sector: str  # "Primary Food Processing", "Protected Agriculture", "Bio-Fertilizer", "Mushroom", "Dairy + Circular"
    minimum_land_required_acres: float
    total_capital_expenditure_capex_inr: float
    annual_operating_expenditure_opex_inr: float
    projected_annual_gross_revenue_inr: float
    projected_annual_net_profit_inr: float
    payback_period_years: float
    internal_rate_of_return_irr_pct: float
    applicable_subsidies: List[str]
    subsidy_amount_expected_inr: float
    net_farmer_investment_inr: float
    key_machinery_required: List[str]
    licenses_required: List[str]  # e.g., FSSAI, GST, Udyam, Pollution NOC
    target_buyer_demographics: List[str]
    step_by_step_setup_guide: List[str]
