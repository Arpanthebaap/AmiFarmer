"""
AmiFarmer Agro-Pedology and Soil Health Analytics Engine.
Calculates Soil Health Score (SHS), physical hydraulic properties,
deficiencies, and precise chemical & organic amendment prescriptions.
"""

import math
from typing import Dict, Any, List, Optional
from amifarmer.models.farm_profile import SoilProfile, SoilNutrients, SoilTexture
from amifarmer.data import load_soil_benchmarks


class SoilAnalyzer:
    """
    Evaluates soil chemical, physical, and biological fertility indices.
    Calibrated against Indian Council of Agricultural Research (ICAR) benchmarks.
    """

    def __init__(self):
        self.benchmarks = load_soil_benchmarks()

    def calculate_soil_health_score(self, soil: SoilProfile) -> float:
        """
        Computes a non-linear Soil Health Score (SHS) in [0, 100].
        Weights:
        - pH optimality (25%)
        - Organic Carbon (25%)
        - Available N-P-K balance (30%)
        - Electrical Conductivity / Salinity (20%)
        """
        nutrients = soil.nutrients

        # 1. pH Score: Optimal range is 6.5 - 7.5. Penalize steep deviations.
        ph = nutrients.ph
        if 6.5 <= ph <= 7.5:
            ph_score = 100.0
        elif 5.5 <= ph < 6.5:
            ph_score = 100.0 - (6.5 - ph) * 35.0
        elif 7.5 < ph <= 8.5:
            ph_score = 100.0 - (ph - 7.5) * 30.0
        elif ph < 5.5:
            ph_score = max(10.0, 65.0 - (5.5 - ph) * 40.0)
        else:  # ph > 8.5 (Alkaline/Sodic)
            ph_score = max(10.0, 70.0 - (ph - 8.5) * 50.0)

        # 2. Organic Carbon % (Low <0.5, Medium 0.5-0.75, High >0.75)
        oc = nutrients.organic_carbon_pct
        if oc >= 0.8:
            oc_score = 100.0
        elif oc >= 0.5:
            oc_score = 70.0 + ((oc - 0.5) / 0.3) * 30.0
        else:
            oc_score = max(15.0, (oc / 0.5) * 70.0)

        # 3. Available N-P-K Balance
        # N (kg/ha): 280-560 is medium
        n_ratio = min(1.2, nutrients.nitrogen_kg_ha / 350.0)
        n_score = min(100.0, n_ratio * 90.0)

        # P2O5 (kg/ha): 10-25 is medium
        p_ratio = min(1.3, nutrients.phosphorus_kg_ha / 18.0)
        p_score = min(100.0, p_ratio * 90.0)

        # K2O (kg/ha): 110-280 is medium
        k_ratio = min(1.3, nutrients.potassium_kg_ha / 180.0)
        k_score = min(100.0, k_ratio * 90.0)

        npk_score = (n_score * 0.4) + (p_score * 0.3) + (k_score * 0.3)

        # 4. Electrical Conductivity (Salinity in dS/m): Normal < 1.0, Critical > 2.0
        ec = nutrients.electrical_conductivity_ds_m
        if ec <= 0.8:
            ec_score = 100.0
        elif ec <= 1.5:
            ec_score = 85.0 - ((ec - 0.8) / 0.7) * 25.0
        elif ec <= 3.0:
            ec_score = 60.0 - ((ec - 1.5) / 1.5) * 40.0
        else:
            ec_score = max(5.0, 20.0 - (ec - 3.0) * 10.0)

        total_shs = (ph_score * 0.25) + (oc_score * 0.25) + (npk_score * 0.30) + (ec_score * 0.20)
        return round(float(total_shs), 1)

    def analyze_soil(self, soil: SoilProfile) -> Dict[str, Any]:
        """
        Runs comprehensive diagnosis of the soil profile.
        """
        shs = self.calculate_soil_health_score(soil)
        texture_name = soil.texture.value if hasattr(soil.texture, "value") else str(soil.texture)
        benchmark = self.benchmarks.get(texture_name, self.benchmarks.get("Alluvial", {}))

        nutrients = soil.nutrients
        deficiencies = []
        strengths = []
        amendment_plan = []

        # N diagnosis
        if nutrients.nitrogen_kg_ha < 280.0:
            deficiencies.append(f"Available Nitrogen is LOW ({nutrients.nitrogen_kg_ha:.1f} kg/ha). Plant vegetative vigor and chlorophyll will be constrained.")
            amendment_plan.append("Incorporate green manuring with Dhaincha (Sesbania bispinosa) or apply 15-20 kg/acre top-dressed neem-coated urea in split doses.")
        else:
            strengths.append(f"Adequate Available Nitrogen ({nutrients.nitrogen_kg_ha:.1f} kg/ha).")

        # P diagnosis
        if nutrients.phosphorus_kg_ha < 12.0:
            deficiencies.append(f"Available Phosphorus is LOW ({nutrients.phosphorus_kg_ha:.1f} kg/ha). Root elongation and flowering will be inhibited.")
            amendment_plan.append("Apply Single Super Phosphate (SSP) @ 50 kg/acre along with Phosphate Solubilizing Bacteria (PSB) @ 2 kg/acre to unlock bound phosphorus.")
        else:
            strengths.append(f"Optimum Phosphorus reserve ({nutrients.phosphorus_kg_ha:.1f} kg/ha).")

        # K diagnosis
        if nutrients.potassium_kg_ha < 140.0:
            deficiencies.append(f"Available Potassium is LOW ({nutrients.potassium_kg_ha:.1f} kg/ha). Disease resistance and drought tolerance reduced.")
            amendment_plan.append("Apply Muriate of Potash (MOP) @ 25 kg/acre or wood ash/compost before sowing.")
        else:
            strengths.append(f"Adequate Potassium ({nutrients.potassium_kg_ha:.1f} kg/ha) providing high cell turgor and pest resilience.")

        # Organic carbon
        if nutrients.organic_carbon_pct < 0.5:
            deficiencies.append(f"Soil Organic Carbon is CRITICAL ({nutrients.organic_carbon_pct:.2f}%). Microbial biomass and water retention severely compromised.")
            amendment_plan.append("Mandatory application of Well-Decomposed Farmyard Manure (FYM) @ 4 tons/acre or Vermicompost @ 1.5 tons/acre. Do NOT burn crop residue.")
        elif nutrients.organic_carbon_pct >= 0.75:
            strengths.append(f"Excellent Soil Organic Carbon ({nutrients.organic_carbon_pct:.2f}%) promoting vibrant soil microbiological activity.")

        # pH & Salinity diagnostics
        if nutrients.ph > 8.0:
            # Gypsum requirement calculation
            excess_ph = nutrients.ph - 7.5
            gypsum_tons = round(min(5.0, max(1.0, excess_ph * 2.5)), 1)
            deficiencies.append(f"Alkaline/Sodic Soil (pH {nutrients.ph:.1f}). Calcium availability restricted, micronutrients precipitated.")
            amendment_plan.append(f"Apply Agricultural Grade Mineral Gypsum @ {gypsum_tons} tons/acre followed by standing irrigation and drainage flushing.")
        elif nutrients.ph < 6.0:
            deficiencies.append(f"Acidic Soil (pH {nutrients.ph:.1f}). Aluminum/Manganese toxicity risk; phosphorus gets fixed.")
            lime_kg = round((6.5 - nutrients.ph) * 400.0)
            amendment_plan.append(f"Broadcast Agricultural Lime (CaCO3) or Dolomite powder @ {lime_kg} kg/acre 3 weeks before sowing.")

        if nutrients.electrical_conductivity_ds_m > 1.8:
            deficiencies.append(f"High Salinity (EC {nutrients.electrical_conductivity_ds_m:.2f} dS/m). Causes osmotic drought stress on young roots.")
            amendment_plan.append("Provide sub-surface drainage channels and leach root zone with low-salinity canal water or monsoon flushing.")

        # Micronutrients
        if nutrients.zinc_ppm is not None and nutrients.zinc_ppm < 0.6:
            deficiencies.append(f"Deficient Zinc ({nutrients.zinc_ppm:.2f} ppm). Risk of Khaira disease in paddy and white bud in maize.")
            amendment_plan.append("Soil application of Zinc Sulphate Heptahydrate (ZnSO4 21%) @ 10 kg/acre.")

        if nutrients.boron_ppm is not None and nutrients.boron_ppm < 0.5:
            deficiencies.append(f"Deficient Boron ({nutrients.boron_ppm:.2f} ppm). Causes hollow heart in potato and fruit cracking in tomato.")
            amendment_plan.append("Foliar spray of Solubor (Borax 20%) @ 1g/L at flowering initiation.")

        # Soil rating
        if shs >= 80.0:
            rating = "Prime Fertility (Grade A)"
        elif shs >= 65.0:
            rating = "Good Agricultural Quality (Grade B)"
        elif shs >= 50.0:
            rating = "Moderate / Restrictive (Grade C)"
        else:
            rating = "Degraded / Reclamation Required (Grade D)"

        return {
            "soil_health_score": shs,
            "soil_health_grade": rating,
            "texture": texture_name,
            "physical_properties": {
                "bulk_density_g_cm3": benchmark.get("bulk_density_g_cm3", 1.4),
                "porosity_pct": benchmark.get("porosity_pct", 45.0),
                "available_water_capacity_mm_m": benchmark.get("available_water_capacity_mm_m", 140.0),
                "cation_exchange_capacity_meq_100g": benchmark.get("cation_exchange_capacity_meq_100g", 18.0)
            },
            "strengths": strengths,
            "deficiencies": deficiencies,
            "amendment_plan": amendment_plan,
            "benchmark_guidelines": benchmark.get("recommended_amendments", "")
        }
