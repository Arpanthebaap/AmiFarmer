"""
AmiFarmer - Autonomous Multimodal Agricultural Intelligence Engine & Farm OS.
"""

from amifarmer.core.full_farm_audit import FullFarmAuditor
from amifarmer.core.soil_analyzer import SoilAnalyzer
from amifarmer.core.hydrology_engine import HydrologyEngine
from amifarmer.core.crop_recommender import CropRecommender
from amifarmer.core.market_intelligence import MarketIntelligence
from amifarmer.core.agronomy_calendar import AgronomyCalendar
from amifarmer.core.plant_protection import PlantProtection
from amifarmer.core.mechanization_advisor import MechanizationAdvisor
from amifarmer.core.subsidy_matcher import SubsidyMatcher
from amifarmer.core.agribusiness_incubator import AgribusinessIncubator

__version__ = "1.0.0"
__author__ = "Arpan Ghosh & The AmiFarmer Research Initiative"

__all__ = [
    "FullFarmAuditor",
    "SoilAnalyzer",
    "HydrologyEngine",
    "CropRecommender",
    "MarketIntelligence",
    "AgronomyCalendar",
    "PlantProtection",
    "MechanizationAdvisor",
    "SubsidyMatcher",
    "AgribusinessIncubator",
]
