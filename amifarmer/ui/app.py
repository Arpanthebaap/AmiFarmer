"""
AmiFarmer - Interactive Streamlit Web Application & Farmer Operating System.
Provides interactive visual analytics for soil diagnostics, groundwater hydrology,
Pareto-optimal crop recommendations, mandi price arbitrage, government subsidies, and agribusiness DPRs.
"""

import sys
from pathlib import Path

# Add project root to sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

import json
import streamlit as st
import pandas as pd
import numpy as np

from amifarmer.models.farm_profile import (
    FarmProfile,
    SoilProfile,
    SoilNutrients,
    SoilTexture,
    WaterProfile,
    ClimateProfile,
    GroundwaterCategory
)
from amifarmer.core.full_farm_audit import FullFarmAuditor
from amifarmer.data import load_agro_climatic_zones

# Set Streamlit Page Configuration
st.set_page_config(
    page_title="AmiFarmer | Autonomous Agricultural Intelligence Engine",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for modern styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.3rem;
        font-weight: 800;
        color: #1e7e34;
        margin-bottom: 0.2rem;
    }
    .sub-header {
        font-size: 1.1rem;
        color: #495057;
        margin-bottom: 1.5rem;
    }
    .metric-card {
        background-color: #f8f9fa;
        border-radius: 8px;
        padding: 1rem;
        border-left: 5px solid #28a745;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    .badge-tag {
        display: inline-block;
        padding: 0.25rem 0.6rem;
        border-radius: 4px;
        font-size: 0.85rem;
        font-weight: 600;
        margin-right: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)


@st.cache_resource
def get_auditor():
    return FullFarmAuditor()


@st.cache_data
def get_zones():
    return load_agro_climatic_zones()


auditor = get_auditor()
zones_data = get_zones()

# Collect list of states and sample districts
state_district_map = {
    "Maharashtra": ["Nashik", "Pune", "Ahmednagar", "Solapur", "Nagpur", "Amravati", "Jalgaon"],
    "Punjab": ["Ludhiana", "Amritsar", "Karnal", "Kurukshetra", "Sirsa", "Sri Ganganagar"],
    "Uttar Pradesh": ["Varanasi", "Gorakhpur", "Prayagraj", "Meerut", "Aligarh", "Bareilly", "Agra"],
    "Bihar": ["Patna", "Muzaffarpur", "Gaya", "Samastipur", "Bhagalpur"],
    "West Bengal": ["Hooghly", "Burdwan (Purba Bardhaman)", "Nadia", "Murshidabad", "North 24 Parganas"],
    "Madhya Pradesh": ["Indore", "Bhopal", "Ujjain", "Kota", "Jabalpur", "Sagar"],
    "Karnataka": ["Belagavi", "Tumakuru", "Dharwad", "Dakshina Kannada", "Wayanad", "Shimoga"],
    "Andhra Pradesh / Telangana": ["Warangal", "Anantapur", "Kurnool", "Guntur", "Krishna", "West Godavari"],
    "Rajasthan": ["Jodhpur", "Bikaner", "Jaisalmer", "Barmer", "Nagaur", "Kota"],
    "Gujarat": ["Rajkot", "Junagadh", "Mehsana", "Anand", "Surat", "Vadodara"]
}

# --- SIDEBAR CONTROLS ---
with st.sidebar:
    st.image("https://img.icons8.com/color/96/tractor.png", width=64)
    st.title("🌾 AmiFarmer OS")
    st.markdown("**Autonomous Agricultural Intelligence**")
    st.divider()

    mode = st.radio(
        "Farmer Experience Mode",
        ["🌱 Beginner (Zero Knowledge)", "🔬 Advanced (Custom Soil Test Report)"],
        index=0
    )

    farmer_name = st.text_input("Farmer / Entrepreneur Name", value="Kisan Mitra")
    state_selected = st.selectbox("Select State", list(state_district_map.keys()), index=0)
    districts = state_district_map.get(state_selected, ["District 1", "District 2"])
    district_selected = st.selectbox("Select District", districts, index=0)
    farm_acres = st.slider("Farm Holding Area (Acres)", min_value=0.5, max_value=50.0, value=3.0, step=0.5)

    season_filter = st.selectbox(
        "Farming Season Filter",
        ["All Seasons", "Kharif (Monsoon: June - Oct)", "Rabi (Winter: Nov - April)", "Zaid (Summer: March - June)", "Perennial / Year-Round"],
        index=0
    )
    season_arg = None if season_filter == "All Seasons" else season_filter

    if mode == "🔬 Advanced (Custom Soil Test Report)":
        st.subheader("Lab Soil Analysis")
        in_ph = st.slider("Soil pH", 4.0, 10.0, 7.2, 0.1)
        in_oc = st.slider("Organic Carbon (%)", 0.1, 2.0, 0.58, 0.05)
        in_n = st.number_input("Available Nitrogen (kg/ha)", value=260.0)
        in_p = st.number_input("Available Phosphorus (kg/ha)", value=16.0)
        in_k = st.number_input("Available Potassium (kg/ha)", value=190.0)
        in_ec = st.number_input("Electrical Conductivity (dS/m)", value=0.55)
        in_gw = st.slider("Water Table Depth (mbgl)", 2.0, 80.0, 16.5, 0.5)

    st.markdown("---")
    st.caption("AmiFarmer v1.0.0 • ICAR & CGWB Aligned")

