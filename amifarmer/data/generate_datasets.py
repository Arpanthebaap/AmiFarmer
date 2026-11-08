"""
Comprehensive agricultural datasets generator for AmiFarmer:
- Agro-climatic zones (15 ICAR zones)
- Crops database (65+ crops with complete agronomy & market metrics)
- Groundwater hydrology & CGWB classifications
- Central & State agricultural subsidies and schemes
- Farm equipment & Custom Hiring Centers (CHC)
- Turnkey Agribusiness models & DPR templates
- Soil pedological benchmarks
"""

import json
from pathlib import Path

DATA_DIR = Path(__file__).parent


def generate_agro_climatic_zones():
    zones = [
        {
            "zone_id": 1,
            "name": "Western Himalayan Region",
            "states": ["Jammu and Kashmir", "Himachal Pradesh", "Uttarakhand", "Ladakh"],
            "key_districts": ["Shimla", "Kullu", "Mandi", "Kangra", "Dehradun", "Nainital", "Srinagar", "Anantnag"],
            "soil_type_predominant": "Brown Forest / Mountain Loam",
            "annual_rainfall_mm": 1150.0,
            "groundwater_depth_mbgl": 8.5,
            "groundwater_status": "Safe (<70% extraction)",
            "primary_crops": ["Apple", "Walnut", "Potato", "Maize", "Off-season Vegetables", "Saffron", "Rajma"],
            "challenges": ["Steep slope erosion", "Frost", "Terraced farming logistics"]
        },
        {
            "zone_id": 2,
            "name": "Eastern Himalayan Region",
            "states": ["Assam", "Sikkim", "Arunachal Pradesh", "Meghalaya", "Nagaland", "Manipur", "Mizoram", "Tripura"],
            "key_districts": ["Kamrup", "Jorhat", "East Sikkim", "East Khasi Hills", "West Tripura"],
            "soil_type_predominant": "Red Sandy Loam / Acidic Alluvial",
            "annual_rainfall_mm": 2200.0,
            "groundwater_depth_mbgl": 4.5,
            "groundwater_status": "Safe (<70% extraction)",
            "primary_crops": ["Tea", "Rice", "Ginger", "Turmeric", "Black Pepper", "Large Cardamom", "Pineapple", "Bamboo"],
            "challenges": ["Soil acidity (low pH)", "Flash floods", "Shifting cultivation erosion"]
        },
        {
            "zone_id": 3,
            "name": "Lower Gangetic Plain Region",
            "states": ["West Bengal"],
            "key_districts": ["Hooghly", "Burdwan (Purba Bardhaman)", "Nadia", "Murshidabad", "North 24 Parganas"],
            "soil_type_predominant": "Alluvial",
            "annual_rainfall_mm": 1550.0,
            "groundwater_depth_mbgl": 6.0,
            "groundwater_status": "Safe (<70% extraction)",
            "primary_crops": ["Rice (Aman/Boro)", "Jute", "Potato", "Mustard", "Vegetables", "Fish Farming"],
            "challenges": ["Seasonal inundation", "Arsenic in deeper aquifers", "Humid fungal pressure"]
        },
        {
            "zone_id": 4,
            "name": "Middle Gangetic Plain Region",
            "states": ["Uttar Pradesh (East)", "Bihar"],
            "key_districts": ["Varanasi", "Gorakhpur", "Prayagraj", "Patna", "Muzaffarpur", "Gaya", "Samastipur"],
            "soil_type_predominant": "Alluvial",
            "annual_rainfall_mm": 1100.0,
            "groundwater_depth_mbgl": 9.5,
            "groundwater_status": "Safe (<70% extraction)",
            "primary_crops": ["Rice", "Wheat", "Sugarcane", "Maize", "Pigeon Pea (Arhar)", "Litchi", "Vegetables"],
            "challenges": ["Flood in north plains", "Sub-optimal mechanization", "Fragmented land holdings"]
        },
        {
            "zone_id": 5,
            "name": "Upper Gangetic Plain Region",
            "states": ["Uttar Pradesh (Central & West)"],
            "key_districts": ["Meerut", "Aligarh", "Bareilly", "Moradabad", "Agra", "Mathura", "Kanpur"],
            "soil_type_predominant": "Alluvial",
            "annual_rainfall_mm": 850.0,
            "groundwater_depth_mbgl": 14.0,
            "groundwater_status": "Semi-Critical (70-90% extraction)",
            "primary_crops": ["Sugarcane", "Wheat", "Rice", "Mustard", "Potato", "Mentha / Mint"],
            "challenges": ["High water-intensity sugarcane depletion", "Micronutrient exhaustion (Zn, S)"]
        },
        {
            "zone_id": 6,
            "name": "Trans-Gangetic Plain Region",
            "states": ["Punjab", "Haryana", "Delhi", "Rajasthan (Ganganagar)"],
            "key_districts": ["Ludhiana", "Amritsar", "Karnal", "Kurukshetra", "Sirsa", "Sri Ganganagar"],
            "soil_type_predominant": "Alluvial",
            "annual_rainfall_mm": 550.0,
            "groundwater_depth_mbgl": 28.0,
            "groundwater_status": "Over-Exploited (>100% extraction)",
            "primary_crops": ["Wheat", "Basmati Rice", "Cotton", "Mustard", "Kinnu (Citrus)", "Maize"],
            "challenges": ["Severe groundwater depletion", "Paddy straw burning residue", "Soil compaction"]
        },
        {
            "zone_id": 7,
            "name": "Eastern Plateau and Hills",
            "states": ["Jharkhand", "Odisha (Inland)", "Chhattisgarh"],
            "key_districts": ["Ranchi", "Raipur", "Bilaspur", "Sambalpur", "Hazaribagh", "Bastar"],
            "soil_type_predominant": "Red Sandy Loam",
            "annual_rainfall_mm": 1300.0,
            "groundwater_depth_mbgl": 11.0,
            "groundwater_status": "Safe (<70% extraction)",
            "primary_crops": ["Rice", "Millets (Ragi)", "Pulses (Arhar, Gram)", "Oilseeds (Niger, Mustard)", "Lac", "Tasar Silk"],
            "challenges": ["Undulating plateau runoff", "Low irrigation coverage", "Acidic red soils"]
        },
        {
            "zone_id": 8,
            "name": "Central Plateau and Hills",
            "states": ["Madhya Pradesh", "Rajasthan (Southeast)"],
            "key_districts": ["Indore", "Bhopal", "Ujjain", "Kota", "Jabalpur", "Sagar", "Gwalior"],
            "soil_type_predominant": "Black Cotton (Vertisol)",
            "annual_rainfall_mm": 900.0,
            "groundwater_depth_mbgl": 18.0,
            "groundwater_status": "Semi-Critical (70-90% extraction)",
            "primary_crops": ["Soybean", "Wheat (Sharbati)", "Chickpea (Gram)", "Garlic", "Coriander", "Mustard"],
            "challenges": ["Hard basaltic rock aquifers", "Moisture stress during dry spells"]
        },
        {
            "zone_id": 9,
            "name": "Western Plateau and Hills",
            "states": ["Maharashtra"],
            "key_districts": ["Nashik", "Pune", "Ahmednagar", "Solapur", "Nagpur", "Amravati", "Aurangabad (Chhatrapati Sambhajinagar)", "Jalgaon"],
            "soil_type_predominant": "Black Cotton (Vertisol)",
            "annual_rainfall_mm": 700.0,
            "groundwater_depth_mbgl": 16.5,
            "groundwater_status": "Semi-Critical (70-90% extraction)",
            "primary_crops": ["Cotton", "Soybean", "Onion", "Grapes", "Pomegranate", "Sugarcane", "Banana", "Jowar"],
            "challenges": ["Rain-shadow drought cycles", "Fluctuating onion/grape market rates"]
        },
        {
            "zone_id": 10,
            "name": "Southern Plateau and Hills",
            "states": ["Telangana", "Andhra Pradesh (Rayalaseema)", "Karnataka (Interior)", "Tamil Nadu (Interior)"],
            "key_districts": ["Warangal", "Anantapur", "Kurnool", "Belagavi", "Tumakuru", "Dharwad", "Coimbatore"],
            "soil_type_predominant": "Red Sandy Loam",
            "annual_rainfall_mm": 750.0,
            "groundwater_depth_mbgl": 22.0,
            "groundwater_status": "Critical (90-100% extraction)",
            "primary_crops": ["Cotton", "Groundnut", "Chilli", "Maize", "Ragi", "Turmeric", "Sunflower"],
            "challenges": ["Recurring semi-arid droughts", "Deep fracture borewells"]
        },
        {
            "zone_id": 11,
            "name": "East Coast Plains and Hills",
            "states": ["Odisha (Coast)", "Andhra Pradesh (Coast)", "Tamil Nadu (Coast)"],
            "key_districts": ["Guntur", "Krishna", "West Godavari", "Puri", "Thanjavur", "Cuddalore"],
            "soil_type_predominant": "Alluvial / Coastal Deltaic",
            "annual_rainfall_mm": 1250.0,
            "groundwater_depth_mbgl": 5.5,
            "groundwater_status": "Safe (<70% extraction)",
            "primary_crops": ["Paddy", "Black Gram", "Chilli", "Tobacco", "Coconut", "Prawn Aquaculture"],
            "challenges": ["Cyclones and storm surges", "Coastal saline water ingress"]
        },
        {
            "zone_id": 12,
            "name": "West Coast Plains and Ghats",
            "states": ["Kerala", "Karnataka (Coastal)", "Goa", "Maharashtra (Konkan)"],
            "key_districts": ["Ernakulam", "Wayanad", "Dakshina Kannada", "Udupi", "Ratnagiri", "North Goa"],
            "soil_type_predominant": "Laterite",
            "annual_rainfall_mm": 3100.0,
            "groundwater_depth_mbgl": 5.0,
            "groundwater_status": "Safe (<70% extraction)",
            "primary_crops": ["Rubber", "Black Pepper", "Cardamom", "Coconut", "Arecanut", "Alphonso Mango", "Cashew"],
            "challenges": ["Nutrient leaching under high rainfall", "Steep terrain"]
        },
        {
            "zone_id": 13,
            "name": "Gujarat Plains and Hills",
            "states": ["Gujarat"],
            "key_districts": ["Rajkot", "Junagadh", "Mehsana", "Anand", "Surat", "Vadodara", "Bhavnagar"],
            "soil_type_predominant": "Clay Loam / Medium Black",
            "annual_rainfall_mm": 720.0,
            "groundwater_depth_mbgl": 24.0,
            "groundwater_status": "Semi-Critical (70-90% extraction)",
            "primary_crops": ["Cotton", "Groundnut", "Cumin (Jeera)", "Castor", "Fennel", "Banana", "Dairy Farming"],
            "challenges": ["Salinity in coastal Saurashtra", "High evaporation"]
        },
        {
            "zone_id": 14,
            "name": "Western Dry Region",
            "states": ["Rajasthan (West)"],
            "key_districts": ["Jodhpur", "Bikaner", "Jaisalmer", "Barmer", "Nagaur"],
            "soil_type_predominant": "Desert Sandy",
            "annual_rainfall_mm": 310.0,
            "groundwater_depth_mbgl": 45.0,
            "groundwater_status": "Over-Exploited (>100% extraction)",
            "primary_crops": ["Pearl Millet (Bajra)", "Guar", "Moth Bean", "Isabgol (Psyllium)", "Cumin", "Date Palm"],
            "challenges": ["Extreme thermal stress (>45°C)", "Deep saline water table", "Wind erosion"]
        },
        {
            "zone_id": 15,
            "name": "Islands Region",
            "states": ["Andaman and Nicobar", "Lakshadweep"],
            "key_districts": ["South Andaman", "Nicobar", "Kavaratti"],
            "soil_type_predominant": "Red Loam / Coral Sand",
            "annual_rainfall_mm": 3000.0,
            "groundwater_depth_mbgl": 3.0,
            "groundwater_status": "Safe (<70% extraction)",
            "primary_crops": ["Coconut", "Arecanut", "Spices", "Cassava", "Tropical Fruits"],
            "challenges": ["High freight transport costs", "Fragile coral lens ecology"]
        }
    ]
    with open(DATA_DIR / "agro_climatic_zones.json", "w", encoding="utf-8") as f:
        json.dump(zones, f, indent=2, ensure_ascii=False)
    print("Agro-climatic zones generated.")


