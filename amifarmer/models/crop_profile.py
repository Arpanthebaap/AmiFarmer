"""
Crop, Vegetable, and High-Value Agronomic Data Models for AmiFarmer.
"""

from enum import Enum
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field


class CropCategory(str, Enum):
    CEREAL = "Cereal & Grain"
    MILLET = "Superfood Millet (Nutri-Cereal)"
    PULSE = "Pulse / Legume"
    OILSEED = "Oilseed"
    VEGETABLE = "Vegetable"
    FRUIT = "Fruit / Horticulture"
    SPICE_CONDIMENT = "Spice & Condiment"
    CASH_CROP = "Commercial / Cash Crop"
    MEDICINAL_AROMATIC = "Medicinal & Aromatic Plant (MAP)"
    PROTECTED_CULTIVATION = "Protected Cultivation (Polyhouse/Hydroponics)"
    AGROFORESTRY = "Agroforestry / Timber"
    MUSHROOM = "Fungi / Mushroom Cultivation"


class FarmingSeason(str, Enum):
    KHARIF = "Kharif (Monsoon: June - Oct)"
    RABI = "Rabi (Winter: Nov - April)"
    ZAID = "Zaid (Summer: March - June)"
    PERENNIAL = "Perennial / Year-Round"


class CropRequirement(BaseModel):
    min_ph: float = 6.0
    max_ph: float = 7.8
    optimal_ph: float = 6.8
    min_temp_c: float = 15.0
    max_temp_c: float = 38.0
    optimal_temp_c: float = 26.0
    water_requirement_mm: float = 500.0  # mm per crop cycle
    drought_tolerance: str = "Moderate"  # High, Moderate, Low
    waterlogging_tolerance: str = "Low"  # High, Moderate, Sensitive
    nitrogen_demand_kg_ha: float = 100.0
    phosphorus_demand_kg_ha: float = 50.0
    potassium_demand_kg_ha: float = 40.0
    soil_textures_compatible: List[str] = Field(default_factory=list)
    sunlight_requirement_hours: float = 6.0


class CropProfile(BaseModel):
    crop_id: str
    common_name: str
    hindi_name: str
    scientific_name: str
    category: CropCategory
    seasons: List[FarmingSeason]
    growth_duration_days: int
    requirements: CropRequirement
    average_yield_quintals_per_acre: float
    high_tech_yield_quintals_per_acre: float
    msp_price_per_quintal_inr: Optional[float] = None
    market_modal_price_per_quintal_inr: float
    direct_to_consumer_price_per_quintal_inr: float
    estimated_cost_of_cultivation_per_acre_inr: float
    special_suitability_tags: List[str] = Field(default_factory=list)  # e.g., ["Saline Tolerant", "Drip Preferred", "Export Grade"]
    agronomy_notes: str = ""


class CropRecommendation(BaseModel):
    crop_id: str
    crop_name: str
    hindi_name: str
    category: CropCategory
    season: FarmingSeason
    suitability_score_pct: float = Field(..., description="Overall Agro-Pedo-Climatic Match %")
    soil_affinity_score: float
    climate_affinity_score: float
    water_sustainability_score: float
    expected_yield_quintals_per_acre: float
    gross_revenue_per_acre_inr: float
    total_cost_per_acre_inr: float
    net_profit_per_acre_inr: float
    return_on_investment_pct: float
    growth_cycle_days: int
    risk_level: str  # "Low", "Moderate", "High"
    primary_advantages: List[str]
    limiting_factors_or_precautions: List[str]
    market_channel_recommendation: str