# Create farm profile
if mode == "🌱 Beginner (Zero Knowledge)":
    farm = auditor.create_beginner_profile(
        farmer_name=farmer_name,
        state=state_selected,
        district=district_selected,
        farm_area_acres=farm_acres,
        experience_level="Beginner (Zero Knowledge)"
    )
else:
    # Custom advanced profile
    base_farm = auditor.create_beginner_profile(
        farmer_name=farmer_name,
        state=state_selected,
        district=district_selected,
        farm_area_acres=farm_acres,
        experience_level="Advanced Custom"
    )
    base_farm.soil.nutrients.ph = in_ph
    base_farm.soil.nutrients.organic_carbon_pct = in_oc
    base_farm.soil.nutrients.nitrogen_kg_ha = in_n
    base_farm.soil.nutrients.phosphorus_kg_ha = in_p
    base_farm.soil.nutrients.potassium_kg_ha = in_k
    base_farm.soil.nutrients.electrical_conductivity_ds_m = in_ec
    base_farm.water.groundwater_depth_mbgl = in_gw
    farm = base_farm

# Run full audit
audit = auditor.run_full_audit(farm, season_filter=season_arg)

# --- HEADER SECTION ---
st.markdown(f"<div class='main-header'>AmiFarmer (अमीफार्मर) - Precision Farm Operating System</div>", unsafe_allow_html=True)
st.markdown(
    f"<div class='sub-header'>Location: <b>{farm.district}, {farm.state}</b> | Area: <b>{farm.total_area_acres} Acres</b> | Category: <b>{farm.farmer_category}</b></div>",
    unsafe_allow_html=True
)

# Top KPI Highlights
top_crop = audit["top_crop_recommendations"][0] if audit["top_crop_recommendations"] else None
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    shs = audit["soil_analysis"]["soil_health_score"]
    st.metric("Soil Health Score", f"{shs}/100", audit["soil_analysis"]["soil_health_grade"])

with col2:
    gw_d = audit["hydrology_and_water_security"]["groundwater_status"]["depth_mbgl"]
    gw_cat = audit["hydrology_and_water_security"]["groundwater_status"]["status_title"]
    st.metric("Water Table Depth", f"{gw_d} mbgl", gw_cat)

with col3:
    if top_crop:
        st.metric("Top Recommended Crop", top_crop["crop_name"], f"{top_crop['suitability_score_pct']}% Match")

with col4:
    if top_crop:
        profit_total = top_crop["net_profit_per_acre_inr"] * farm.cultivable_area_acres
        st.metric("Expected Net Profit", f"₹{top_crop['net_profit_per_acre_inr']:,}/acre", f"₹{profit_total:,.0f} Total")

with col5:
    sub_count = audit["government_subsidies_and_schemes"]["total_schemes_eligible"]
    sub_val = audit["government_subsidies_and_schemes"]["total_potential_benefit_inr"]
    st.metric("Subsidies Unlocked", f"{sub_count} Schemes", f"₹{sub_val:,} Cap")

st.info(audit["executive_summary"])

# --- TABBED DEEP DIVE ---
tabs = st.tabs([
    "🏆 Crop Recommendations",
    "🌱 Soil & Pedology Diagnostics",
    "💧 Water Table & Solar Pumping",
    "📈 Mandi Prices & Market Arbitrage",
    "🗓️ 7-Stage Agronomy Calendar",
    "🛡️ Pest & Disease Protection (IPM)",
    "🚜 Farm Machinery & Mechanization",
    "🏛️ Subsidies & Schemes Portal",
    "💼 Turnkey Agribusiness DPR",
    "📥 Export Audit Dossier"
])

