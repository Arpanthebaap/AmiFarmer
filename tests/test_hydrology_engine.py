"""
Unit tests for AmiFarmer HydrologyEngine.
"""

import pytest
from amifarmer.core.hydrology_engine import HydrologyEngine


def test_evaluate_groundwater_shallow_vs_deep():
    hydro = HydrologyEngine()
    shallow = hydro.evaluate_groundwater_status(4.0)
    assert shallow["sustainability_score"] > 85.0
    assert "Shallow" in shallow["status_title"] or "Safe" in shallow["category"]

    deep = hydro.evaluate_groundwater_status(45.0)
    assert deep["sustainability_score"] <= 45.0
    assert "Critical" in deep["category"] or "Critical" in deep["status_title"]


def test_solar_pump_sizing():
    hydro = HydrologyEngine()
    res = hydro.size_solar_irrigation_pump(water_depth_mbgl=18.0, farm_area_acres=3.0)
    assert res["recommended_pump_hp"] in [3.0, 5.0, 7.5, 10.0]
    assert res["pm_kusum_subsidy_inr"] > 0
    assert res["annual_cost_savings_inr"] > 0
    assert res["payback_period_years"] < 6.0