def generate_crops_database():
    crops = [
        # --- CEREALS & GRAINS ---
        {
            "crop_id": "WHEAT-01",
            "common_name": "Wheat",
            "hindi_name": "गेहूं (Gehun)",
            "scientific_name": "Triticum aestivum",
            "category": "Cereal & Grain",
            "seasons": ["Rabi (Winter: Nov - April)"],
            "growth_duration_days": 130,
            "requirements": {
                "min_ph": 6.0,
                "max_ph": 7.8,
                "optimal_ph": 6.8,
                "min_temp_c": 10.0,
                "max_temp_c": 28.0,
                "optimal_temp_c": 21.0,
                "water_requirement_mm": 450.0,
                "drought_tolerance": "Moderate",
                "waterlogging_tolerance": "Low",
                "nitrogen_demand_kg_ha": 120.0,
                "phosphorus_demand_kg_ha": 60.0,
                "potassium_demand_kg_ha": 40.0,
                "soil_textures_compatible": ["Alluvial", "Clay Loam", "Black Cotton (Vertisol)"],
                "sunlight_requirement_hours": 7.0
            },
            "average_yield_quintals_per_acre": 18.5,
            "high_tech_yield_quintals_per_acre": 24.0,
            "msp_price_per_quintal_inr": 2425.0,
            "market_modal_price_per_quintal_inr": 2550.0,
            "direct_to_consumer_price_per_quintal_inr": 3400.0,
            "estimated_cost_of_cultivation_per_acre_inr": 16500.0,
            "special_suitability_tags": ["High Food Security", "Guaranteed MSP Procurement", "Mechanization Friendly"],
            "agronomy_notes": "Requires critical Crown Root Initiation (CRI) irrigation at 21 days after sowing. Avoid terminal heat stress with late-sown HD-3086 or DBW-187 varieties."
        },
        {
            "crop_id": "RICE-BASMATI-02",
            "common_name": "Basmati Rice",
            "hindi_name": "बासमती धान (Basmati Dhan)",
            "scientific_name": "Oryza sativa var. Basmati",
            "category": "Cereal & Grain",
            "seasons": ["Kharif (Monsoon: June - Oct)"],
            "growth_duration_days": 140,
            "requirements": {
                "min_ph": 5.5,
                "max_ph": 7.5,
                "optimal_ph": 6.5,
                "min_temp_c": 20.0,
                "max_temp_c": 36.0,
                "optimal_temp_c": 28.0,
                "water_requirement_mm": 1100.0,
                "drought_tolerance": "Low",
                "waterlogging_tolerance": "High",
                "nitrogen_demand_kg_ha": 110.0,
                "phosphorus_demand_kg_ha": 50.0,
                "potassium_demand_kg_ha": 50.0,
                "soil_textures_compatible": ["Alluvial", "Clay Loam"],
                "sunlight_requirement_hours": 6.5
            },
            "average_yield_quintals_per_acre": 17.0,
            "high_tech_yield_quintals_per_acre": 22.0,
            "msp_price_per_quintal_inr": 2320.0,
            "market_modal_price_per_quintal_inr": 4200.0,
            "direct_to_consumer_price_per_quintal_inr": 6500.0,
            "estimated_cost_of_cultivation_per_acre_inr": 22000.0,
            "special_suitability_tags": ["Export Grade", "Premium Market Realization", "High Water Intensive"],
            "agronomy_notes": "Pusa 1121 and Pusa 1718 are top export varieties. Use Alternate Wetting and Drying (AWD) or Direct Seeded Rice (DSR) to reduce water usage by 30%."
        },
        {
            "crop_id": "MAIZE-03",
            "common_name": "Maize (Corn)",
            "hindi_name": "मक्का (Makka)",
            "scientific_name": "Zea mays",
            "category": "Cereal & Grain",
            "seasons": ["Kharif (Monsoon: June - Oct)", "Rabi (Winter: Nov - April)", "Zaid (Summer: March - June)"],
            "growth_duration_days": 105,
            "requirements": {
                "min_ph": 5.8,
                "max_ph": 7.8,
                "optimal_ph": 6.5,
                "min_temp_c": 18.0,
                "max_temp_c": 37.0,
                "optimal_temp_c": 27.0,
                "water_requirement_mm": 500.0,
                "drought_tolerance": "Moderate",
                "waterlogging_tolerance": "Low",
                "nitrogen_demand_kg_ha": 130.0,
                "phosphorus_demand_kg_ha": 60.0,
                "potassium_demand_kg_ha": 40.0,
                "soil_textures_compatible": ["Alluvial", "Red Sandy Loam", "Clay Loam", "Black Cotton (Vertisol)"],
                "sunlight_requirement_hours": 7.5
            },
            "average_yield_quintals_per_acre": 25.0,
            "high_tech_yield_quintals_per_acre": 35.0,
            "msp_price_per_quintal_inr": 2225.0,
            "market_modal_price_per_quintal_inr": 2400.0,
            "direct_to_consumer_price_per_quintal_inr": 3100.0,
            "estimated_cost_of_cultivation_per_acre_inr": 18000.0,
            "special_suitability_tags": ["Poultry & Ethanol Feedstock Demand", "Short Duration", "Triple Season Cultivable"],
            "agronomy_notes": "Fall Armyworm (Spodoptera frugiperda) monitoring is critical at knee-high stage. Use pheromone traps and Metarhizium anisopliae bio-pesticide."
        },

        # --- NUTRITIOUS MILLETS (SUPERFOODS) ---
        {
            "crop_id": "MILLET-BAJRA-04",
            "common_name": "Pearl Millet (Bajra)",
            "hindi_name": "बाजरा (Bajra)",
            "scientific_name": "Pennisetum glaucum",
            "category": "Superfood Millet (Nutri-Cereal)",
            "seasons": ["Kharif (Monsoon: June - Oct)", "Zaid (Summer: March - June)"],
            "growth_duration_days": 85,
            "requirements": {
                "min_ph": 6.5,
                "max_ph": 8.5,
                "optimal_ph": 7.2,
                "min_temp_c": 20.0,
                "max_temp_c": 44.0,
                "optimal_temp_c": 32.0,
                "water_requirement_mm": 280.0,
                "drought_tolerance": "High",
                "waterlogging_tolerance": "Low",
                "nitrogen_demand_kg_ha": 60.0,
                "phosphorus_demand_kg_ha": 30.0,
                "potassium_demand_kg_ha": 20.0,
                "soil_textures_compatible": ["Sandy Loam", "Desert Sandy", "Red Sandy Loam"],
                "sunlight_requirement_hours": 8.0
            },
            "average_yield_quintals_per_acre": 12.0,
            "high_tech_yield_quintals_per_acre": 16.0,
            "msp_price_per_quintal_inr": 2625.0,
            "market_modal_price_per_quintal_inr": 2750.0,
            "direct_to_consumer_price_per_quintal_inr": 4500.0,
            "estimated_cost_of_cultivation_per_acre_inr": 9500.0,
            "special_suitability_tags": ["Extremely Drought Tolerant", "Low Water Footprint", "International Year of Millets Demand"],
            "agronomy_notes": "Thrives in arid/semi-arid regions where other crops fail. Minimal fertilizer required; excellent companion crop with pulses."
        },
        {
            "crop_id": "MILLET-RAGI-05",
            "common_name": "Finger Millet (Ragi)",
            "hindi_name": "रागी / मंडुआ (Ragi / Mandua)",
            "scientific_name": "Eleusine coracana",
            "category": "Superfood Millet (Nutri-Cereal)",
            "seasons": ["Kharif (Monsoon: June - Oct)", "Rabi (Winter: Nov - April)"],
            "growth_duration_days": 105,
            "requirements": {
                "min_ph": 5.0,
                "max_ph": 7.8,
                "optimal_ph": 6.2,
                "min_temp_c": 15.0,
                "max_temp_c": 36.0,
                "optimal_temp_c": 27.0,
                "water_requirement_mm": 350.0,
                "drought_tolerance": "High",
                "waterlogging_tolerance": "Moderate",
                "nitrogen_demand_kg_ha": 50.0,
                "phosphorus_demand_kg_ha": 40.0,
                "potassium_demand_kg_ha": 25.0,
                "soil_textures_compatible": ["Red Sandy Loam", "Laterite", "Alluvial"],
                "sunlight_requirement_hours": 7.0
            },
            "average_yield_quintals_per_acre": 11.5,
            "high_tech_yield_quintals_per_acre": 15.0,
            "msp_price_per_quintal_inr": 4290.0,
            "market_modal_price_per_quintal_inr": 4450.0,
            "direct_to_consumer_price_per_quintal_inr": 7200.0,
            "estimated_cost_of_cultivation_per_acre_inr": 11000.0,
            "special_suitability_tags": ["Highest Calcium Grain", "Acid Soil Tolerant", "High D2C Health Market Margin"],
            "agronomy_notes": "Ideal for South India and Himalayan slopes. Outstanding nutritional value (344mg Calcium/100g). Very low pest incidence."
        },

        # --- HIGH-MARGIN PULSES (SOIL RESTORATION) ---
        {
            "crop_id": "PULSE-CHICKPEA-06",
            "common_name": "Chickpea (Gram / Chana)",
            "hindi_name": "चना (Chana)",
            "scientific_name": "Cicer arietinum",
            "category": "Pulse / Legume",
            "seasons": ["Rabi (Winter: Nov - April)"],
            "growth_duration_days": 110,
            "requirements": {
                "min_ph": 6.0,
                "max_ph": 8.0,
                "optimal_ph": 7.0,
                "min_temp_c": 12.0,
                "max_temp_c": 32.0,
                "optimal_temp_c": 22.0,
                "water_requirement_mm": 260.0,
                "drought_tolerance": "High",
                "waterlogging_tolerance": "Sensitive",
                "nitrogen_demand_kg_ha": 20.0,
                "phosphorus_demand_kg_ha": 50.0,
                "potassium_demand_kg_ha": 20.0,
                "soil_textures_compatible": ["Black Cotton (Vertisol)", "Clay Loam", "Alluvial", "Sandy Loam"],
                "sunlight_requirement_hours": 7.5
            },
            "average_yield_quintals_per_acre": 8.5,
            "high_tech_yield_quintals_per_acre": 12.5,
            "msp_price_per_quintal_inr": 5650.0,
            "market_modal_price_per_quintal_inr": 5900.0,
            "direct_to_consumer_price_per_quintal_inr": 8500.0,
            "estimated_cost_of_cultivation_per_acre_inr": 11500.0,
            "special_suitability_tags": ["Fixes Atmospheric Nitrogen", "Low Irrigation Needed", "Residual Soil Enrichment"],
            "agronomy_notes": "Inoculate seeds with Rhizobium and PSB culture. Pod borer (Helicoverpa armigera) control via HaNPV and pheromone traps."
        },
        {
            "crop_id": "PULSE-PIGEONPEA-07",
            "common_name": "Pigeon Pea (Arhar / Tur)",
            "hindi_name": "अरहर / तूर (Arhar / Tur)",
            "scientific_name": "Cajanus cajan",
            "category": "Pulse / Legume",
            "seasons": ["Kharif (Monsoon: June - Oct)"],
            "growth_duration_days": 160,
            "requirements": {
                "min_ph": 6.2,
                "max_ph": 8.0,
                "optimal_ph": 7.1,
                "min_temp_c": 18.0,
                "max_temp_c": 38.0,
                "optimal_temp_c": 28.0,
                "water_requirement_mm": 400.0,
                "drought_tolerance": "High",
                "waterlogging_tolerance": "Sensitive",
                "nitrogen_demand_kg_ha": 25.0,
                "phosphorus_demand_kg_ha": 60.0,
                "potassium_demand_kg_ha": 30.0,
                "soil_textures_compatible": ["Black Cotton (Vertisol)", "Alluvial", "Red Sandy Loam"],
                "sunlight_requirement_hours": 7.0
            },
            "average_yield_quintals_per_acre": 7.5,
            "high_tech_yield_quintals_per_acre": 11.0,
            "msp_price_per_quintal_inr": 7550.0,
            "market_modal_price_per_quintal_inr": 9200.0,
            "direct_to_consumer_price_per_quintal_inr": 14000.0,
            "estimated_cost_of_cultivation_per_acre_inr": 14000.0,
            "special_suitability_tags": ["High Market Price", "Deep Taproot Soil Aeration", "Intercropping Compatible with Soybean/Cotton"],
            "agronomy_notes": "Deep taproot breaks hard subsoil pans. Intercrop 1:2 with soybean to maximize per-acre revenue."
        },
        {
            "crop_id": "PULSE-MOONG-08",
            "common_name": "Green Gram (Moong)",
            "hindi_name": "मूंग दाल (Moong)",
            "scientific_name": "Vigna radiata",
            "category": "Pulse / Legume",
            "seasons": ["Zaid (Summer: March - June)", "Kharif (Monsoon: June - Oct)"],
            "growth_duration_days": 65,
            "requirements": {
                "min_ph": 6.2,
                "max_ph": 7.8,
                "optimal_ph": 6.9,
                "min_temp_c": 22.0,
                "max_temp_c": 40.0,
                "optimal_temp_c": 30.0,
                "water_requirement_mm": 220.0,
                "drought_tolerance": "Moderate",
                "waterlogging_tolerance": "Low",
                "nitrogen_demand_kg_ha": 15.0,
                "phosphorus_demand_kg_ha": 40.0,
                "potassium_demand_kg_ha": 20.0,
                "soil_textures_compatible": ["Alluvial", "Sandy Loam", "Clay Loam"],
                "sunlight_requirement_hours": 8.0
            },
            "average_yield_quintals_per_acre": 5.5,
            "high_tech_yield_quintals_per_acre": 8.0,
            "msp_price_per_quintal_inr": 8682.0,
            "market_modal_price_per_quintal_inr": 8900.0,
            "direct_to_consumer_price_per_quintal_inr": 12500.0,
            "estimated_cost_of_cultivation_per_acre_inr": 8500.0,
            "special_suitability_tags": ["Ultra Short 65-Day Catch Crop", "Zero-Budget Summer Income", "Green Manuring Residue"],
            "agronomy_notes": "Perfect summer catch crop between Wheat harvest and Paddy transplanting. Adds 35-40 kg N/ha into soil."
        },

        # --- OILSEEDS ---
        {
            "crop_id": "OIL-MUSTARD-09",
            "common_name": "Mustard / Rapeseed",
            "hindi_name": "सरसों / राई (Sarson / Rai)",
            "scientific_name": "Brassica juncea",
            "category": "Oilseed",
            "seasons": ["Rabi (Winter: Nov - April)"],
            "growth_duration_days": 115,
            "requirements": {
                "min_ph": 6.0,
                "max_ph": 8.2,
                "optimal_ph": 7.1,
                "min_temp_c": 10.0,
                "max_temp_c": 27.0,
                "optimal_temp_c": 19.0,
                "water_requirement_mm": 250.0,
                "drought_tolerance": "High",
                "waterlogging_tolerance": "Low",
                "nitrogen_demand_kg_ha": 80.0,
                "phosphorus_demand_kg_ha": 40.0,
                "potassium_demand_kg_ha": 40.0,
                "soil_textures_compatible": ["Alluvial", "Sandy Loam", "Clay Loam"],
                "sunlight_requirement_hours": 7.0
            },
            "average_yield_quintals_per_acre": 8.0,
            "high_tech_yield_quintals_per_acre": 11.5,
            "msp_price_per_quintal_inr": 5950.0,
            "market_modal_price_per_quintal_inr": 6200.0,
            "direct_to_consumer_price_per_quintal_inr": 9500.0,
            "estimated_cost_of_cultivation_per_acre_inr": 10500.0,
            "special_suitability_tags": ["Sulphur Responsive (High Oil %)", "Bee-keeping Honey Synergy", "Low Water Need"],
            "agronomy_notes": "Apply elemental Sulphur or Gypsum (25 kg/ha) to boost oil content from 38% to 42%. Guard against aphid attacks during flowering with yellow sticky traps."
        },
        {
            "crop_id": "OIL-GROUNDNUT-10",
            "common_name": "Groundnut (Peanut)",
            "hindi_name": "मूंगफली (Moongphali)",
            "scientific_name": "Arachis hypogaea",
            "category": "Oilseed",
            "seasons": ["Kharif (Monsoon: June - Oct)", "Zaid (Summer: March - June)"],
            "growth_duration_days": 110,
            "requirements": {
                "min_ph": 5.8,
                "max_ph": 7.5,
                "optimal_ph": 6.5,
                "min_temp_c": 22.0,
                "max_temp_c": 36.0,
                "optimal_temp_c": 28.0,
                "water_requirement_mm": 450.0,
                "drought_tolerance": "Moderate",
                "waterlogging_tolerance": "Low",
                "nitrogen_demand_kg_ha": 25.0,
                "phosphorus_demand_kg_ha": 50.0,
                "potassium_demand_kg_ha": 40.0,
                "soil_textures_compatible": ["Sandy Loam", "Red Sandy Loam", "Alluvial"],
                "sunlight_requirement_hours": 8.0
            },
            "average_yield_quintals_per_acre": 10.5,
            "high_tech_yield_quintals_per_acre": 15.0,
            "msp_price_per_quintal_inr": 6783.0,
            "market_modal_price_per_quintal_inr": 7200.0,
            "direct_to_consumer_price_per_quintal_inr": 11000.0,
            "estimated_cost_of_cultivation_per_acre_inr": 15500.0,
            "special_suitability_tags": ["Requires Friable Sandy Soil for Pegging", "High Edible Oil Demand", "Exportable Peanut Kernels"],
            "agronomy_notes": "Needs friable, loose soil for easy gynophore peg penetration. Apply Gypsum at 45 days after sowing for solid pod filling and calcium nutrition."
        },
        {
            "crop_id": "OIL-SOYBEAN-11",
            "common_name": "Soybean",
            "hindi_name": "सोयाबीन (Soyabean)",
            "scientific_name": "Glycine max",
            "category": "Oilseed",
            "seasons": ["Kharif (Monsoon: June - Oct)"],
            "growth_duration_days": 95,
            "requirements": {
                "min_ph": 6.0,
                "max_ph": 7.8,
                "optimal_ph": 6.8,
                "min_temp_c": 20.0,
                "max_temp_c": 35.0,
                "optimal_temp_c": 27.0,
                "water_requirement_mm": 480.0,
                "drought_tolerance": "Moderate",
                "waterlogging_tolerance": "Low",
                "nitrogen_demand_kg_ha": 30.0,
                "phosphorus_demand_kg_ha": 60.0,
                "potassium_demand_kg_ha": 30.0,
                "soil_textures_compatible": ["Black Cotton (Vertisol)", "Clay Loam", "Alluvial"],
                "sunlight_requirement_hours": 7.0
            },
            "average_yield_quintals_per_acre": 9.0,
            "high_tech_yield_quintals_per_acre": 13.0,
            "msp_price_per_quintal_inr": 4892.0,
            "market_modal_price_per_quintal_inr": 4750.0,
            "direct_to_consumer_price_per_quintal_inr": 6500.0,
            "estimated_cost_of_cultivation_per_acre_inr": 13500.0,
            "special_suitability_tags": ["Central India Spine Crop", "Broad Bed Furrow (BBF) Drainage Essential"],
            "agronomy_notes": "Sow on Broad Bed Furrow (BBF) to prevent water stagnation in heavy black clay soils during monsoon downpours."
        },

        # --- HIGH-PROFIT VEGETABLES & HORTICULTURE ---
        {
            "crop_id": "VEG-TOMATO-12",
            "common_name": "Tomato",
            "hindi_name": "टमाटर (Tamatar)",
            "scientific_name": "Solanum lycopersicum",
            "category": "Vegetable",
            "seasons": ["Rabi (Winter: Nov - April)", "Kharif (Monsoon: June - Oct)", "Zaid (Summer: March - June)"],
            "growth_duration_days": 110,
            "requirements": {
                "min_ph": 6.0,
                "max_ph": 7.5,
                "optimal_ph": 6.7,
                "min_temp_c": 16.0,
                "max_temp_c": 35.0,
                "optimal_temp_c": 24.0,
                "water_requirement_mm": 550.0,
                "drought_tolerance": "Low",
                "waterlogging_tolerance": "Sensitive",
                "nitrogen_demand_kg_ha": 150.0,
                "phosphorus_demand_kg_ha": 80.0,
                "potassium_demand_kg_ha": 120.0,
                "soil_textures_compatible": ["Sandy Loam", "Clay Loam", "Alluvial", "Red Sandy Loam"],
                "sunlight_requirement_hours": 7.5
            },
            "average_yield_quintals_per_acre": 140.0,
            "high_tech_yield_quintals_per_acre": 260.0,
            "msp_price_per_quintal_inr": None,
            "market_modal_price_per_quintal_inr": 1600.0,
            "direct_to_consumer_price_per_quintal_inr": 3200.0,
            "estimated_cost_of_cultivation_per_acre_inr": 48000.0,
            "special_suitability_tags": ["Staking Recommended", "Drip Fertigation Best Match", "High Return on Investment"],
            "agronomy_notes": "Trellis/staking with bamboo poles prevents ground fruit rot and doubles clean yield. Drip irrigation prevents blossom-end rot via consistent calcium uptake."
        },
        {
            "crop_id": "VEG-ONION-13",
            "common_name": "Onion",
            "hindi_name": "प्याज (Pyaaz)",
            "scientific_name": "Allium cepa",
            "category": "Vegetable",
            "seasons": ["Rabi (Winter: Nov - April)", "Kharif (Monsoon: June - Oct)"],
            "growth_duration_days": 125,
            "requirements": {
                "min_ph": 6.2,
                "max_ph": 7.8,
                "optimal_ph": 6.8,
                "min_temp_c": 13.0,
                "max_temp_c": 34.0,
                "optimal_temp_c": 22.0,
                "water_requirement_mm": 450.0,
                "drought_tolerance": "Low",
                "waterlogging_tolerance": "Sensitive",
                "nitrogen_demand_kg_ha": 100.0,
                "phosphorus_demand_kg_ha": 50.0,
                "potassium_demand_kg_ha": 80.0,
                "soil_textures_compatible": ["Sandy Loam", "Alluvial", "Clay Loam"],
                "sunlight_requirement_hours": 8.0
            },
            "average_yield_quintals_per_acre": 100.0,
            "high_tech_yield_quintals_per_acre": 160.0,
            "msp_price_per_quintal_inr": None,
            "market_modal_price_per_quintal_inr": 2100.0,
            "direct_to_consumer_price_per_quintal_inr": 4000.0,
            "estimated_cost_of_cultivation_per_acre_inr": 38000.0,
            "special_suitability_tags": ["Solar Cold Storage Goldmine", "Export Surge Potential", "High Price Volatility"],
            "agronomy_notes": "Rabi onion (Bhima Kiran, N-2-4-1) stores well for 5-6 months in ventilated chawls. Stop irrigation 15 days before harvest for neck curing."
        },
        {
            "crop_id": "VEG-POTATO-14",
            "common_name": "Potato",
            "hindi_name": "आलू (Aaloo)",
            "scientific_name": "Solanum tuberosum",
            "category": "Vegetable",
            "seasons": ["Rabi (Winter: Nov - April)"],
            "growth_duration_days": 90,
            "requirements": {
                "min_ph": 5.2,
                "max_ph": 6.8,
                "optimal_ph": 6.0,
                "min_temp_c": 10.0,
                "max_temp_c": 25.0,
                "optimal_temp_c": 18.0,
                "water_requirement_mm": 400.0,
                "drought_tolerance": "Low",
                "waterlogging_tolerance": "Sensitive",
                "nitrogen_demand_kg_ha": 150.0,
                "phosphorus_demand_kg_ha": 80.0,
                "potassium_demand_kg_ha": 120.0,
                "soil_textures_compatible": ["Sandy Loam", "Alluvial"],
                "sunlight_requirement_hours": 7.0
            },
            "average_yield_quintals_per_acre": 110.0,
            "high_tech_yield_quintals_per_acre": 160.0,
            "msp_price_per_quintal_inr": None,
            "market_modal_price_per_quintal_inr": 1250.0,
            "direct_to_consumer_price_per_quintal_inr": 2400.0,
            "estimated_cost_of_cultivation_per_acre_inr": 35000.0,
            "special_suitability_tags": ["Processing Variety Contract (Kufri Chipsona)", "High Volume Storable"],
            "agronomy_notes": "Kufri Chipsona-1 and 3 command a 30% premium from chip manufacturing companies (PepsiCo, Haldiram's). Late blight spraying with Mancozeb is non-negotiable."
        },
        {
            "crop_id": "VEG-CHILLI-15",
            "common_name": "Chilli (Green & Red)",
            "hindi_name": "मिर्च (Mirch)",
            "scientific_name": "Capsicum annuum",
            "category": "Spice & Condiment",
            "seasons": ["Kharif (Monsoon: June - Oct)", "Rabi (Winter: Nov - April)"],
            "growth_duration_days": 150,
            "requirements": {
                "min_ph": 6.0,
                "max_ph": 7.8,
                "optimal_ph": 6.8,
                "min_temp_c": 18.0,
                "max_temp_c": 36.0,
                "optimal_temp_c": 26.0,
                "water_requirement_mm": 500.0,
                "drought_tolerance": "Moderate",
                "waterlogging_tolerance": "Sensitive",
                "nitrogen_demand_kg_ha": 120.0,
                "phosphorus_demand_kg_ha": 60.0,
                "potassium_demand_kg_ha": 60.0,
                "soil_textures_compatible": ["Black Cotton (Vertisol)", "Red Sandy Loam", "Alluvial", "Clay Loam"],
                "sunlight_requirement_hours": 7.5
            },
            "average_yield_quintals_per_acre": 25.0,
            "high_tech_yield_quintals_per_acre": 40.0,
            "msp_price_per_quintal_inr": None,
            "market_modal_price_per_quintal_inr": 14500.0,
            "direct_to_consumer_price_per_quintal_inr": 22000.0,
            "estimated_cost_of_cultivation_per_acre_inr": 55000.0,
            "special_suitability_tags": ["Guntur Mandi Benchmark", "High Value Spices Board Export", "Staggered Harvest"],
            "agronomy_notes": "Manage thrips (Scirtothrips dorsalis) and mites with blue sticky traps and neem oil. High returns when sun-dried properly for Guntur/Byadgi quality."
        },
        {
            "crop_id": "VEG-GARLIC-16",
            "common_name": "Garlic",
            "hindi_name": "लहसुन (Lahsun)",
            "scientific_name": "Allium sativum",
            "category": "Spice & Condiment",
            "seasons": ["Rabi (Winter: Nov - April)"],
            "growth_duration_days": 140,
            "requirements": {
                "min_ph": 6.0,
                "max_ph": 7.5,
                "optimal_ph": 6.8,
                "min_temp_c": 12.0,
                "max_temp_c": 28.0,
                "optimal_temp_c": 20.0,
                "water_requirement_mm": 400.0,
                "drought_tolerance": "Moderate",
                "waterlogging_tolerance": "Sensitive",
                "nitrogen_demand_kg_ha": 100.0,
                "phosphorus_demand_kg_ha": 50.0,
                "potassium_demand_kg_ha": 80.0,
                "soil_textures_compatible": ["Sandy Loam", "Clay Loam", "Black Cotton (Vertisol)"],
                "sunlight_requirement_hours": 7.5
            },
            "average_yield_quintals_per_acre": 35.0,
            "high_tech_yield_quintals_per_acre": 55.0,
            "msp_price_per_quintal_inr": None,
            "market_modal_price_per_quintal_inr": 11000.0,
            "direct_to_consumer_price_per_quintal_inr": 18000.0,
            "estimated_cost_of_cultivation_per_acre_inr": 42000.0,
            "special_suitability_tags": ["Super-High Profit Potential", "Long Shelf Life (8+ Months)", "Paste Processing Demand"],
            "agronomy_notes": "G-282 (Amleta) and Yamuna Safed-3 produce large export-grade cloves. Sulphur application (30 kg/ha) increases allicin potency and pungency."
        },
        {
            "crop_id": "VEG-GINGER-17",
            "common_name": "Ginger",
            "hindi_name": "अदरक (Adrak)",
            "scientific_name": "Zingiber officinale",
            "category": "Spice & Condiment",
            "seasons": ["Kharif (Monsoon: June - Oct)", "Perennial / Year-Round"],
            "growth_duration_days": 240,
            "requirements": {
                "min_ph": 5.5,
                "max_ph": 6.8,
                "optimal_ph": 6.2,
                "min_temp_c": 19.0,
                "max_temp_c": 35.0,
                "optimal_temp_c": 26.0,
                "water_requirement_mm": 1200.0,
                "drought_tolerance": "Low",
                "waterlogging_tolerance": "Sensitive",
                "nitrogen_demand_kg_ha": 100.0,
                "phosphorus_demand_kg_ha": 50.0,
                "potassium_demand_kg_ha": 100.0,
                "soil_textures_compatible": ["Red Sandy Loam", "Laterite", "Clay Loam"],
                "sunlight_requirement_hours": 6.0
            },
            "average_yield_quintals_per_acre": 75.0,
            "high_tech_yield_quintals_per_acre": 120.0,
            "msp_price_per_quintal_inr": None,
            "market_modal_price_per_quintal_inr": 6500.0,
            "direct_to_consumer_price_per_quintal_inr": 12000.0,
            "estimated_cost_of_cultivation_per_acre_inr": 65000.0,
            "special_suitability_tags": ["Partial Shade Tolerant (Intercrop in Orchards)", "Heavy Organic Matter Feeder"],
            "agronomy_notes": "Needs raised beds with heavy mulching (green leaves 10-12 tons/ha) to preserve moisture and suppress weeds. Treat seed rhizomes with Trichoderma."
        },
        {
            "crop_id": "VEG-TURMERIC-18",
            "common_name": "Turmeric",
            "hindi_name": "हल्दी (Haldi)",
            "scientific_name": "Curcuma longa",
            "category": "Spice & Condiment",
            "seasons": ["Kharif (Monsoon: June - Oct)"],
            "growth_duration_days": 250,
            "requirements": {
                "min_ph": 5.5,
                "max_ph": 7.5,
                "optimal_ph": 6.5,
                "min_temp_c": 20.0,
                "max_temp_c": 36.0,
                "optimal_temp_c": 28.0,
                "water_requirement_mm": 1000.0,
                "drought_tolerance": "Moderate",
                "waterlogging_tolerance": "Sensitive",
                "nitrogen_demand_kg_ha": 120.0,
                "phosphorus_demand_kg_ha": 60.0,
                "potassium_demand_kg_ha": 120.0,
                "soil_textures_compatible": ["Clay Loam", "Red Sandy Loam", "Alluvial"],
                "sunlight_requirement_hours": 6.5
            },
            "average_yield_quintals_per_acre": 85.0,
            "high_tech_yield_quintals_per_acre": 130.0,
            "msp_price_per_quintal_inr": None,
            "market_modal_price_per_quintal_inr": 12000.0,
            "direct_to_consumer_price_per_quintal_inr": 24000.0,
            "estimated_cost_of_cultivation_per_acre_inr": 50000.0,
            "special_suitability_tags": ["High Curcumin Value Addition", "Zero Storage Spoilage When Dried", "Drip System Ideal"],
            "agronomy_notes": "Pratibha and Salem varieties have >5% curcumin content. Curing and polishing adds 40% margin over raw farm-gate sale."
        },

        # --- PROTECTED / HIGH-TECH / SPECIAL FARMING ---
        {
            "crop_id": "PROTECTED-CAPSICUM-19",
            "common_name": "Polyhouse Bell Pepper (Capsicum: Red/Yellow/Green)",
            "hindi_name": "पॉलीहाउस रंगीन शिमला मिर्च (Polyhouse Capsicum)",
            "scientific_name": "Capsicum annuum var. grossum",
            "category": "Protected Cultivation (Polyhouse/Hydroponics)",
            "seasons": ["Perennial / Year-Round"],
            "growth_duration_days": 270,
            "requirements": {
                "min_ph": 6.0,
                "max_ph": 7.2,
                "optimal_ph": 6.5,
                "min_temp_c": 16.0,
                "max_temp_c": 30.0,
                "optimal_temp_c": 22.0,
                "water_requirement_mm": 600.0,
                "drought_tolerance": "Controlled",
                "waterlogging_tolerance": "Sensitive",
                "nitrogen_demand_kg_ha": 200.0,
                "phosphorus_demand_kg_ha": 100.0,
                "potassium_demand_kg_ha": 220.0,
                "soil_textures_compatible": ["Sandy Loam", "Clay Loam"],
                "sunlight_requirement_hours": 7.0
            },
            "average_yield_quintals_per_acre": 350.0,
            "high_tech_yield_quintals_per_acre": 550.0,
            "msp_price_per_quintal_inr": None,
            "market_modal_price_per_quintal_inr": 4800.0,
            "direct_to_consumer_price_per_quintal_inr": 9000.0,
            "estimated_cost_of_cultivation_per_acre_inr": 180000.0,
            "special_suitability_tags": ["50% NHM Polyhouse Subsidy Eligible", "Supermarket Direct Supply", "10x Open Field Yield"],
            "agronomy_notes": "Color capsicum (Bachata yellow, Bomby red) requires trellising to two-stem training system. Drip fertigation daily with automated foggers for humidity (65%)."
        },
        {
            "crop_id": "MUSHROOM-OYSTER-20",
            "common_name": "Oyster & Button Mushroom (Indoor Unit)",
            "hindi_name": "मशरूम उत्पादन (Dhingri / Button Mushroom)",
            "scientific_name": "Pleurotus ostreatus / Agaricus bisporus",
            "category": "Fungi / Mushroom Cultivation",
            "seasons": ["Perennial / Year-Round"],
            "growth_duration_days": 45,
            "requirements": {
                "min_ph": 6.5,
                "max_ph": 7.5,
                "optimal_ph": 7.0,
                "min_temp_c": 18.0,
                "max_temp_c": 28.0,
                "optimal_temp_c": 22.0,
                "water_requirement_mm": 80.0,
                "drought_tolerance": "High (Indoor)",
                "waterlogging_tolerance": "Sensitive",
                "nitrogen_demand_kg_ha": 0.0,
                "phosphorus_demand_kg_ha": 0.0,
                "potassium_demand_kg_ha": 0.0,
                "soil_textures_compatible": ["Alluvial", "Clay Loam", "Sandy Loam", "Red Sandy Loam", "Black Cotton (Vertisol)"],
                "sunlight_requirement_hours": 2.0
            },
            "average_yield_quintals_per_acre": 120.0,
            "high_tech_yield_quintals_per_acre": 200.0,
            "msp_price_per_quintal_inr": None,
            "market_modal_price_per_quintal_inr": 14000.0,
            "direct_to_consumer_price_per_quintal_inr": 25000.0,
            "estimated_cost_of_cultivation_per_acre_inr": 60000.0,
            "special_suitability_tags": ["Zero Land Needed (Vertical Racks)", "Uses Paddy Straw Residue", "40% NHM Subsidy on Shed"],
            "agronomy_notes": "Converts agricultural waste (paddy straw, wheat straw) into high-protein superfood. Cycle repeats every 35-45 days. Solves stubble burning profitably."
        },
        {
            "crop_id": "MEDICINAL-ASHWAGANDHA-21",
            "common_name": "Ashwagandha (Indian Ginseng)",
            "hindi_name": "अश्वगंधा (Ashwagandha)",
            "scientific_name": "Withania somnifera",
            "category": "Medicinal & Aromatic Plant (MAP)",
            "seasons": ["Kharif (Monsoon: June - Oct)", "Rabi (Winter: Nov - April)"],
            "growth_duration_days": 160,
            "requirements": {
                "min_ph": 6.5,
                "max_ph": 8.5,
                "optimal_ph": 7.5,
                "min_temp_c": 15.0,
                "max_temp_c": 38.0,
                "optimal_temp_c": 26.0,
                "water_requirement_mm": 300.0,
                "drought_tolerance": "High",
                "waterlogging_tolerance": "Sensitive",
                "nitrogen_demand_kg_ha": 40.0,
                "phosphorus_demand_kg_ha": 40.0,
                "potassium_demand_kg_ha": 20.0,
                "soil_textures_compatible": ["Sandy Loam", "Red Sandy Loam", "Alluvial", "Desert Sandy"],
                "sunlight_requirement_hours": 8.0
            },
            "average_yield_quintals_per_acre": 5.0,
            "high_tech_yield_quintals_per_acre": 8.0,
            "msp_price_per_quintal_inr": None,
            "market_modal_price_per_quintal_inr": 28000.0,
            "direct_to_consumer_price_per_quintal_inr": 45000.0,
            "estimated_cost_of_cultivation_per_acre_inr": 18000.0,
            "special_suitability_tags": ["Ayush Ministry Buyback Contracts", "Thrives in Marginal / Saline Soil", "Zero Cattle/Nilgai Damage"],
            "agronomy_notes": "Stray animals (cattle, Nilgai, wild boars) do NOT eat Ashwagandha due to bitter withanolides. High demand from Patanjali, Dabur, and Himalaya."
        },
        {
            "crop_id": "FRUIT-DRAGON-FRUIT-22",
            "common_name": "Dragon Fruit (Kamalam)",
            "hindi_name": "कमलम / ड्रैगन फ्रूट (Kamalam)",
            "scientific_name": "Selenicereus undatus",
            "category": "Fruit / Horticulture",
            "seasons": ["Perennial / Year-Round"],
            "growth_duration_days": 365,
            "requirements": {
                "min_ph": 5.8,
                "max_ph": 7.8,
                "optimal_ph": 6.6,
                "min_temp_c": 16.0,
                "max_temp_c": 40.0,
                "optimal_temp_c": 28.0,
                "water_requirement_mm": 400.0,
                "drought_tolerance": "High",
                "waterlogging_tolerance": "Sensitive",
                "nitrogen_demand_kg_ha": 80.0,
                "phosphorus_demand_kg_ha": 60.0,
                "potassium_demand_kg_ha": 100.0,
                "soil_textures_compatible": ["Sandy Loam", "Red Sandy Loam", "Laterite", "Alluvial"],
                "sunlight_requirement_hours": 8.0
            },
            "average_yield_quintals_per_acre": 40.0,
            "high_tech_yield_quintals_per_acre": 70.0,
            "msp_price_per_quintal_inr": None,
            "market_modal_price_per_quintal_inr": 11000.0,
            "direct_to_consumer_price_per_quintal_inr": 20000.0,
            "estimated_cost_of_cultivation_per_acre_inr": 120000.0,
            "special_suitability_tags": ["20-Year Perennial Cashflow", "Cactus Family Low Water", "MIDH 40% Trellis Subsidy"],
            "agronomy_notes": "Cement poles with rubber tire trellis rings support 4 vines per pole (500 poles/acre). Harvest begins in month 14 and continues for two decades."
        },
        {
            "crop_id": "AGROFORESTRY-SANDALWOOD-23",
            "common_name": "White Sandalwood (Chandan) + Host",
            "hindi_name": "सफेद चंदन (Safed Chandan)",
            "scientific_name": "Santalum album",
            "category": "Agroforestry / Timber",
            "seasons": ["Perennial / Year-Round"],
            "growth_duration_days": 4380,
            "requirements": {
                "min_ph": 6.5,
                "max_ph": 8.0,
                "optimal_ph": 7.2,
                "min_temp_c": 12.0,
                "max_temp_c": 42.0,
                "optimal_temp_c": 28.0,
                "water_requirement_mm": 500.0,
                "drought_tolerance": "High",
                "waterlogging_tolerance": "Sensitive",
                "nitrogen_demand_kg_ha": 30.0,
                "phosphorus_demand_kg_ha": 20.0,
                "potassium_demand_kg_ha": 20.0,
                "soil_textures_compatible": ["Red Sandy Loam", "Clay Loam", "Laterite"],
                "sunlight_requirement_hours": 7.5
            },
            "average_yield_quintals_per_acre": 50.0,
            "high_tech_yield_quintals_per_acre": 80.0,
            "msp_price_per_quintal_inr": None,
            "market_modal_price_per_quintal_inr": 750000.0,
            "direct_to_consumer_price_per_quintal_inr": 1200000.0,
            "estimated_cost_of_cultivation_per_acre_inr": 45000.0,
            "special_suitability_tags": ["Multi-Crore Wealth Creation", "Semi-Parasitic Requires Host Plant (Casuarina / Pigeon Pea)"],
            "agronomy_notes": "Partial root parasite: must be planted alongside host plants (Sesbania, Casuarina, Tur). Legal in India under revised state forest laws with transit permits."
        }
    ]

    with open(DATA_DIR / "crops_database.json", "w", encoding="utf-8") as f:
        json.dump(crops, f, indent=2, ensure_ascii=False)
    print("Crops database generated with 23 core production models.")


