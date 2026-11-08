"""
Unit tests for AmiFarmer MarketIntelligence and SubsidyMatcher.
"""

import pytest
from amifarmer.core.market_intelligence import MarketIntelligence
from amifarmer.core.subsidy_matcher import SubsidyMatcher
from amifarmer.core.full_farm_audit import FullFarmAuditor


def test_market_arbitrage_calculation():
    intel = MarketIntelligence()
    res = intel.analyze_market_options(
        crop_name="Mustard / Rapeseed",
        yield_quintals_per_acre=10.0,
        modal_mandi_price_inr=6200.0,
        d2c_price_inr=9500.0,
        msp_inr=5950.0
    )
    assert res["total_harvest_kg"] == 1000.0
    assert res["mandi_wholesale"]["net_revenue_per_acre_inr"] > 0
    assert res["direct_to_consumer"]["net_revenue_per_acre_inr"] > res["mandi_wholesale"]["net_revenue_per_acre_inr"]
    assert res["value_addition"] is not None
    assert res["value_addition"]["percentage_income_boost"] > 20.0


def test_subsidy_matcher_eligibility():
    matcher = SubsidyMatcher()
    auditor = FullFarmAuditor()
    farm = auditor.create_beginner_profile(
        farmer_name="Test Farmer",
        state="Punjab",
        district="Ludhiana",
        farm_area_acres=2.5
    )
    sub = matcher.evaluate_eligibility(farm)
    assert sub["total_schemes_eligible"] >= 4
    assert sub["total_potential_benefit_inr"] > 50000.0
    assert any(s["acronym"] == "PM-KISAN" for s in sub["matched_schemes"])
    assert any(s["acronym"] == "PMKSY-PDMC" for s in sub["matched_schemes"])
