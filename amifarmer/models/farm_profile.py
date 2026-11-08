"""
Farm, Soil, Hydrology, and Climate data models for AmiFarmer.
Built with strict Pydantic v2 schemas for robust validation and serialization.
"""

from enum import Enum
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field


class SoilTexture(str, Enum):
    ALLUVIAL = "Alluvial"
    BLACK_COTTON = "Black Cotton (Vertisol)"
    RED_SANDY_LOAM = "Red Sandy Loam"
    LATERITE = "Laterite"
    CLAY_LOAM = "Clay Loam"
    SANDY_LOAM = "Sandy Loam"
    DESERT_SANDY = "Desert Sandy"
    PEATY_MARSHY = "Peaty / Marshy"
    SALINE_ALKALINE = "Saline / Alkaline"


class GroundwaterCategory(str, Enum):
    SAFE = "Safe (<70% extraction)"
    SEMI_CRITICAL = "Semi-Critical (70-90% extraction)"
    CRITICAL = "Critical (90-100% extraction)"
    OVER_EXPLOITED = "Over-Exploited (>100% extraction)"
    SALINE_AQUIFER = "Saline Aquifer"


class IrrigationSource(str, Enum):
    TUBEWELL_BOREWELL = "Tubewell / Borewell"
    CANAL = "Canal"
    OPEN_WELL = "Open Dug Well"
    RAINWATER_FARM_POND = "Rainwater Harvesting / Farm Pond"
    RIVER_LIFT = "River Lift Irrigation"
    DRIP_IRRIGATION = "Micro Drip Irrigation"
    SPRINKLER = "Micro Sprinkler"
    NONE_RAINFED = "Purely Rainfed"


class SoilNutrients(BaseModel):
    nitrogen_kg_ha: float = Field(default=240.0, description="Available Nitrogen in kg/ha (Low: <280, Med: 280-560, High: >560)")
    phosphorus_kg_ha: float = Field(default=18.0, description="Available Phosphorus (P2O5) in kg/ha (Low: <10, Med: 10-25, High: >25)")
    potassium_kg_ha: float = Field(default=210.0, description="Available Potassium (K2O) in kg/ha (Low: <110, Med: 110-280, High: >280)")
    organic_carbon_pct: float = Field(default=0.55, description="Soil Organic Carbon % (Low: <0.5%, Med: 0.5-0.75%, High: >0.75%)")
    ph: float = Field(default=7.2, description="Soil pH (Acidic: <6.5, Neutral: 6.5-7.5, Alkaline/Sodic: >7.8)")
    electrical_conductivity_ds_m: float = Field(default=0.45, description="Electrical Conductivity in dS/m (Normal: <1.0, Saline: >2.0)")
    zinc_ppm: Optional[float] = Field(default=0.8, description="DTPA-extractable Zinc in ppm (Critical threshold: 0.6 ppm)")
    boron_ppm: Optional[float] = Field(default=0.5, description="Hot water extractable Boron in ppm (Critical: 0.5 ppm)")
    iron_ppm: Optional[float] = Field(default=6.0, description="Available Iron in ppm (Critical: 4.5 ppm)")
    sulphur_ppm: Optional[float] = Field(default=12.0, description="Available Sulphur in ppm (Critical: 10.0 ppm)")


class SoilProfile(BaseModel):
    texture: SoilTexture = SoilTexture.ALLUVIAL
    nutrients: SoilNutrients = Field(default_factory=SoilNutrients)
    soil_depth_cm: float = Field(default=90.0, description="Effective root zone soil depth in cm")
    drainage_quality: str = Field(default="Moderate", description="Well Drained, Moderate, Poor, Waterlogged")
    slope_pct: float = Field(default=1.5, description="Topographical slope percentage")
    soil_health_card_number: Optional[str] = None


class WaterProfile(BaseModel):
    groundwater_depth_mbgl: float = Field(default=12.5, description="Groundwater depth in meters below ground level (mbgl)")
    groundwater_category: GroundwaterCategory = GroundwaterCategory.SAFE
    primary_source: IrrigationSource = IrrigationSource.TUBEWELL_BOREWELL
    secondary_source: Optional[IrrigationSource] = None
    water_quality_ph: float = Field(default=7.1, description="Irrigation water pH")
    water_salinity_ec_ds_m: float = Field(default=0.7, description="Irrigation water EC in dS/m")
    water_table_trend: str = Field(default="Stable", description="Rising (+0.1m/yr), Stable, Falling (-0.3m/yr to -1.5m/yr)")
    solar_pump_installed: bool = False
    farm_pond_available: bool = False


class ClimateProfile(BaseModel):
    annual_rainfall_mm: float = Field(default=950.0, description="Mean annual rainfall in mm")
    kharif_rainfall_mm: float = Field(default=720.0, description="Monsoon (June-Sept) rainfall in mm")
    summer_max_temp_c: float = Field(default=39.5, description="Peak summer temperature °C")
    winter_min_temp_c: float = Field(default=9.0, description="Lowest winter temperature °C")
    average_humidity_pct: float = Field(default=62.0, description="Mean relative humidity %")
    agro_climatic_zone_id: int = Field(default=4, description="ICAR Agro-Climatic Zone (1 to 15)")
    agro_climatic_zone_name: str = Field(default="Middle Gangetic Plain Region")
    elevation_masl: float = Field(default=120.0, description="Elevation in meters above sea level")


class FarmProfile(BaseModel):
    farm_id: str = Field(default="FARM-001", description="Unique Farm Identifier")
    farmer_name: str = Field(default="Kisan Mitra", description="Farmer / Owner Name")
    state: str = Field(default="Uttar Pradesh", description="Indian State")
    district: str = Field(default="Varanasi", description="District")
    sub_district_block: Optional[str] = Field(default="Kashi", description="Tehsil or Block")
    latitude: Optional[float] = Field(default=25.3176, description="GPS Latitude")
    longitude: Optional[float] = Field(default=82.9739, description="GPS Longitude")
    total_area_acres: float = Field(default=2.5, description="Total farm holding area in acres")
    cultivable_area_acres: float = Field(default=2.3, description="Cultivable area in acres")
    farmer_category: str = Field(default="Small (1-2 ha)", description="Marginal (<1 ha), Small (1-2 ha), Semi-Medium (2-4 ha), Medium (4-10 ha), Large (>10 ha)")
    farming_experience_level: str = Field(default="Beginner", description="Beginner (0 yrs), Intermediate (1-5 yrs), Experienced (5+ yrs)")
    has_fencing: bool = Field(default=False, description="Boundary protective fencing present")
    soil: SoilProfile = Field(default_factory=SoilProfile)
    water: WaterProfile = Field(default_factory=WaterProfile)
    climate: ClimateProfile = Field(default_factory=ClimateProfile)
    created_at: str = Field(default="2026-11-08")
