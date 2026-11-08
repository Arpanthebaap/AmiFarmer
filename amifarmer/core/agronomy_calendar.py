"""
AmiFarmer Precision Agronomy Roadmap and Crop Calendar Engine.
Generates an actionable, day-by-day 7-stage operational calendar from field preparation to post-harvest storage.
"""

from typing import Dict, Any, List, Optional


class AgronomyCalendar:
    """
    Constructs an end-to-end agronomic operations schedule calibrated to crop physiology.
    """

    STAGE_TEMPLATES = {
        "Cereal & Grain": [
            {
                "stage_number": 0,
                "stage_name": "Land Preparation & Basal Nutrition",
                "day_range": "Day -15 to Day 0",
                "key_operations": [
                    "Perform deep summer ploughing with disc or MB plough to expose soil pests and weed rhizomes to sunlight.",
                    "Apply 4-5 tons/acre well-rotted Farmyard Manure (FYM) or 1.5 tons vermicompost and incorporate with rotavator.",
                    "Apply 50% of recommended Nitrogen, 100% of Phosphorus, and 100% of Potassium as basal dose before final leveling.",
                    "Level the field with a laser land leveler to ensure uniform irrigation water distribution and avoid localized waterlogging."
                ]
            },
            {
                "stage_number": 1,
                "stage_name": "Seed Treatment & Sowing",
                "day_range": "Day 1 to Day 5",
                "key_operations": [
                    "Select certified, disease-resistant seed varieties from ICAR / State Seed Corporation.",
                    "Seed Treatment: Treat seeds with Trichoderma viride @ 5g/kg seed to prevent seed-borne and soil-borne fungal pathogens.",
                    "Bio-fertilizer Inoculation: Coat seeds with Azotobacter / Azospirillum and PSB culture @ 10g/kg; dry in shade for 30 minutes before sowing.",
                    "Sowing: Drill seeds at row-to-row spacing of 20-22 cm and depth of 4-5 cm using a zero-till seed drill or conventional planter."
                ]
            },
            {
                "stage_number": 2,
                "stage_name": "Early Vegetative & Crown Root Initiation (CRI)",
                "day_range": "Day 6 to Day 25",
                "key_operations": [
                    "Inspect field for uniform emergence (7-10 days after sowing); fill gaps if germination is patchy.",
                    "Crucial First Irrigation: Apply light irrigation at Crown Root Initiation (CRI) stage (Day 20-22 for wheat/grains). Never delay this irrigation.",
                    "Weed Management: Apply pre-emergence or early post-emergence selective herbicide or carry out manual weeding at 20-25 days."
                ]
            },
            {
                "stage_number": 3,
                "stage_name": "Tillering & Active Vegetative Growth",
                "day_range": "Day 26 to Day 55",
                "key_operations": [
                    "First Split Dose of Nitrogen: Top-dress remaining 25% of Nitrogen (Neem-coated urea @ 25-30 kg/acre) just before second irrigation.",
                    "Secondary Irrigation: Provide second irrigation at maximum tillering stage (Day 40-45).",
                    "Foliar Micronutrient Nutrition: Spray Zinc Sulphate (0.5%) + Urea (1%) if interveinal chlorosis is observed."
                ]
            },
            {
                "stage_number": 4,
                "stage_name": "Booting, Heading & Flowering",
                "day_range": "Day 56 to Day 85",
                "key_operations": [
                    "Critical Flowering Irrigation: Maintain adequate root zone moisture during booting and panicle emergence. Moisture stress here causes unfilled grains.",
                    "Final Split of Nitrogen: Top-dress balance 25% Nitrogen before heading.",
                    "Pest & Disease Scouting: Monitor for rust, smut, or armyworm. Deploy pheromone traps and light traps."
                ]
            },
            {
                "stage_number": 5,
                "stage_name": "Grain Filling & Dough Stage",
                "day_range": "Day 86 to Day 115",
                "key_operations": [
                    "Provide milk-stage / grain-filling irrigation during warm days to prevent premature grain shriveling.",
                    "Spray 00:00:50 (Potassium Sulphate @ 1%) to increase grain bold weight and test weight (1000-grain weight).",
                    "Stop All Irrigation 12-15 days before anticipated harvest to enable uniform crop drying and firm soil for harvesters."
                ]
            },
            {
                "stage_number": 6,
                "stage_name": "Harvesting, Threshing & Safe Storage",
                "day_range": "Day 116 to Day 135",
                "key_operations": [
                    "Harvest when grains become hard and moisture drops below 18-20% (golden yellow straw color).",
                    "Combine harvesting or manual reaping followed by mechanical thresher.",
                    "Sun-dry grains on clean tarpaulin until moisture is below 12% to prevent aflatoxin and storage weevils.",
                    "Store in hermetic bags (PICS bags) or clean bins treated with neem leaves or diatomaceous earth."
                ]
            }
        ],
        "Vegetable": [
            {
                "stage_number": 0,
                "stage_name": "Land Preparation, Raised Beds & Drip Layout",
                "day_range": "Day -20 to Day 0",
                "key_operations": [
                    "Deep ploughing and fine tilth preparation. Incorporate 6 tons/acre FYM or 2 tons vermicompost + 50 kg neem cake.",
                    "Prepare raised beds of 1 meter top width, 30 cm height, with 50 cm pathways for superior root aeration.",
                    "Lay inline drip lateral pipes (16mm, 40cm emitter spacing) along the center of raised beds.",
                    "Lay 25-micron silver-black plastic mulch sheet over the beds and punch planting holes at recommended spacing."
                ]
            },
            {
                "stage_number": 1,
                "stage_name": "Nursery Raising & Transplanting",
                "day_range": "Day 1 to Day 25",
                "key_operations": [
                    "Raise seedlings in 98-cell pro-trays using sterilized coco-peat + vermicompost + Trichoderma substrate in shade net.",
                    "Transplant healthy 22-25 day old seedlings during late afternoon to minimize transplanting shock.",
                    "Immediately give drip irrigation with humic acid (2 ml/L) to stimulate rapid lateral root establishment."
                ]
            },
            {
                "stage_number": 2,
                "stage_name": "Vegetative Establishment & Trellising",
                "day_range": "Day 26 to Day 45",
                "key_operations": [
                    "Fertigation: Inject 19:19:19 water-soluble fertilizer through Venturi @ 3 kg/acre twice a week.",
                    "Erect bamboo stakes or GI wire trellising with nylon twine for indeterminate varieties (tomato, capsicum, creeper cucurbits).",
                    "Prune auxiliary side shoots (suckers) up to 30 cm height to divert photosynthates to central shoot."
                ]
            },
            {
                "stage_number": 3,
                "stage_name": "Flowering & Fruit Setting",
                "day_range": "Day 46 to Day 70",
                "key_operations": [
                    "Shift fertigation to high-phosphorus 12:61:00 (Mono Ammonium Phosphate) @ 2.5 kg/acre to promote heavy flower blooming.",
                    "Foliar spray of Boron 20% (1g/L) + Calcium Nitrate (2g/L) to prevent flower drop and blossom-end rot.",
                    "Install yellow and blue sticky traps (20 per acre) to control whiteflies, thrips, and aphids vectoring viruses."
                ]
            },
            {
                "stage_number": 4,
                "stage_name": "Fruit Development & Sizing",
                "day_range": "Day 71 to Day 95",
                "key_operations": [
                    "Shift fertigation to 13:00:45 (Potassium Nitrate) @ 3.5 kg/acre to accelerate fruit sizing, firmness, and glossiness.",
                    "Maintain steady daily drip irrigation (2-3 hours early morning). Fluctuating moisture causes severe fruit cracking.",
                    "Spray neem oil 10,000 ppm (2 ml/L) preventively for caterpillar and borer control."
                ]
            },
            {
                "stage_number": 5,
                "stage_name": "Staggered Harvesting & Grading",
                "day_range": "Day 96 to Day 130",
                "key_operations": [
                    "Harvest early in the morning at the breaker/pink stage for long-distance transport, or red-ripe for local direct sales.",
                    "Use plastic crates instead of rough jute sacks to eliminate bruising and transit losses.",
                    "Sort into Grade-A (export / modern retail), Grade-B (wholesale mandi), and Grade-C (processing/sauce)."
                ]
            },
            {
                "stage_number": 6,
                "stage_name": "Post-Harvest Handling & Cold Chain",
                "day_range": "Post-Harvest",
                "key_operations": [
                    "Pre-cooling: Remove field heat immediately under shaded packhouse.",
                    "Store in solar cold room (8-12°C, 90% RH) to extend market shelf life from 3 days to 21 days.",
                    "Direct delivery to retail partners, restaurants, or local mandis."
                ]
            }
        ]
    }

    def generate_crop_roadmap(self, crop_name: str, category: str, growth_days: int) -> Dict[str, Any]:
        """
        Retrieves the tailored step-by-step roadmap for the crop category.
        """
        category_key = "Vegetable" if "Vegetable" in category or "Protected" in category or "Spice" in category else "Cereal & Grain"
        stages = self.STAGE_TEMPLATES.get(category_key, self.STAGE_TEMPLATES["Cereal & Grain"])

        return {
            "crop_name": crop_name,
            "category": category,
            "total_growth_duration_days": growth_days,
            "operational_stages": stages,
            "irrigation_philosophy": (
                "Drip fertigation with automated scheduling: deliver water and nutrients directly to root hairs daily."
                if category_key == "Vegetable"
                else "Critical stage flood/border irrigation: ensure zero moisture stress at Crown Root Initiation, Flowering, and Milk stages."
            ),
            "safety_guideline": "Adhere strictly to Pre-Harvest Intervals (PHI) on any applied crop protection chemicals to ensure zero toxic residues on produce."
        }
