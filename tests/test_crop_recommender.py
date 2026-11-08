"""
Unit tests for AmiFarmer CropRecommender.
"""

import pytest
from amifarmer.models.farm_profile import FarmProfile, SoilProfile, SoilTexture, WaterProfile, ClimateProfile
from amifarmer.core.crop_recommender import CropRecommender


def test_crop_recommender_returns_ranked_results():
    recommender = CropRecommender()
    farm = FarmProfile(
        farm_id="TEST-001",
        state="Maharashtra",
        district="Nashik",
        total_area_acres=3.0,
        cultivable_area_acres=2.7,
        soil=SoilProfile(texture=SoilTexture.BLACK_COTTON),
        water=WaterProfile(groundwater_depth_mbgl=16.5),
        climate=ClimateProfile(annual_rainfall_mm=750.0)
    )

    recs = recommender.get_recommendations(farm, top_n=5)
    assert len(recs) == 5
    assert recs[0]["pareto_composite_score"] >= recs[1]["pareto_composite_score"]
    assert "net_profit_per_acre_inr" in recs[0]
    assert "suitability_score_pct" in recs[0]
