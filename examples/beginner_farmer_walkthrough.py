"""
AmiFarmer - Beginner Farmer End-to-End Walkthrough Script.
Simulates a first-time farmer with 2.5 acres of land in Nashik, Maharashtra,
with zero prior agricultural experience, creating a complete seed-to-wealth roadmap.
"""

import sys
from pathlib import Path

# Fix Windows console UTF-8 encoding
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

# Add project root to sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from amifarmer.core.full_farm_audit import FullFarmAuditor
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console(force_terminal=True, legacy_windows=False)


def run_walkthrough():
    console.print(Panel(
        "[bold green]🌾 AmiFarmer Beginner Farmer Walkthrough: Zero Knowledge to Sustainable Rural Wealth[/bold green]\n"
        "[white]Scenario: An urban professional or first-generation rural youth inheriting 2.5 acres in Nashik, Maharashtra.[/white]",
        style="bold green"
    ))

    auditor = FullFarmAuditor()

    # Step 1: Initialize Beginner Farm Profile (Zero Knowledge)
    console.print("[bold yellow]Step 1: Ingesting Regional Baselines (ICAR & CGWB Database)...[/bold yellow]")
    farm = auditor.create_beginner_profile(
        farmer_name="Rohit Patil",
        state="Maharashtra",
        district="Nashik",
        farm_area_acres=2.5,
        experience_level="Beginner (Zero Knowledge)"
    )
    console.print(f"✔ Farm Profile Initialized: {farm.farm_id} in {farm.district}, {farm.state}")
    console.print(f"✔ Predominant Soil: {farm.soil.texture.value} | Initial Water Table: {farm.water.groundwater_depth_mbgl} mbgl\n")

    # Step 2: Run Full Multi-Disciplinary Farm Audit
    console.print("[bold yellow]Step 2: Executing Autonomous 360° Agro-Pedological & Economic Audit...[/bold yellow]")
    audit = auditor.run_full_audit(farm)

    # Step 3: Soil Diagnostics
    soil = audit["soil_analysis"]
    console.print(f"✔ Soil Health Score: [bold green]{soil['soil_health_score']}/100[/bold green] ({soil['soil_health_grade']})")
    for d in soil["deficiencies"]:
        console.print(f"  ⚠ Deficiency Detected: {d}")
    for a in soil["amendment_plan"]:
        console.print(f"  💊 Actionable Prescription: {a}")

    # Step 4: Hydrology & Solar Pumping
    gw = audit["hydrology_and_water_security"]["groundwater_status"]
    pump = audit["hydrology_and_water_security"]["solar_pump_sizing"]
    console.print(f"\n✔ Groundwater Status: [bold cyan]{gw['status_title']}[/bold cyan] ({gw['depth_mbgl']} mbgl)")
    console.print(f"✔ Solar Pump Sizing: [bold green]{pump['recommended_pump_hp']} HP[/bold green] Submersible with {pump['recommended_solar_pv_array_wp']} Wp Solar Array")
    console.print(f"✔ Capital Cost: ₹{pump['estimated_system_cost_inr']:,} | PM-KUSUM 60% Subsidy: ₹{pump['pm_kusum_subsidy_inr']:,} | Net Share: ₹{pump['net_farmer_cost_inr']:,}")
    console.print(f"✔ Annual Diesel Saved: {pump['annual_diesel_saved_liters']} L (₹{pump['annual_cost_savings_inr']:,}/year savings)\n")

    # Step 5: Crop Recommendations
    console.print("[bold yellow]Step 3: Evaluating Pareto-Optimal Crops & Vegetables...[/bold yellow]")
    table = Table(title="Top Crop Options for Rohit's Farm")
    table.add_column("Rank", style="yellow")
    table.add_column("Crop", style="bold white")
    table.add_column("Category", style="cyan")
    table.add_column("Net Profit / Acre", style="bold green")
    table.add_column("Growth Days", style="white")

    for i, c in enumerate(audit["top_crop_recommendations"][:5], 1):
        table.add_row(
            str(i),
            f"{c['crop_name']} ({c['hindi_name']})",
            c["category"],
            f"₹{c['net_profit_per_acre_inr']:,}",
            f"{c['growth_cycle_days']} days"
        )
    console.print(table)

    # Step 6: Subsidies Unlocked
    sub = audit["government_subsidies_and_schemes"]
    console.print(f"\n✔ Unlocked [bold green]{sub['total_schemes_eligible']} Government Subsidies[/bold green] with total potential benefit of [bold green]₹{sub['total_potential_benefit_inr']:,}[/bold green]:")
    for s in sub["matched_schemes"][:4]:
        console.print(f"  🏛 {s['acronym']}: ₹{s['estimated_benefit_inr']:,} ({s['category']}) -> {s['official_portal']}")

    # Step 7: Agribusiness DPR
    biz = audit["turnkey_agribusiness_dpr"]
    console.print(f"\n✔ Bankable Agribusiness DPR Prepared: [bold blue]{biz['project_title']}[/bold blue]")
    console.print(f"  • Total CapEx: ₹{biz['capital_structure']['total_project_capex_inr']:,}")
    console.print(f"  • Expected Subsidy: ₹{biz['capital_structure']['government_capital_subsidy_inr']:,}")
    console.print(f"  • Year 2 Projected Net Profit: ₹{biz['three_year_cash_flow_projection'][1]['net_profit_inr']:,}")
    console.print(f"  • Payback Period: {biz['financial_viability_metrics']['payback_period_years']} years (IRR: {biz['financial_viability_metrics']['internal_rate_of_return_irr_pct']}%)")

    console.print("\n[bold green]✔ Walkthrough successfully completed! Rohit is fully equipped to begin farming with high profitability.[/bold green]")


if __name__ == "__main__":
    run_walkthrough()