# ----------------- TAB 1: CROP RECOMMENDATIONS -----------------
with tabs[0]:
    st.subheader("Pareto-Optimal Crop & Vegetable Selection")
    st.caption("Ranked by multi-objective algorithm: 45% biophysical suitability + 55% economic profitability.")

    rec_df = []
    for r in audit["top_crop_recommendations"]:
        rec_df.append({
            "Crop Name": f"{r['crop_name']} ({r['hindi_name']})",
            "Category": r["category"],
            "Pareto Score": r["pareto_composite_score"],
            "Suitability %": r["suitability_score_pct"],
            "Yield (Qtl/Acre)": r["expected_yield_quintals_per_acre"],
            "Cost/Acre (₹)": r["cost_of_cultivation_per_acre_inr"],
            "Net Profit/Acre (₹)": r["net_profit_per_acre_inr"],
            "ROI (%)": r["return_on_investment_pct"],
            "Growth Days": r["growth_cycle_days"],
            "Risk Level": r["risk_level"]
        })

    df_crops = pd.DataFrame(rec_df)
    st.dataframe(df_crops, use_container_width=True)

    # Detailed card for Top 3 crops
    st.markdown("### Top 3 Recommended Cropping Profiles")
    top3_cols = st.columns(3)
    for i, c in enumerate(audit["top_crop_recommendations"][:3]):
        with top3_cols[i]:
            st.markdown(f"#### #{i+1} {c['crop_name']}")
            st.caption(f"{c['scientific_name']} | *{c['hindi_name']}*")
            st.write(f"**Net Profit:** :green[₹{c['net_profit_per_acre_inr']:,} / acre]")
            st.write(f"**Wholesale Mandi Rate:** ₹{c['market_modal_price_per_quintal_inr']:,}/Qtl")
            st.write(f"**Cycle Duration:** {c['growth_cycle_days']} Days")
            st.write(f"**Risk Level:** {c['risk_level']}")
            st.write(f"**Recommended Channel:** {c['recommended_channel']}")
            st.markdown("**Key Advantages:**")
            for adv in c["primary_advantages"]:
                st.markdown(f"- ✅ {adv}")
            if c["limiting_factors_or_precautions"]:
                st.markdown("**Precautions:**")
                for prec in c["limiting_factors_or_precautions"]:
                    st.markdown(f"- ⚠️ {prec}")

# ----------------- TAB 2: SOIL & PEDOLOGY -----------------
with tabs[1]:
    st.subheader("Soil Fertility, Texture & Reclamation Plan")
    soil_data = audit["soil_analysis"]
    col_s1, col_s2 = st.columns(2)

    with col_s1:
        st.markdown(f"**Soil Texture Type:** `{soil_data['texture']}`")
        st.markdown(f"**Soil Health Score:** **{soil_data['soil_health_score']}/100** ({soil_data['soil_health_grade']})")

        phys = soil_data["physical_properties"]
        st.markdown("#### Soil Physical & Hydraulic Properties")
        st.write(f"- **Bulk Density:** {phys['bulk_density_g_cm3']} g/cm³")
        st.write(f"- **Total Porosity:** {phys['porosity_pct']}%")
        st.write(f"- **Available Water Capacity (AWC):** {phys['available_water_capacity_mm_m']} mm/meter depth")
        st.write(f"- **Cation Exchange Capacity (CEC):** {phys['cation_exchange_capacity_meq_100g']} meq/100g")

        st.markdown("#### Soil Strengths")
        for s in soil_data["strengths"]:
            st.success(f"✔ {s}")

    with col_s2:
        st.markdown("#### Detected Nutrient Deficiencies & Stress Factors")
        for d in soil_data["deficiencies"]:
            st.warning(f"⚠ {d}")

        st.markdown("#### Tailored Soil Amendment & Reclamation Roadmap")
        for a in soil_data["amendment_plan"]:
            st.info(f"💊 {a}")

        if soil_data.get("benchmark_guidelines"):
            st.caption(f"ICAR Regional Guideline: {soil_data['benchmark_guidelines']}")