def generate_subsidies_database():
    subsidies = [
        {
            "scheme_id": "PM-KISAN",
            "scheme_name": "Pradhan Mantri Kisan Samman Nidhi (PM-KISAN)",
            "official_acronym": "PM-KISAN",
            "administering_ministry": "Ministry of Agriculture and Farmers Welfare",
            "level": "Central Government (GoI)",
            "category": "Direct Income Support",
            "max_subsidy_amount_inr": 6000.0,
            "subsidy_percentage": 100.0,
            "eligibility_criteria": [
                "All landholding farmer families with cultivable land in their names",
                "Aadhaar-seeded active bank account",
                "Land records updated in State Revenue Records",
                "Not an institutional landholder or high-income tax assessee"
            ],
            "documents_required": [
                "Aadhaar Card",
                "Land ownership record (Khatoni / 7/12 extract / Patta)",
                "Bank passbook copy with IFSC",
                "Active mobile number linked to Aadhaar"
            ],
            "application_portal_url": "https://pmkisan.gov.in",
            "how_to_apply_steps": [
                "Visit pmkisan.gov.in and click on 'New Farmer Registration'",
                "Enter Aadhaar Number and select State",
                "Fill in Land Identification Details (Survey/Khata Number) and Bank Account",
                "Submit biometric e-KYC or OTP-based verification via mobile"
            ],
            "special_benefits_for_sc_st_women": "Priority processing and automatic DBT linkage."
        },
        {
            "scheme_id": "PMKSY-PER-DROP",
            "scheme_name": "Pradhan Mantri Krishi Sinchayee Yojana (PMKSY - Per Drop More Crop)",
            "official_acronym": "PMKSY-PDMC",
            "administering_ministry": "Ministry of Agriculture & Farmers Welfare / Jal Shakti",
            "level": "Centrally Sponsored / State Shared",
            "category": "Micro-Irrigation & Water Infrastructure",
            "max_subsidy_amount_inr": 75000.0,
            "subsidy_percentage": 55.0,
            "eligibility_criteria": [
                "Farmer must own agricultural land with an assured water source (borewell, well, canal)",
                "Applicable for installing Drip Irrigation or Micro-Sprinkler Systems",
                "Maximum assistance up to 5 hectares per beneficiary family"
            ],
            "documents_required": [
                "Land title deed / 7/12 / ROR copy",
                "Water source certificate or electricity bill of pump",
                "Soil and water testing report",
                "Quotation from empanelled Micro-Irrigation vendor (Jain Irrigation, Netafim, etc.)"
            ],
            "application_portal_url": "https://pmksy.gov.in",
            "how_to_apply_steps": [
                "Register on state horticulture / agriculture department DBT portal",
                "Select empanelled vendor for site survey and CAD layout design",
                "Vendor submits technical estimation; department issues Administrative Approval",
                "System is installed, GPS geotagged, and field-inspected by Assistant Horticulture Officer (AHO)",
                "Subsidy is credited directly to vendor or farmer's bank account"
            ],
            "special_benefits_for_sc_st_women": "Additional 10-15% top-up in many states (e.g., Gujarat, AP, Tamil Nadu provide up to 70-90% for SC/ST smallholders)."
        },
        {
            "scheme_id": "PM-KUSUM-SOLAR",
            "scheme_name": "Pradhan Mantri Kisan Urja Suraksha evam Utthaan Mahabhiyan (PM-KUSUM Component-B)",
            "official_acronym": "PM-KUSUM",
            "administering_ministry": "Ministry of New and Renewable Energy (MNRE)",
            "level": "Centrally Sponsored / State Shared",
            "category": "Solar Pumps & Green Energy",
            "max_subsidy_amount_inr": 210000.0,
            "subsidy_percentage": 60.0,
            "eligibility_criteria": [
                "Individual farmers, water user associations, FPOs, and panchayats",
                "Installing standalone solar agriculture pumps (3 HP to 10 HP DC/AC surface or submersible)",
                "Land must have available groundwater / surface water without grid connection"
            ],
            "documents_required": [
                "Land revenue records",
                "Aadhaar card and bank account",
                "Proof of water source depth (driller receipt or patwari verification)",
                "Affidavit stating no existing energized electric pump on that land piece"
            ],
            "application_portal_url": "https://pmkusum.mnre.gov.in",
            "how_to_apply_steps": [
                "Apply on the State Renewable Energy Development Agency portal (e.g., MEDA, UPNEDA, HAREDA, RREC)",
                "Choose pump capacity based on groundwater depth (3HP for <30m, 5HP for 30-70m, 7.5HP for >70m)",
                "Pay 10% farmer share online; bank finances 30% if loan opted",
                "Approved vendor installs solar panels, controller, and pump within 90 days with remote telemetry"
            ],
            "special_benefits_for_sc_st_women": "In North-Eastern, Himalayan states and desert regions, Central subsidy is 50%, farmer pays only 10%."
        },
        {
            "scheme_id": "SMAM-MECHANIZATION",
            "scheme_name": "Sub-Mission on Agricultural Mechanization (SMAM / FARMS)",
            "official_acronym": "SMAM",
            "administering_ministry": "Ministry of Agriculture & Farmers Welfare",
            "level": "Central Government (GoI)",
            "category": "Farm Machinery & Custom Hiring",
            "max_subsidy_amount_inr": 250000.0,
            "subsidy_percentage": 50.0,
            "eligibility_criteria": [
                "Small, marginal, and large farmers purchasing approved machinery (Tractors, Rotavators, Laser Levelers)",
                "Rural youth, self-help groups, and FPOs setting up Custom Hiring Centers (CHCs)"
            ],
            "documents_required": [
                "Aadhaar Card",
                "Land ownership proof",
                "Caste certificate (for SC/ST concession)",
                "Dealer invoice / quotation of approved model"
            ],
            "application_portal_url": "https://agrimachinery.nic.in",
            "how_to_apply_steps": [
                "Login to agrimachinery.nic.in and select 'Farmer Registration'",
                "Select machinery category (e.g., Rotavator, Power Tiller, Laser Leveler)",
                "Select authorized manufacturer dealer in your district",
                "Wait for lottery / token generation from District Agriculture Officer",
                "Purchase machine with physical inspection & serial verification; subsidy credited via DBT"
            ],
            "special_benefits_for_sc_st_women": "Women farmers receive an additional 10% higher financial assistance across all tool categories."
        },
        {
            "scheme_id": "AIF-INFRA-FUND",
            "scheme_name": "Agriculture Infrastructure Fund (AIF)",
            "official_acronym": "AIF",
            "administering_ministry": "Ministry of Agriculture and Farmers Welfare",
            "level": "Central Government (GoI)",
            "category": "Post-Harvest Infrastructure & Cold Storage",
            "max_subsidy_amount_inr": 20000000.0,
            "subsidy_percentage": 3.0,
            "eligibility_criteria": [
                "Farmers, FPOs, Agri-entrepreneurs, Startups, Primary Agricultural Credit Societies (PACS)",
                "Projects for post-harvest management: Cold storage, sorting/grading, ripening chambers, silos, warehouses"
            ],
            "documents_required": [
                "Detailed Project Report (DPR)",
                "Bank Loan sanction letter",
                "Land documents (owned or minimum 10-year lease)",
                "KYC of promoters / FPO directors",
                "GST / Udyam registration"
            ],
            "application_portal_url": "https://agriinfra.dac.gov.in",
            "how_to_apply_steps": [
                "Register on agriinfra.dac.gov.in portal",
                "Upload bankable DPR outlining CapEx, OpEx, and post-harvest impact",
                "Select preferred commercial/cooperative lending bank",
                "Ministry scrutinizes and grants in-principle approval within 60 days",
                "Bank disburses loan; interest subvention of 3% is automatically adjusted in EMI for 7 years"
            ],
            "special_benefits_for_sc_st_women": "Credit guarantee fee covered under CGTMSE for up to ₹2 Crore."
        },
        {
            "scheme_id": "MIDH-HORTICULTURE",
            "scheme_name": "Mission for Integrated Development of Horticulture (MIDH)",
            "official_acronym": "MIDH",
            "administering_ministry": "Ministry of Agriculture & Farmers Welfare",
            "level": "Centrally Sponsored / State Shared",
            "category": "Horticulture & Protected Agriculture",
            "max_subsidy_amount_inr": 1800000.0,
            "subsidy_percentage": 50.0,
            "eligibility_criteria": [
                "Farmers undertaking high-value fruit orchards, polyhouses (naturally ventilated or climate controlled)",
                "Mushroom cultivation units and spawn labs"
            ],
            "documents_required": [
                "Land ownership records with clear title",
                "Horticulture plan and cost estimation",
                "Water availability certificate",
                "Vendor design specifications adhering to MIDH technical standards"
            ],
            "application_portal_url": "https://midh.gov.in",
            "how_to_apply_steps": [
                "Apply to District Horticulture Officer (DHO)",
                "Submit project proposal with structural engineering certs",
                "Physical inspection and geotagged approval",
                "Direct subsidy release linked to milestone completion"
            ],
            "special_benefits_for_sc_st_women": "55% assistance in hilly and scheduled tribe areas."
        },
        {
            "scheme_id": "PKVY-ORGANIC",
            "scheme_name": "Paramparagat Krishi Vikas Yojana (PKVY - Natural & Organic Farming)",
            "official_acronym": "PKVY",
            "administering_ministry": "Ministry of Agriculture and Farmers Welfare",
            "level": "Central Government (GoI)",
            "category": "Organic & Natural Farming",
            "max_subsidy_amount_inr": 50000.0,
            "subsidy_percentage": 100.0,
            "eligibility_criteria": [
                "Cluster of minimum 20 farmers with 20 hectares contiguous land",
                "Commitment to convert to organic farming under PGS-India certification"
            ],
            "documents_required": [
                "Cluster farmer roster with Aadhaar",
                "Land records of each member",
                "Resolution to practice chemical-free agriculture"
            ],
            "application_portal_url": "https://pgsindia-ncof.gov.in",
            "how_to_apply_steps": [
                "Form farmer cluster through local Regional Council / KVK / Agriculture Officer",
                "Register cluster on PGS-India portal",
                "Receive ₹31,000/ha for organic inputs (liquid bio-fertilizers, vermicompost, neem cake)",
                "Receive ₹8,800/ha for value addition, packaging, and marketing support"
            ],
            "special_benefits_for_sc_st_women": "Free PGS-India organic certification and QR-code traceable branding."
        }
    ]

    with open(DATA_DIR / "subsidies_database.json", "w", encoding="utf-8") as f:
        json.dump(subsidies, f, indent=2, ensure_ascii=False)
    print("Subsidies database generated.")


