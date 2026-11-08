"""
AmiFarmer Integrated Pest Management (IPM) and Plant Protection Engine.
Provides biological biocontrol protocols and emergency chemical therapeutics with Pre-Harvest Intervals (PHI).
"""

from typing import Dict, Any, List, Optional


class PlantProtection:
    """
    Diagnostic database for crop insect pests, viral/fungal pathogens,
    and eco-friendly Integrated Pest Management (IPM) measures.
    """

    PEST_DISEASE_REGISTRY = {
        "Wheat": [
            {
                "issue_name": "Yellow / Stripe Rust (Puccinia striiformis)",
                "type": "Fungal Disease",
                "symptoms": "Linear bright yellow stripes composed of urediniospores on leaf blades. Stunted tillering.",
                "organic_preventive": "Foliar spray of Sour Buttermilk (Chhachh 5%) + Cow Urine (5%) or Trichoderma harzianum @ 5g/L.",
                "chemical_curative": "Propiconazole 25% EC (Tilt) @ 1 ml/L of water at the first sign of yellow pustules.",
                "pre_harvest_interval_days": 30
            },
            {
                "issue_name": "Termites (Odontotermes obesus)",
                "type": "Insect Pest",
                "symptoms": "Wilting and drying of plants in patches; root system hollowed out with mud tunnels.",
                "organic_preventive": "Incorporate well-rotted neem cake @ 100 kg/acre into soil during land preparation. Irrigate with Beauveria bassiana.",
                "chemical_curative": "Seed treatment with Chlorpyrifos 20% EC @ 4 ml/kg seed, or drenching along irrigation channels.",
                "pre_harvest_interval_days": 45
            }
        ],
        "Basmati Rice": [
            {
                "issue_name": "Bacterial Leaf Blight (Xanthomonas oryzae)",
                "type": "Bacterial Disease",
                "symptoms": "Water-soaked lesions on leaf margins turning translucent, yellow, and finally bleaching white straw color.",
                "organic_preventive": "Foliar spray of Pseudomonas fluorescens @ 5g/L + avoid excessive nitrogen fertilizer application.",
                "chemical_curative": "Copper Oxychloride 50% WP @ 2.5 g/L + Streptocycline (plant antibiotic) @ 6g per 60 liters of water.",
                "pre_harvest_interval_days": 21
            },
            {
                "issue_name": "Yellow Stem Borer (Scirpophaga incertulas)",
                "type": "Insect Pest",
                "symptoms": "Dead heart at vegetative stage and white earhead (empty chaffy panicles) at reproductive stage.",
                "organic_preventive": "Install pheromone traps with lure @ 8 per acre. Release egg parasitoid Trichogramma japonicum @ 40,000/acre.",
                "chemical_curative": "Chlorantraniliprole 0.4% G (Ferterra) @ 4 kg/acre broadcast with sand in standing water.",
                "pre_harvest_interval_days": 28
            }
        ],
        "Tomato": [
            {
                "issue_name": "Tomato Leaf Curl Virus (ToLCV)",
                "type": "Viral Disease (Whitefly Transmitted)",
                "symptoms": "Severe stunting, upward curling and puckering of leaves, thickening of veins, complete flower drop.",
                "organic_preventive": "Erect 50-mesh nylon insect nets in nursery. Install yellow sticky traps (25/acre) to trap whitefly vectors. Spray Neem Oil 10,000 ppm (3 ml/L).",
                "chemical_curative": "Spray Diafenthiuron 50% WP @ 1.2 g/L or Spiromesifen 22.9% SC @ 1 ml/L to eradicate whitefly populations.",
                "pre_harvest_interval_days": 7
            },
            {
                "issue_name": "Early & Late Blight (Alternaria / Phytophthora)",
                "type": "Fungal Disease",
                "symptoms": "Target-board concentric rings (Early blight) or water-soaked dark brown blotches with white fungal mildew underneath (Late blight).",
                "organic_preventive": "Prevent soil splash by straw mulching. Foliar spray of Bordeaux mixture (1%) or Trichoderma viride.",
                "chemical_curative": "Cymoxanil 8% + Mancozeb 64% WP (Curzate) @ 2.5 g/L, or Azoxystrobin 23% SC @ 1 ml/L.",
                "pre_harvest_interval_days": 5
            }
        ],
        "Onion": [
            {
                "issue_name": "Onion Thrips (Thrips tabaci)",
                "type": "Insect Pest",
                "symptoms": "Silver specks, white blotches, and leaf tip drying due to sap sucking. Stunted bulb formation.",
                "organic_preventive": "Install blue sticky traps (20 per acre). Spray Lecanicillium lecanii (entomopathogenic fungus) @ 5g/L.",
                "chemical_curative": "Fipronil 5% SC @ 2 ml/L or Spinetoram 11.7% SC @ 0.8 ml/L with non-ionic surfactant/sticker.",
                "pre_harvest_interval_days": 10
            },
            {
                "issue_name": "Purple Blotch (Alternaria porri)",
                "type": "Fungal Disease",
                "symptoms": "Small, sunken, white lesions with purple centers that enlarge and girdle the tubular leaves.",
                "organic_preventive": "Seed bulb treatment with Trichoderma. Avoid overhead sprinkler irrigation during warm humid evenings.",
                "chemical_curative": "Tebuconazole 25.9% EC @ 1.5 ml/L or Difenoconazole 25% EC @ 1 ml/L.",
                "pre_harvest_interval_days": 15
            }
        ],
        "Chickpea (Gram / Chana)": [
            {
                "issue_name": "Gram Pod Borer (Helicoverpa armigera)",
                "type": "Caterpillar Pest",
                "symptoms": "Larvae bore round entry holes into developing green pods and feed on developing grain with body half inside.",
                "organic_preventive": "Install Helilure pheromone traps @ 5 per acre. Spray Helicoverpa NPV (HaNPV) @ 250 LE/ha or Bacillus thuringiensis (Bt) @ 2g/L.",
                "chemical_curative": "Emamectin Benzoate 5% SG @ 0.4 g/L or Indoxacarb 14.5% SC @ 1 ml/L.",
                "pre_harvest_interval_days": 14
            },
            {
                "issue_name": "Fusarium Wilt (Fusarium oxysporum f. sp. ciceris)",
                "type": "Soil-Borne Fungal Disease",
                "symptoms": "Sudden drooping and yellowing of foliage; vascular browning visible when stem is split longitudinally.",
                "organic_preventive": "Crop rotation with non-host crops (mustard, wheat). Seed treatment with Trichoderma viride @ 8g/kg seed.",
                "chemical_curative": "No chemical curative once systemic vascular wilt establishes. Deep rogueing and burn affected plants.",
                "pre_harvest_interval_days": 0
            }
        ]
    }

    def get_plant_protection_guide(self, crop_name: str) -> List[Dict[str, Any]]:
        """
        Retrieves the pest and disease diagnostic guide for a given crop.
        """
        for k, v in self.PEST_DISEASE_REGISTRY.items():
            if k.lower() in crop_name.lower() or crop_name.lower() in k.lower():
                return v

        # Default universal IPM protocol
        return [
            {
                "issue_name": "Sucking Pests (Aphids, Jassids, Whiteflies)",
                "type": "General Sucking Insect Complex",
                "symptoms": "Curling of tender leaves, honeydew excretion attracting sooty mold, vectoring viral diseases.",
                "organic_preventive": "Install 20 yellow sticky traps/acre. Spray pure cold-pressed Neem Oil 10,000 ppm @ 2-3 ml/L with liquid soap.",
                "chemical_curative": "Acetamiprid 20% SP @ 0.3 g/L or Thiamethoxam 25% WG @ 0.4 g/L.",
                "pre_harvest_interval_days": 14
            },
            {
                "issue_name": "Damping Off & Soil-Borne Root Rot (Pythium / Rhizoctonia)",
                "type": "Soil-Borne Fungal Complex",
                "symptoms": "Water-soaked collapse of seedling collars at soil line; seedling falling over.",
                "organic_preventive": "Drench nursery beds with Trichoderma harzianum @ 10g/L + ensure flawless drainage.",
                "chemical_curative": "Drenching with Metalaxyl 8% + Mancozeb 64% WP @ 2.5 g/L.",
                "pre_harvest_interval_days": 21
            }
        ]
