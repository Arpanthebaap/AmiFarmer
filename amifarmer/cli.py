"""
AmiFarmer Interactive Terminal CLI & Precision Farm Diagnostic Wizard.
Built with Rich for beautiful terminal tables, status panels, and interactive consultation.
"""

import sys
import json
import argparse
from pathlib import Path

# Fix Windows console UTF-8 encoding
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

# Ensure package root is in sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt, FloatPrompt
from rich.text import Text

from amifarmer.core.full_farm_audit import FullFarmAuditor
from amifarmer.data import load_agro_climatic_zones

console = Console(force_terminal=True, legacy_windows=False)

BANNER = r"""
   ___           _ _____                                
  / _ \         (_)  ___|                               
 / /_\ \_ __ ___  _ \ `--.  ___ _ ____   _____ _ __     
 |  _  | '_ ` _ \| | `--. \/ _ \ '__\ \ / / _ \ '__|    
 | | | | | | | | | |/\__/ /  __/ |   \ V /  __/ |       
 \_| |_/_| |_| |_|_|\____/ \___|_|    \_/ \___|_|       
                                                        
 [bold green]Autonomous Multimodal Agricultural Intelligence Engine & Farm OS[/bold green]
 [bold cyan]Stanford / MIT Research Grade • ICAR & CGWB Calibrated • Zero-Knowledge Beginner Friendly[/bold cyan]
"""


def render_banner():
    console.print(Panel(BANNER, style="bold green", subtitle="v1.0.0 • Production Release"))