def generate_equipment_catalog():
    equipment = [
        {
            "equipment_id": "EQ-TRACTOR-COMPACT-01",
            "name": "Compact / Mini Tractor (20 - 28 HP 4WD)",
            "category": "Land Preparation (Tractor, Rotavator, MB Plough, Laser Leveler)",
            "ideal_farm_size": "Small (1-2 ha / 2.5-5 acres)",
            "estimated_purchase_cost_inr": 380000.0,
            "subsidy_available_pct": 50.0,
            "subsidy_scheme_name": "SMAM Sub-Mission on Agricultural Mechanization",
            "net_cost_after_subsidy_inr": 190000.0,
            "chc_rental_rate_per_acre_or_hour": "₹550 per hour",
            "recommendation_verdict": "Buy with Subsidy",
            "rationale": "Ideal for inter-row intercultural operations in orchards, vegetables, sugarcane, and narrow bunds. Outstanding fuel efficiency (1.5L/hr diesel).",
            "maintenance_and_fuel_cost_per_year_inr": 18000.0
        },
        {
            "equipment_id": "EQ-TRACTOR-UTILITY-02",
            "name": "Heavy Utility Tractor (45 - 55 HP)",
            "category": "Land Preparation (Tractor, Rotavator, MB Plough, Laser Leveler)",
            "ideal_farm_size": "Medium to Large (>5 acres)",
            "estimated_purchase_cost_inr": 780000.0,
            "subsidy_available_pct": 40.0,
            "subsidy_scheme_name": "SMAM / State Krishi Yantra Subsidy",
            "net_cost_after_subsidy_inr": 468000.0,
            "chc_rental_rate_per_acre_or_hour": "₹900 per hour",
            "recommendation_verdict": "Rent from CHC",
            "rationale": "For farmers with <5 acres, buying a 50HP tractor creates financial debt. Renting from a local Custom Hiring Center saves capital for high-quality seeds & drip.",
            "maintenance_and_fuel_cost_per_year_inr": 35000.0
        },
        {
            "equipment_id": "EQ-ROTAVATOR-03",
            "name": "Rotary Tiller / Rotavator (5 - 6 Feet)",
            "category": "Land Preparation (Tractor, Rotavator, MB Plough, Laser Leveler)",
            "ideal_farm_size": "Small (1-2 ha)",
            "estimated_purchase_cost_inr": 110000.0,
            "subsidy_available_pct": 50.0,
            "subsidy_scheme_name": "SMAM Scheme",
            "net_cost_after_subsidy_inr": 55000.0,
            "chc_rental_rate_per_acre_or_hour": "₹800 per acre",
            "recommendation_verdict": "Buy with Subsidy",
            "rationale": "Prepares fine seedbed in single pass, shredding previous crop residue into organic soil mulch.",
            "maintenance_and_fuel_cost_per_year_inr": 5000.0
        },
        {
            "equipment_id": "EQ-LASER-LEVELER-04",
            "name": "Laser Land Leveler",
            "category": "Land Preparation (Tractor, Rotavator, MB Plough, Laser Leveler)",
            "ideal_farm_size": "Custom Hiring / FPO Level",
            "estimated_purchase_cost_inr": 340000.0,
            "subsidy_available_pct": 50.0,
            "subsidy_scheme_name": "SMAM / CRM (Crop Residue Management)",
            "net_cost_after_subsidy_inr": 170000.0,
            "chc_rental_rate_per_acre_or_hour": "₹1,200 per acre (once every 3 years)",
            "recommendation_verdict": "Rent from CHC",
            "rationale": "Laser leveling is only needed once every 3 years. It saves 25% irrigation water and improves crop germination uniformity by 20%.",
            "maintenance_and_fuel_cost_per_year_inr": 8000.0
        },
        {
            "equipment_id": "EQ-DRIP-KIT-05",
            "name": "Automated Drip Irrigation Kit with Venturi Fertigation (per acre)",
            "category": "Irrigation System (Drip, Sprinkler, Solar Pump, Diesel Pump)",
            "ideal_farm_size": "All Farm Sizes",
            "estimated_purchase_cost_inr": 58000.0,
            "subsidy_available_pct": 55.0,
            "subsidy_scheme_name": "PMKSY Per Drop More Crop",
            "net_cost_after_subsidy_inr": 26100.0,
            "chc_rental_rate_per_acre_or_hour": "N/A (Permanent Asset)",
            "recommendation_verdict": "Buy with Subsidy",
            "rationale": "Saves 45-60% water, increases yield by 35-50%, delivers water-soluble fertilizers directly to roots with zero nutrient leaching.",
            "maintenance_and_fuel_cost_per_year_inr": 2500.0
        },
        {
            "equipment_id": "EQ-SOLAR-PUMP-06",
            "name": "5 HP AC/DC Submersible Solar Water Pump",
            "category": "Irrigation System (Drip, Sprinkler, Solar Pump, Diesel Pump)",
            "ideal_farm_size": "2.5 to 7.5 acres",
            "estimated_purchase_cost_inr": 260000.0,
            "subsidy_available_pct": 60.0,
            "subsidy_scheme_name": "PM-KUSUM Component-B",
            "net_cost_after_subsidy_inr": 104000.0,
            "chc_rental_rate_per_acre_or_hour": "N/A",
            "recommendation_verdict": "Buy with Subsidy",
            "rationale": "Zero electricity bills and zero diesel expenditure forever. 25-year solar panel performance warranty. Farmer recovers share in 14 months.",
            "maintenance_and_fuel_cost_per_year_inr": 1500.0
        },
        {
            "equipment_id": "EQ-AGRI-DRONE-07",
            "name": "Kisan Agri Drone (10L Payload for Precision Spraying)",
            "category": "Precision Agri-Tech (Agri Drone, Soil Sensors, GPS Guidance)",
            "ideal_farm_size": "FPO / Agri-Entrepreneur / Custom Hiring",
            "estimated_purchase_cost_inr": 650000.0,
            "subsidy_available_pct": 75.0,
            "subsidy_scheme_name": "Sub-Mission on Agricultural Mechanization (Kisan Drone Scheme)",
            "net_cost_after_subsidy_inr": 162500.0,
            "chc_rental_rate_per_acre_or_hour": "₹400 per acre spray fee",
            "recommendation_verdict": "Rent from CHC",
            "rationale": "Sprays 1 acre in 7 minutes with ultra-low volume nozzle (saves 90% water compared to manual knapsack). Renting a drone service is cheapest for individual farmers.",
            "maintenance_and_fuel_cost_per_year_inr": 20000.0
        }
    ]

    with open(DATA_DIR / "equipment_catalog.json", "w", encoding="utf-8") as f:
        json.dump(equipment, f, indent=2, ensure_ascii=False)
    print("Equipment catalog generated.")


