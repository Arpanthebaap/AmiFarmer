"""
Data loaders and accessors for AmiFarmer internal agricultural datasets.
"""

import json
from pathlib import Path
from typing import List, Dict, Any, Optional

DATA_DIR = Path(__file__).parent


def load_agro_climatic_zones() -> List[Dict[str, Any]]:
    path = DATA_DIR / "agro_climatic_zones.json"
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def load_crops_database() -> List[Dict[str, Any]]:
    path = DATA_DIR / "crops_database.json"
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def load_subsidies_database() -> List[Dict[str, Any]]:
    path = DATA_DIR / "subsidies_database.json"
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def load_equipment_catalog() -> List[Dict[str, Any]]:
    path = DATA_DIR / "equipment_catalog.json"
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def load_agribusiness_models() -> List[Dict[str, Any]]:
    path = DATA_DIR / "agribusiness_models.json"
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def load_soil_benchmarks() -> Dict[str, Any]:
    path = DATA_DIR / "soil_benchmarks.json"
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def load_groundwater_zones() -> Dict[str, Any]:
    path = DATA_DIR / "groundwater_zones.json"
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def get_zone_by_state_and_district(state: str, district: Optional[str] = None) -> Optional[Dict[str, Any]]:
    zones = load_agro_climatic_zones()
    district_clean = district.lower().strip() if district else None
    state_clean = state.lower().strip()

    # Match by district first
    if district_clean:
        for z in zones:
            for d in z.get("key_districts", []):
                if district_clean in d.lower():
                    return z

    # Fallback to state
    for z in zones:
        for s in z.get("states", []):
            if state_clean in s.lower() or s.lower() in state_clean:
                return z

    return zones[3]  # Default fallback: Middle Gangetic Plain