# ----------------- TAB 3: WATER & SOLAR PUMPING -----------------
with tabs[2]:
    st.subheader("Groundwater Table Assessment & Solar Pump Sizing")
    hydro = audit["hydrology_and_water_security"]
    gw = hydro["groundwater_status"]
    pump = hydro["solar_pump_sizing"]
    irrig = hydro["irrigation_recommendation"]

    col_w1, col_w2 = st.columns(2)

    with col_w1:
        st.markdown("#### Groundwater Aquifer Status (CGWB)")
        st.write(f"- **Depth to Water Level:** **{gw['depth_mbgl']} meters below ground level (mbgl)**")
        st.write(f"- **Classification:** `{gw['category']}`")
        st.write(f"- **Aquifer Sustainability Score:** {gw['sustainability_score']}/100")
        st.write(f"- **Recharge Ease:** {gw['recharge_ease']}")
        st.write(f"- **Drainage / Waterlogging Risk:** {gw['drainage_risk']}")

        st.markdown("#### Recommended Irrigation Method")
        st.success(f"🎯 **{irrig['recommended_method']}**")
        st.write(f"- **Water Savings vs Flood Irrigation:** {irrig['water_savings_pct']}%")
        st.write(f"- **Yield Boost:** +{irrig['yield_increase_pct']}%")
        for j in irrig["justification"]:
            st.markdown(f"- {j}")

    with col_w2:
        st.markdown("#### PM-KUSUM Standalone Solar Agriculture Pump Sizing")
        st.write(f"- **Total Dynamic Head (TDH):** {pump['total_dynamic_head_m']} meters")
        st.write(f"- **Hourly Discharge:** {pump['flow_rate_m3_per_hour']} m³/hour")
        st.write(f"- **Recommended Pump Capacity:** **{pump['recommended_pump_hp']} HP** Submersible")
        st.write(f"- **Solar PV Array Required:** **{pump['recommended_solar_pv_array_wp']} Watts peak (Wp)**")
        st.markdown("---")
        st.write(f"- **Benchmark Cost:** ₹{pump['estimated_system_cost_inr']:,}")
        st.write(f"- **PM-KUSUM 60% Subsidy:** :green[₹{pump['pm_kusum_subsidy_inr']:,}]")
        st.write(f"- **Net Farmer Share:** **₹{pump['net_farmer_cost_inr']:,}**")
        st.write(f"- **Annual Diesel Fuel Saved:** {pump['annual_diesel_saved_liters']} Litres/year")
        st.write(f"- **Annual Money Saved:** :green[₹{pump['annual_cost_savings_inr']:,} / year]")
        st.write(f"- **Payback Period:** **{pump['payback_period_years']} Years**")

# ----------------- TAB 4: MARKET INTELLIGENCE -----------------
with tabs[3]:
    st.subheader("Market Intelligence, APMC Mandi Rates & D2C Arbitrage")
    mkt = audit["market_intelligence_and_arbitrage"]
    if mkt:
        st.write(f"Crop Analyzed: **{mkt['crop_name']}** (Total Output: **{mkt['total_harvest_kg']:,.0f} kg**)")

        col_m1, col_m2, col_m3, col_m4 = st.columns(4)
        with col_m1:
            st.metric("Mandi Wholesale Rate", f"₹{mkt['mandi_wholesale']['rate_per_kg_inr']}/kg", f"₹{mkt['mandi_wholesale']['net_revenue_per_acre_inr']:,}/acre")
        with col_m2:
            st.metric("FPO Collective Rate", f"₹{mkt['fpo_collective']['rate_per_kg_inr']}/kg", f"+{mkt['fpo_collective']['gain_over_mandi_pct']}% vs Mandi")
        with col_m3:
            st.metric("Direct-to-Consumer (D2C)", f"₹{mkt['direct_to_consumer']['rate_per_kg_inr']}/kg", f"+{mkt['direct_to_consumer']['gain_over_mandi_pct']}% vs Mandi")
        with col_m4:
            msp_val = mkt["msp_procurement"]["msp_rate_per_quintal_inr"]
            st.metric("MSP Minimum Support Price", f"₹{msp_val:,}/Qtl" if msp_val else "N/A (Horticulture)", "Govt Procurement" if msp_val else "Open Market")

        st.markdown("#### Post-Harvest Value Addition Multiplier")
        va = mkt.get("value_addition")
        if va:
            st.success(f"💡 **Opportunity:** {va['product_type']}")
            col_v1, col_v2, col_v3 = st.columns(3)
            with col_v1:
                st.write(f"- **Value Multiplier:** {va['value_multiplier']}x raw price")
                st.write(f"- **Processing Cost:** ₹{va['processing_cost_inr']:,}")
            with col_v2:
                st.write(f"- **Gross Processed Revenue:** ₹{va['gross_processed_revenue_inr']:,}")
                st.write(f"- **Net Processed Revenue:** ₹{va['net_processed_revenue_inr']:,}")
            with col_v3:
                st.write(f"- **Extra Profit over Raw Mandi:** :green[**+₹{va['incremental_profit_over_mandi_inr']:,}**]")
                st.write(f"- **Income Boost:** :green[**+{va['percentage_income_boost']}%**]")
        else:
            st.info("Primary grading, sorting into plastic crates, and pre-cooling provides 15-20% higher market realization.")

        st.caption(f"Storage Advisory: {mkt['storage_advisory']}")