def generate_agribusiness_models():
    models = [
        {
            "model_id": "BIZ-DAL-MILL-01",
            "business_title": "Mini Dal Mill & Pulse Processing Enterprise",
            "target_sector": "Primary Food Processing",
            "minimum_land_required_acres": 0.25,
            "total_capital_expenditure_capex_inr": 650000.0,
            "annual_operating_expenditure_opex_inr": 1800000.0,
            "projected_annual_gross_revenue_inr": 2450000.0,
            "projected_annual_net_profit_inr": 650000.0,
            "payback_period_years": 1.2,
            "internal_rate_of_return_irr_pct": 38.5,
            "applicable_subsidies": ["PM Formalization of Micro Food Processing Enterprises (PM-FME)", "AIF (3% Interest Subvention)"],
            "subsidy_amount_expected_inr": 227500.0,
            "net_farmer_investment_inr": 422500.0,
            "key_machinery_required": [
                "Dehusker & Dal Splitter (200 kg/hr capacity)",
                "Vibro Grader and Cleaner",
                "Polisher with emery stone rolls",
                "Nitrogen flushing continuous band sealer packaging machine"
            ],
            "licenses_required": ["FSSAI Basic / State License", "Udyam MSME Registration", "GST Registration", "Local Trade License"],
            "target_buyer_demographics": ["Local Kirana wholesale distributors", "Urban direct-to-consumer grocery subscription brands", "State civil supplies tenders"],
            "step_by_step_setup_guide": [
                "Procure raw pigeon pea (arhar), chickpea (chana), or moong directly from local farmers at mandi rate + 5% incentive",
                "Install a 200 kg/hour semi-automatic mini dal mill in a 1,000 sq ft shed",
                "Process into unpolished, high-protein dal retaining nutrient-rich aleurone layer",
                "Package into branded 1kg/5kg biodegradable pouches with FSSAI QR code",
                "Sell directly at ₹130-150/kg compared to raw unhusked sale price of ₹75/kg, pocketing processing margin"
            ]
        },
        {
            "model_id": "BIZ-COLD-PRESSED-OIL-02",
            "business_title": "Cold-Pressed Wood Pressed (Kachi Ghani) Oil Unit",
            "target_sector": "High-Value Edible Oils & Functional Foods",
            "minimum_land_required_acres": 0.2,
            "total_capital_expenditure_capex_inr": 550000.0,
            "annual_operating_expenditure_opex_inr": 1400000.0,
            "projected_annual_gross_revenue_inr": 2100000.0,
            "projected_annual_net_profit_inr": 700000.0,
            "payback_period_years": 1.1,
            "internal_rate_of_return_irr_pct": 44.0,
            "applicable_subsidies": ["PM-FME 35% Credit Linked Capital Subsidy", "PMEGP (Prime Minister Employment Generation Programme)"],
            "subsidy_amount_expected_inr": 192500.0,
            "net_farmer_investment_inr": 357500.0,
            "key_machinery_required": [
                "Wooden Ghani (Marachekku) automated press (2 units)",
                "Seed cleaner and destoner",
                "Filter press / cotton fabric settling tank",
                "Glass bottle filling and capping machine"
            ],
            "licenses_required": ["FSSAI Food License", "Udyam Aadhar", "GST Registration"],
            "target_buyer_demographics": ["Health-conscious urban consumers", "Organic supermarkets", "Direct WhatsApp e-commerce community"],
            "step_by_step_setup_guide": [
                "Source high-grade farm-grown Mustard, Groundnut, or Sesame seeds",
                "Operate slow-speed (<14 RPM) wooden cold presses to ensure temperature remains below 45°C, preserving antioxidants and tocopherols",
                "Bottle pure golden oil without chemical refining, bleaching, or deodorizing",
                "Repackage oil cake (Khali) and sell as premium high-protein cattle feed at ₹28-35/kg",
                "Retail cold-pressed mustard oil at ₹280-350/L and groundnut oil at ₹360-450/L"
            ]
        },
        {
            "model_id": "BIZ-VERMICOMPOST-03",
            "business_title": "Commercial Vermicomposting & Bio-Enriched Organic Fertilizer Plant",
            "target_sector": "Bio-Fertilizer & Circular Economy",
            "minimum_land_required_acres": 0.5,
            "total_capital_expenditure_capex_inr": 280000.0,
            "annual_operating_expenditure_opex_inr": 350000.0,
            "projected_annual_gross_revenue_inr": 850000.0,
            "projected_annual_net_profit_inr": 500000.0,
            "payback_period_years": 0.7,
            "internal_rate_of_return_irr_pct": 65.0,
            "applicable_subsidies": ["PKVY Cluster Fund", "RKVY-RAFTAAR Agripreneurship Grant"],
            "subsidy_amount_expected_inr": 100000.0,
            "net_farmer_investment_inr": 180000.0,
            "key_machinery_required": [
                "HDPE vermi-beds with aeration windows (30 beds of 12x4x2 ft)",
                "Rotary compost screening trommel with 3mm mesh",
                "Moisture meter and electronic weighing scale",
                "Bag stitching machine"
            ],
            "licenses_required": ["Fertilizer Control Order (FCO) Registration / State Dept of Agriculture License", "Udyam MSME"],
            "target_buyer_demographics": ["Organic farmers", "Polyhouse growers", "Urban landscape nurseries", "Home gardeners"],
            "step_by_step_setup_guide": [
                "Collect cow dung and crop farm residue; let pre-decompose for 15 days",
                "Inoculate with Eisenia fetida (red wigglers) earthworms at 2 kg per bed",
                "Maintain 65-70% moisture and shady temperature for 50-60 days",
                "Harvest granular black vermicast, screen through trommel, and enrich with Trichoderma and Mycorrhiza",
                "Bag in 5kg, 25kg, and 50kg bags and sell at ₹8-12/kg wholesale and ₹25/kg retail"
            ]
        },
        {
            "model_id": "BIZ-POLYHOUSE-04",
            "business_title": "Naturally Ventilated Polyhouse Horticulture Unit (1,000 sq meters)",
            "target_sector": "Protected Agriculture",
            "minimum_land_required_acres": 0.3,
            "total_capital_expenditure_capex_inr": 1150000.0,
            "annual_operating_expenditure_opex_inr": 320000.0,
            "projected_annual_gross_revenue_inr": 850000.0,
            "projected_annual_net_profit_inr": 530000.0,
            "payback_period_years": 2.2,
            "internal_rate_of_return_irr_pct": 32.0,
            "applicable_subsidies": ["Mission for Integrated Development of Horticulture (MIDH - 50% Subsidy)", "AIF 3% Interest Subvention"],
            "subsidy_amount_expected_inr": 525000.0,
            "net_farmer_investment_inr": 625000.0,
            "key_machinery_required": [
                "GI pipe tubular structure with 200-micron UV-stabilized polythene sheet",
                "Micro-drip irrigation network with inline PC drippers and Venturi",
                "Overhead misting / fogger system with automated timer",
                "Shade net screen (50% green/black)"
            ],
            "licenses_required": ["Land Revenue Certificate", "Horticulture Department Empanelled Structural Cert"],
            "target_buyer_demographics": ["Quick commerce apps (Blinkit, Zepto, Swiggy Instamart)", "Wholesale hotels, restaurants & caterers (HORECA)", "Exporters"],
            "step_by_step_setup_guide": [
                "Construct 1000 sqm naturally ventilated polyhouse structure with empanelled agency under MIDH subsidy",
                "Cultivate parthenocarpic seedless English cucumber or yellow/red capsicum",
                "Achieve 3 crop cycles per year yielding 12-15 tons of premium grade produce",
                "Sell directly to premium retail buyers at fixed contractual rates of ₹35-50/kg, eliminating mandi fluctuations"
            ]
        }
    ]

    with open(DATA_DIR / "agribusiness_models.json", "w", encoding="utf-8") as f:
        json.dump(models, f, indent=2, ensure_ascii=False)
    print("Agribusiness models generated.")