def run_interactive_wizard():
    render_banner()
    console.print("[bold yellow]🌾 Welcome to AmiFarmer Consultation Wizard![/bold yellow]")
    console.print("Even if you have [bold green]ZERO prior knowledge[/bold green] of farming, AmiFarmer will guide you from soil to wealth.\n")

    farmer_name = Prompt.ask("[cyan]Enter Farmer / Entrepreneur Name[/cyan]", default="Aarav Sharma")
    state = Prompt.ask("[cyan]Enter State (e.g. Maharashtra, Punjab, Uttar Pradesh, West Bengal, Karnataka)[/cyan]", default="Maharashtra")
    district = Prompt.ask("[cyan]Enter District (e.g. Nashik, Ludhiana, Varanasi, Hooghly, Belagavi)[/cyan]", default="Nashik")
    acres = FloatPrompt.ask("[cyan]Enter Farm Holding Area in Acres[/cyan]", default=3.0)

    console.print("\n[bold cyan]⚡ Running Autonomous Multi-Disciplinary Agro-Pedo-Hydrological Audit...[/bold cyan]")
    auditor = FullFarmAuditor()
    farm = auditor.create_beginner_profile(farmer_name=farmer_name, state=state, district=district, farm_area_acres=acres)
    audit_report = auditor.run_full_audit(farm)

    # 1. Executive Summary Panel
    console.print("\n")
    console.print(Panel(
        f"[bold white]{audit_report['executive_summary']}[/bold white]",
        title="📋 Executive Audit Dossier",
        style="bold green"
    ))

    # 2. Soil & Hydrology Table
    soil_res = audit_report["soil_analysis"]
    gw_res = audit_report["hydrology_and_water_security"]["groundwater_status"]
    pump_res = audit_report["hydrology_and_water_security"]["solar_pump_sizing"]

    env_table = Table(title="🌱 Soil & Hydrological Health Matrix", style="cyan")
    env_table.add_column("Parameter", style="bold yellow")
    env_table.add_column("Value / Status", style="white")
    env_table.add_column("Agronomic Implication / Action", style="green")

    env_table.add_row("Soil Texture", soil_res["texture"], "Defines infiltration & tillage requirement")
    env_table.add_row("Soil Health Score (SHS)", f"{soil_res['soil_health_score']}/100 ({soil_res['soil_health_grade']})", "Composite fertility index")
    env_table.add_row("Groundwater Depth", f"{gw_res['depth_mbgl']} mbgl", gw_res["status_title"])
    env_table.add_row("Water Table Sustainability", f"{gw_res['sustainability_score']}/100", f"Recharge ease: {gw_res['recharge_ease']}")
    env_table.add_row("Solar Pump Recommended", f"{pump_res['recommended_pump_hp']} HP ({pump_res['recommended_solar_pv_array_wp']} Wp Array)", f"Saves ₹{pump_res['annual_cost_savings_inr']:,}/yr diesel under PM-KUSUM")

    console.print(env_table)

    # 3. Top Crop Recommendations Table
    crop_table = Table(title="🏆 Top Pareto-Optimal Crop & Vegetable Recommendations", style="magenta")
    crop_table.add_column("Rank", style="bold yellow", justify="center")
    crop_table.add_column("Crop Name", style="bold white")
    crop_table.add_column("Category", style="cyan")
    crop_table.add_column("Suitability %", style="green", justify="center")
    crop_table.add_column("Expected Yield", style="white", justify="right")
    crop_table.add_column("Cost / Acre", style="red", justify="right")
    crop_table.add_column("Net Profit / Acre", style="bold green", justify="right")
    crop_table.add_column("Growth Days", style="yellow", justify="center")
    crop_table.add_column("Risk Level", style="magenta")

    for idx, c in enumerate(audit_report["top_crop_recommendations"], 1):
        crop_table.add_row(
            str(idx),
            f"{c['crop_name']} ({c['hindi_name']})",
            c["category"],
            f"{c['suitability_score_pct']}%",
            f"{c['expected_yield_quintals_per_acre']} Qtl",
            f"₹{c['cost_of_cultivation_per_acre_inr']:,}",
            f"₹{c['net_profit_per_acre_inr']:,}",
            f"{c['growth_cycle_days']} d",
            c["risk_level"]
        )

    console.print(crop_table)

    # 4. Government Subsidies Matched Table
    sub_res = audit_report["government_subsidies_and_schemes"]
    sub_table = Table(title=f"🏛️ Government Subsidies Unlocked ({sub_res['total_schemes_eligible']} Schemes, ₹{sub_res['total_potential_benefit_inr']:,} Benefit)", style="green")
    sub_table.add_column("Scheme", style="bold yellow")
    sub_table.add_column("Category", style="cyan")
    sub_table.add_column("Max Financial Benefit", style="bold green")
    sub_table.add_column("Official Portal", style="blue")

    for s in sub_res["matched_schemes"][:5]:
        sub_table.add_row(
            s["acronym"],
            s["category"],
            f"₹{s['estimated_benefit_inr']:,}",
            s["official_portal"]
        )

    console.print(sub_table)

    # 5. Agribusiness Incubator Highlight
    biz = audit_report["turnkey_agribusiness_dpr"]
    console.print("\n")
    console.print(Panel(
        f"[bold green]Enterprise:[/bold green] {biz['project_title']}\n"
        f"[bold yellow]CapEx:[/bold yellow] ₹{biz['capital_structure']['total_project_capex_inr']:,} | "
        f"[bold cyan]Govt Subsidy:[/bold cyan] ₹{biz['capital_structure']['government_capital_subsidy_inr']:,} | "
        f"[bold magenta]Promoter Equity:[/bold magenta] ₹{biz['capital_structure']['promoter_margin_money_inr']:,}\n"
        f"[bold green]Year 2 Net Profit:[/bold green] ₹{biz['three_year_cash_flow_projection'][1]['net_profit_inr']:,} | "
        f"[bold green]Payback Period:[/bold green] {biz['financial_viability_metrics']['payback_period_years']} years | "
        f"[bold green]IRR:[/bold green] {biz['financial_viability_metrics']['internal_rate_of_return_irr_pct']}%\n"
        f"[bold white]Required Licenses:[/bold white] {', '.join(biz['statutory_licenses_and_approvals'])}",
        title="💼 Turnkey Agribusiness DPR Opportunity",
        style="bold blue"
    ))

    # Export report prompt
    export = Prompt.ask("\n[cyan]Export complete 360° JSON report to file?[/cyan]", choices=["y", "n"], default="y")
    if export.lower() == "y":
        filename = f"farm_audit_{district.lower()}_{acres}acres.json"
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(audit_report, f, indent=2, ensure_ascii=False)
        console.print(f"[bold green]✔ Report successfully exported to {filename}[/bold green]\n")


def main():
    parser = argparse.ArgumentParser(description="AmiFarmer: Autonomous Multimodal Agricultural Intelligence Engine")
    parser.add_argument("--wizard", action="store_true", help="Launch interactive step-by-step diagnostic wizard")
    parser.add_argument("--state", type=str, help="State name")
    parser.add_argument("--district", type=str, help="District name")
    parser.add_argument("--acres", type=float, default=2.5, help="Farm size in acres")
    parser.add_argument("--export", type=str, help="File path to save JSON report")

    args = parser.parse_args()

    if args.wizard or (not args.state and not args.district):
        run_interactive_wizard()
    else:
        auditor = FullFarmAuditor()
        farm = auditor.create_beginner_profile(
            farmer_name="Farmer",
            state=args.state or "Uttar Pradesh",
            district=args.district or "Varanasi",
            farm_area_acres=args.acres
        )
        report = auditor.run_full_audit(farm)
        if args.export:
            with open(args.export, "w", encoding="utf-8") as f:
                json.dump(report, f, indent=2, ensure_ascii=False)
            print(f"Report written to {args.export}")
        else:
            print(json.dumps(report, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
