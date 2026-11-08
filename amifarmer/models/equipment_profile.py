"""
Agricultural machinery, mechanization, and Custom Hiring Center (CHC) models.
"""

from enum import Enum
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field


class EquipmentType(str, Enum):
    LAND_PREPARATION = "Land Preparation (Tractor, Rotavator, MB Plough, Laser Leveler)"
    SOWING_PLANTING = "Sowing & Planting (Seed Drill, Planter, Transplanter)"
    CROP_MAINTENANCE = "Crop Maintenance (Weeder, Intercultivator, Boom Sprayer)"
    IRRIGATION = "Irrigation System (Drip, Sprinkler, Solar Pump, Diesel Pump)"
    HARVESTING_THRESHING = "Harvesting & Threshing (Combine, Reaper, Multi-crop Thresher)"
    PRECISION_TECH = "Precision Agri-Tech (Agri Drone, Soil Sensors, GPS Guidance)"


class FarmEquipment(BaseModel):
    equipment_id: str
    name: str
    category: EquipmentType
    ideal_farm_size: str  # "Marginal (<2.5 acres)", "Medium (2.5-10 acres)", "Large (>10 acres)"
    estimated_purchase_cost_inr: float
    subsidy_available_pct: float
    subsidy_scheme_name: str
    net_cost_after_subsidy_inr: float
    chc_rental_rate_per_acre_or_hour: str
    recommendation_verdict: str  # "Buy with Subsidy", "Rent from CHC", "Shared Ownership via FPO"
    rationale: str
    maintenance_and_fuel_cost_per_year_inr: float