# ----------------- TAB 5: AGRONOMY CALENDAR -----------------
with tabs[4]:
    st.subheader(f"Step-by-Step Agronomy Calendar: {audit['agronomy_operational_roadmap']['crop_name']}")
    sched = audit["agronomy_operational_roadmap"]
    st.write(f"**Total Growth Duration:** {sched['total_growth_duration_days']} Days | **Strategy:** {sched['irrigation_philosophy']}")

    for stage in sched["operational_stages"]:
        with st.expander(f"Stage {stage['stage_number']}: {stage['stage_name']} ({stage['day_range']})", expanded=(stage['stage_number'] <= 1)):
            for op in stage["key_operations"]:
                st.markdown(f"- 🔹 {op}")

    st.warning(f"Safety Standard: {sched['safety_guideline']}")

# ----------------- TAB 6: PLANT PROTECTION (IPM) -----------------
with tabs[5]:
    st.subheader(f"Integrated Pest Management (IPM) & Disease Therapeutics: {top_crop['crop_name'] if top_crop else 'Crops'}")
    ipm_list = audit["integrated_pest_management"] or []

    for issue in ipm_list:
        with st.container():
            st.markdown(f"### 🐛 {issue['issue_name']} ({issue['type']})")
            st.write(f"**Symptoms:** {issue['symptoms']}")
            col_p1, col_p2 = st.columns(2)
            with col_p1:
                st.success(f"🌿 **Biological & Organic Preventive:** {issue['organic_preventive']}")
            with col_p2:
                st.error(f"🧪 **Emergency Chemical Curative:** {issue['chemical_curative']}")
                st.caption(f"Mandatory Pre-Harvest Interval (PHI): **{issue['pre_harvest_interval_days']} days** before harvesting")
            st.divider()

# ----------------- TAB 7: MECHANIZATION & CHC -----------------
with tabs[6]:
    st.subheader("Farm Machinery Sizing & Custom Hiring Center (CHC) Advisor")
    mech = audit["mechanization_and_equipment_plan"]

    st.write(f"Farm Holding: **{mech['farm_area_acres']} Acres** ({mech['farmer_holding_class']})")
    col_fin1, col_fin2, col_fin3 = st.columns(3)
    with col_fin1:
        st.metric("Total Equipment Value", f"₹{mech['financial_summary']['total_equipment_cost_inr']:,}")
    with col_fin2:
        st.metric("SMAM Subsidy Unlocked", f"₹{mech['financial_summary']['total_government_subsidy_inr']:,}", f"{mech['financial_summary']['subsidy_absorption_pct']}% Coverage")
    with col_fin3:
        st.metric("Net Farmer Share", f"₹{mech['financial_summary']['net_farmer_capital_required_inr']:,}")

    st.markdown("#### Recommended Purchases (with Subsidies)")
    for p in mech["recommended_purchases"]:
        st.markdown(f"- **{p['name']}**: Cost ₹{p['cost_inr']:,} | Subsidy: :green[₹{p['subsidy_inr']:,}] | Net: **₹{p['farmer_share_inr']:,}** ({p['rationale']})")

    st.markdown("#### Shared Ownership & Rental Recommendations (CHC)")
    for r in mech["rental_from_chc_strategy"]:
        st.markdown(f"- 🚜 **{r['equipment']}**: Rate `{r['chc_rate']}` — *{r['reason']}*")

    st.info(mech["chc_app_advisory"])

