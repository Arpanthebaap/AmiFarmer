"""
Unit tests for AmiFarmer SoilAnalyzer.
"""

import pytest
from amifarmer.models.farm_profile import SoilProfile, SoilNutrients, SoilTexture
from amifarmer.core.soil_analyzer import SoilAnalyzer


def test_soil_health_score_neutral_balanced():
    analyzer = SoilAnalyzer()
    soil = SoilProfile(
        texture=SoilTexture.ALLUVIAL,
        nutrients=SoilNutrients(
            nitrogen_kg_ha=350.0,
            phosphorus_kg_ha=20.0,
            potassium_kg_ha=220.0,
            organic_carbon_pct=0.85,
            ph=7.0,
            electrical_conductivity_ds_m=0.5
        )
    )
    score = analyzer.calculate_soil_health_score(soil)
    assert 85.0 <= score <= 100.0, f"Expected high score for optimal soil, got {score}"


def test_soil_health_score_alkaline_sodic_penalization():
    analyzer = SoilAnalyzer()
    soil = SoilProfile(
        texture=SoilTexture.SALINE_ALKALINE,
        nutrients=SoilNutrients(
            nitrogen_kg_ha=140.0,
            phosphorus_kg_ha=8.0,
            potassium_kg_ha=110.0,
            organic_carbon_pct=0.25,
            ph=9.2,
            electrical_conductivity_ds_m=3.5
        )
    )
    analysis = analyzer.analyze_soil(soil)
    assert analysis["soil_health_score"] < 45.0, "Expected low score for degraded sodic soil"
    assert any("Alkaline/Sodic" in d for d in analysis["deficiencies"])
    assert any("Gypsum" in a for a in analysis["amendment_plan"])
