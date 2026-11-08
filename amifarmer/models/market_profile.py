"""
Market intelligence, price equilibrium, Mandi arbitrage, and post-harvest economics.
"""

from enum import Enum
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field


class MarketingChannel(str, Enum):
    APMC_MANDI = "APMC Mandi (Regulated Wholesale)"
    FPO_COLLECTIVE = "FPO / Farmer Producer Company Aggregation"
    DIRECT_TO_CONSUMER = "Direct to Consumer (D2C / Farmer Markets / Urban Subscriptions)"
    FOOD_PROCESSOR_CONTRACT = "Contract Farming / Food Processing Company (ITC, PepsiCo, Agro-units)"
    E_NAM_PLATFORM = "e-NAM (Electronic National Agriculture Market)"
    EXPORT_MARKET = "Export Market (APEDA certified)"


class MarketPricePoint(BaseModel):
    crop_name: str
    mandi_name: str
    state: str
    modal_price_per_quintal_inr: float
    min_price_per_quintal_inr: float
    max_price_per_quintal_inr: float
    msp_inr: Optional[float] = None
    price_trend_30d: str = "Stable"  # "Bullish (+15%)", "Bearish (-10%)", "Stable"
    peak_demand_months: List[str] = Field(default_factory=list)


class ValueAdditionOpportunity(BaseModel):
    raw_produce: str
    processed_product: str
    value_multiplier: float  # e.g., 2.5x raw value
    required_equipment: List[str]
    fssai_compliance_needed: bool
    shelf_life_increase_months: int
    profit_margin_increase_pct: float


class MarketArbitrageStrategy(BaseModel):
    crop_id: str
    crop_name: str
    apmc_mandi_revenue_per_acre: float
    fpo_revenue_per_acre: float
    d2c_revenue_per_acre: float
    processing_revenue_per_acre: float
    recommended_channel: MarketingChannel
    storage_recommendation: str
    buyer_types_to_target: List[str]
    transport_and_packing_cost_per_quintal_inr: float