# ----------------- TAB 8: GOVERNMENT SUBSIDIES -----------------
with tabs[7]:
    st.subheader("Government Agriculture Subsidies & Schemes Portal")
    sub_rep = audit["government_subsidies_and_schemes"]
    st.write(f"Total Eligible Schemes: **{sub_rep['total_schemes_eligible']}** | Cumulative Financial Benefits: :green[**₹{sub_rep['total_potential_benefit_inr']:,}**]")

    for s in sub_rep["matched_schemes"]:
        with st.expander(f"🏛️ {s['acronym']} - {s['scheme_name']} (Benefit: ₹{s['estimated_benefit_inr']:,})"):
            st.write(f"**Ministry:** {s['ministry']}")
            st.write(f"**Category:** {s['category']}")
            st.markdown("**Eligibility Rationale:**")
            for q in s["qualification_highlights"]:
                st.markdown(f"- {q}")
            st.markdown("**Documents Required:**")
            for doc in s["documents_required"]:
                st.markdown(f"- 📄 {doc}")
            st.markdown(f"**Direct Application Portal:** [{s['official_portal']}]({s['official_portal']})")
            st.markdown("**How to Apply Steps:**")
            for step in s["application_steps"]:
                st.markdown(f"1. {step}")

# ----------------- TAB 9: AGRIBUSINESS DPR -----------------
with tabs[8]:
    st.subheader("Bankable Agribusiness Detailed Project Report (DPR)")
    biz = audit["turnkey_agribusiness_dpr"]

    st.markdown(f"### Project Title: {biz['project_title']}")
    st.caption(f"Promoter: {biz['promoter_name']} | Location: {biz['project_location']} | Sector: {biz['target_sector']}")

    col_b1, col_b2, col_b3, col_b4 = st.columns(4)
    with col_b1:
        st.metric("Total Project CapEx", f"₹{biz['capital_structure']['total_project_capex_inr']:,}")
    with col_b2:
        st.metric("Government Subsidy", f"₹{biz['capital_structure']['government_capital_subsidy_inr']:,}")
    with col_b3:
        st.metric("Promoter Margin Money", f"₹{biz['capital_structure']['promoter_margin_money_inr']:,}")
    with col_b4:
        st.metric("Bank Term Loan", f"₹{biz['capital_structure']['bank_term_loan_required_inr']:,}")

    st.markdown("#### 3-Year Cash Flow & Profitability Projections")
    df_cf = pd.DataFrame(biz["three_year_cash_flow_projection"])
    st.dataframe(df_cf, use_container_width=True)

    col_vm1, col_vm2, col_vm3 = st.columns(3)
    with col_vm1:
        st.write(f"- **Payback Period:** **{biz['financial_viability_metrics']['payback_period_years']} Years**")
    with col_vm2:
        st.write(f"- **Internal Rate of Return (IRR):** **{biz['financial_viability_metrics']['internal_rate_of_return_irr_pct']}%**")
    with col_vm3:
        st.write(f"- **Debt Service Coverage Ratio (DSCR):** **{biz['financial_viability_metrics']['debt_service_coverage_ratio_dscr']}**")

    st.markdown("#### Required Plant & Machinery")
    for m in biz["plant_and_machinery"]:
        st.markdown(f"- ⚙ {m}")

    st.markdown("#### Statutory Licenses Required")
    for lic in biz["statutory_licenses_and_approvals"]:
        st.markdown(f"- 📜 {lic}")

    st.markdown("#### 90-Day Execution Roadmap for Beginners")
    for stp in biz["step_by_step_execution_roadmap"]:
        st.markdown(f"- 🚀 {stp}")

# ----------------- TAB 10: EXPORT DOSSIER -----------------
with tabs[9]:
    st.subheader("Export 360° Farm Master Audit Report")
    st.caption("Generate verifiable JSON or Markdown dossiers for bank loans, KCC expansion, or subsidy submissions.")

    report_json_str = json.dumps(audit, indent=2, ensure_ascii=False)
    st.download_button(
        label="📥 Download Complete Audit Report (JSON)",
        data=report_json_str,
        file_name=f"amifarmer_audit_{farm.district}_{farm.total_area_acres}acres.json",
        mime="application/json"
    )

    st.markdown("#### Raw Audit Snapshot Preview")
    st.json(audit["executive_summary"])