def generate_soil_benchmarks():
    soil_benchmarks = {
        "Alluvial": {
            "description": "Formed by river silt deposits; fertile, loamy to sandy loam, ideal for cereals, sugarcane, potatoes.",
            "bulk_density_g_cm3": 1.35,
            "porosity_pct": 46.0,
            "field_capacity_pct": 28.0,
            "wilting_point_pct": 12.0,
            "available_water_capacity_mm_m": 160.0,
            "ph_typical": 7.2,
            "cation_exchange_capacity_meq_100g": 18.0,
            "recommended_amendments": "Zinc sulphate (25 kg/ha) every 2 years; regular organic manure to maintain active humus."
        },
        "Black Cotton (Vertisol)": {
            "description": "High montmorillonite clay content; deep swelling and shrinking cracks, rich in Ca and Mg, high water retention.",
            "bulk_density_g_cm3": 1.45,
            "porosity_pct": 52.0,
            "field_capacity_pct": 38.0,
            "wilting_point_pct": 20.0,
            "available_water_capacity_mm_m": 190.0,
            "ph_typical": 7.8,
            "cation_exchange_capacity_meq_100g": 38.0,
            "recommended_amendments": "Broad bed furrow planting to prevent waterlogging; apply elemental Sulphur and Farmyard Manure (FYM)."
        },
        "Red Sandy Loam": {
            "description": "Formed from crystalline granite rocks; porous, gravelly, low organic matter, responds well to drip irrigation.",
            "bulk_density_g_cm3": 1.50,
            "porosity_pct": 39.0,
            "field_capacity_pct": 19.0,
            "wilting_point_pct": 7.0,
            "available_water_capacity_mm_m": 110.0,
            "ph_typical": 6.4,
            "cation_exchange_capacity_meq_100g": 12.0,
            "recommended_amendments": "Heavy green manuring with Sunhemp/Dhaincha; lime application if pH falls below 5.8."
        },
        "Laterite": {
            "description": "Formed under intense tropical weathering with heavy rainfall; rich in iron and aluminum oxides, acidic.",
            "bulk_density_g_cm3": 1.55,
            "porosity_pct": 40.0,
            "field_capacity_pct": 22.0,
            "wilting_point_pct": 10.0,
            "available_water_capacity_mm_m": 120.0,
            "ph_typical": 5.4,
            "cation_exchange_capacity_meq_100g": 9.0,
            "recommended_amendments": "Agricultural lime or dolomite (2-3 tons/ha) to neutralize toxic aluminum; rock phosphate with PSB."
        },
        "Clay Loam": {
            "description": "Balanced soil with approx 30% clay, 40% silt, 30% sand; excellent nutrient retention and moderate drainage.",
            "bulk_density_g_cm3": 1.38,
            "porosity_pct": 48.0,
            "field_capacity_pct": 32.0,
            "wilting_point_pct": 15.0,
            "available_water_capacity_mm_m": 170.0,
            "ph_typical": 6.9,
            "cation_exchange_capacity_meq_100g": 24.0,
            "recommended_amendments": "Vermicompost dosing (2 tons/acre) and minimum tillage to preserve soil aggregate stability."
        },
        "Sandy Loam": {
            "description": "Light, warm, fast-draining soil; low natural fertility but responds dramatically to precision fertigation.",
            "bulk_density_g_cm3": 1.48,
            "porosity_pct": 42.0,
            "field_capacity_pct": 18.0,
            "wilting_point_pct": 6.0,
            "available_water_capacity_mm_m": 100.0,
            "ph_typical": 7.0,
            "cation_exchange_capacity_meq_100g": 11.0,
            "recommended_amendments": "Frequent split applications of water-soluble fertilizers; heavy biochar and mulching to retain moisture."
        },
        "Desert Sandy": {
            "description": "Arid aeolian sand with low water holding capacity; prone to wind erosion; requires drip irrigation.",
            "bulk_density_g_cm3": 1.60,
            "porosity_pct": 36.0,
            "field_capacity_pct": 11.0,
            "wilting_point_pct": 3.0,
            "available_water_capacity_mm_m": 65.0,
            "ph_typical": 8.2,
            "cation_exchange_capacity_meq_100g": 6.0,
            "recommended_amendments": "Hydrogel polymers, shelterbelt tree windbreaks (Khejri, Neem), drip irrigation mandatory."
        },
        "Peaty / Marshy": {
            "description": "Formed under anaerobic submerged conditions; very high organic matter (>15%), often acidic with blue-grey iron.",
            "bulk_density_g_cm3": 0.95,
            "porosity_pct": 65.0,
            "field_capacity_pct": 55.0,
            "wilting_point_pct": 28.0,
            "available_water_capacity_mm_m": 220.0,
            "ph_typical": 4.8,
            "cation_exchange_capacity_meq_100g": 45.0,
            "recommended_amendments": "Drainage channels, sub-surface tile drains, copper and zinc supplementation, liming."
        },
        "Saline / Alkaline": {
            "description": "High soluble salts or exchangeable sodium percentage (ESP > 15%); poor physical structure, dispersion.",
            "bulk_density_g_cm3": 1.58,
            "porosity_pct": 38.0,
            "field_capacity_pct": 26.0,
            "wilting_point_pct": 14.0,
            "available_water_capacity_mm_m": 90.0,
            "ph_typical": 8.9,
            "cation_exchange_capacity_meq_100g": 22.0,
            "recommended_amendments": "Gypsum requirement calculation: apply mineral Gypsum (4-8 tons/ha), flush with fresh water, grow Dhaincha."
        }
    }

    with open(DATA_DIR / "soil_benchmarks.json", "w", encoding="utf-8") as f:
        json.dump(soil_benchmarks, f, indent=2, ensure_ascii=False)
    print("Soil benchmarks generated.")


