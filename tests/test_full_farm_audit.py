"""
Unit tests for FullFarmAuditor and AgribusinessIncubator.
"""

import pytest
from amifarmer.core.full_farm_audit import FullFarmAuditor
from amifarmer.core.agribusiness_incubator import AgribusinessIncubator


def test_full_farm_audit_pipeline():
    auditor = FullFarmAuditor()
    farm = auditor.create_beginner_profile(
        farmer_name="Sanjay Verma",
        state="Uttar Pradesh",
        district="Varanasi",
        farm_area_acres=4.0
    )
    report = auditor.run_full_audit(farm)

    assert "dossier_id" in report
    assert "soil_analysis" in report
    assert "hydrology_and_water_security" in report
    assert len(report["top_crop_recommendations"]) > 0
    assert "government_subsidies_and_schemes" in report
    assert "turnkey_agribusiness_dpr" in report
    assert report["government_subsidies_and_schemes"]["total_potential_benefit_inr"] > 0


def test_agribusiness_incubator_dpr():
    incubator = AgribusinessIncubator()
    models = incubator.list_available_models()
    assert len(models) >= 4

    dpr = incubator.generate_bankable_dpr(
        model_id=models[0]["model_id"],
        farmer_name="Pooja Sharma",
        farm_location="Indore, Madhya Pradesh"
    )
    assert dpr["capital_structure"]["total_project_capex_inr"] > 0
    assert len(dpr["three_year_cash_flow_projection"]) == 3
    assert dpr["financial_viability_metrics"]["payback_period_years"] > 0