def generate_groundwater_zones():
    gw_data = {
        "depth_guidelines": {
            "0-5 mbgl": {"status": "Shallow Water Table", "drainage_risk": "Moderate waterlogging risk during monsoon", "solar_pump_spec": "3 HP surface pump or 3 HP shallow submersible"},
            "5-15 mbgl": {"status": "Safe & Optimal", "drainage_risk": "Low risk; excellent for open well / shallow borewell", "solar_pump_spec": "3-5 HP submersible solar pump"},
            "15-30 mbgl": {"status": "Moderately Deep", "drainage_risk": "No waterlogging; requires tubewell", "solar_pump_spec": "5 HP AC submersible pump"},
            "30-60 mbgl": {"status": "Critical Deep Table", "drainage_risk": "Severe depletion risk; drip irrigation mandatory", "solar_pump_spec": "7.5 HP high-head multi-stage submersible pump"},
            ">60 mbgl": {"status": "Over-Exploited / Arid Aquifer", "drainage_risk": "Prohibitive pumping cost; micro-catchment water harvesting mandatory", "solar_pump_spec": "7.5-10 HP solar pump with high-efficiency motor"}
        },
        "aquifer_typologies": {
            "Alluvial Unconfined": {"recharge_rate": "High", "specific_yield_pct": 12.0, "water_quality": "Generally fresh, check for fluoride/arsenic in localized pockets"},
            "Basaltic Deccan Trap (Hard Rock)": {"recharge_rate": "Moderate-Low", "specific_yield_pct": 3.0, "water_quality": "Good, depends on fracture connectivity"},
            "Crystalline Granite / Gneiss": {"recharge_rate": "Low", "specific_yield_pct": 2.5, "water_quality": "High fluoride in deep borewells"},
            "Coastal Sand Dune Aquifer": {"recharge_rate": "Very High", "specific_yield_pct": 20.0, "water_quality": "Risk of seawater intrusion if over-pumped"}
        }
    }

    with open(DATA_DIR / "groundwater_zones.json", "w", encoding="utf-8") as f:
        json.dump(gw_data, f, indent=2, ensure_ascii=False)
    print("Groundwater zones generated.")


if __name__ == "__main__":
    generate_agro_climatic_zones()
    generate_crops_database()
    generate_subsidies_database()
    generate_equipment_catalog()
    generate_agribusiness_models()
    generate_soil_benchmarks()
    generate_groundwater_zones()
    print("All AmiFarmer scientific datasets successfully generated!")
