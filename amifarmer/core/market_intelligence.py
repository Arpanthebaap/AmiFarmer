"""
AmiFarmer Market Intelligence, Price Arbitrage, and Post-Harvest Economics Engine.
Connects APMC Mandi trends, Minimum Support Price (MSP) benchmarks,
and direct-to-consumer (D2C) value-addition multipliers.
"""

from typing import Dict, Any, List, Optional
from amifarmer.models.market_profile import MarketingChannel, MarketArbitrageStrategy


class MarketIntelligence:
    """
    Analyzes crop price realization across wholesale mandis, corporate contract farming,
    e-NAM, and direct consumer supply chains.
    """

    VALUE_ADDITION_CATALOG = {
        "Mustard / Rapeseed": {
            "processed_product": "Wood-Pressed Pure Kachi Ghani Mustard Oil + Cattle Feed (Khali)",
            "raw_price_per_kg": 62.0,
            "processed_price_per_liter": 280.0,
            "oil_recovery_pct": 36.0,
            "cake_recovery_pct": 60.0,
            "cake_price_per_kg": 30.0,
            "processing_cost_per_kg": 6.0,
            "value_multiplier": 1.95
        },
        "Turmeric": {
            "processed_product": "Boiled, Polished & Ground Pure Curcumin-Rich Turmeric Powder",
            "raw_price_per_kg": 25.0,  # fresh wet rhizome
            "processed_price_per_kg": 260.0,  # dry powder
            "recovery_pct": 20.0,
            "processing_cost_per_kg": 15.0,
            "value_multiplier": 2.60
        },
        "Chickpea (Gram / Chana)": {
            "processed_product": "Unpolished Chana Dal & Pure Besan (Gram Flour)",
            "raw_price_per_kg": 59.0,
            "processed_price_per_kg": 135.0,
            "recovery_pct": 75.0,
            "processing_cost_per_kg": 8.0,
            "value_multiplier": 1.70
        },
        "Garlic": {
            "processed_product": "Dehydrated Garlic Flakes / Retort Pouch Pure Garlic Paste",
            "raw_price_per_kg": 110.0,
            "processed_price_per_kg": 350.0,
            "recovery_pct": 65.0,
            "processing_cost_per_kg": 25.0,
            "value_multiplier": 2.10
        },
        "Tomato": {
            "processed_product": "Sun-Dried Tomatoes in Olive Oil / Concentrated Tomato Puree",
            "raw_price_per_kg": 16.0,
            "processed_price_per_kg": 180.0,
            "recovery_pct": 14.0,
            "processing_cost_per_kg": 12.0,
            "value_multiplier": 1.85
        }
    }

    def analyze_market_options(
        self,
        crop_name: str,
        yield_quintals_per_acre: float,
        modal_mandi_price_inr: float,
        d2c_price_inr: float,
        msp_inr: Optional[float] = None
    ) -> Dict[str, Any]:
        """
        Calculates revenue across all distribution channels and assesses value-addition gain.
        """
        # 1 Quintal = 100 kg
        total_kg = yield_quintals_per_acre * 100.0

        # Channel 1: APMC Mandi Wholesale
        mandi_rate_per_kg = modal_mandi_price_inr / 100.0
        mandi_gross = total_kg * mandi_rate_per_kg
        mandi_comm_and_transport = mandi_gross * 0.08  # 8% mandi cess, commission, freight
        mandi_net_revenue = mandi_gross - mandi_comm_and_transport

        # Channel 2: FPO Aggregation (Farmer Producer Organization)
        # FPOs eliminate middleman commission and negotiate 10% premium with millers
        fpo_rate_per_kg = mandi_rate_per_kg * 1.08
        fpo_gross = total_kg * fpo_rate_per_kg
        fpo_net_revenue = fpo_gross * 0.96  # 4% collective logistics

        # Channel 3: Direct to Consumer (D2C / Farmer Markets / WhatsApp community)
        d2c_rate_per_kg = d2c_price_inr / 100.0
        d2c_gross = total_kg * d2c_rate_per_kg
        d2c_packing_and_delivery = total_kg * 14.0  # ₹14/kg packaging, sorting, delivery
        d2c_net_revenue = d2c_gross - d2c_packing_and_delivery

        # Channel 4: MSP Procurement (if eligible)
        msp_revenue = None
        if msp_inr:
            msp_gross = total_kg * (msp_inr / 100.0)
            msp_revenue = round(msp_gross * 0.98, 0)  # 2% handling

        # Value Addition Potential
        val_add_info = self.VALUE_ADDITION_CATALOG.get(crop_name)
        value_addition_summary = None

        if val_add_info:
            raw_kg = total_kg
            proc_cost = raw_kg * val_add_info["processing_cost_per_kg"]
            if "oil_recovery_pct" in val_add_info:
                oil_liters = raw_kg * (val_add_info["oil_recovery_pct"] / 100.0)
                cake_kg = raw_kg * (val_add_info["cake_recovery_pct"] / 100.0)
                gross_proc_rev = (oil_liters * val_add_info["processed_price_per_liter"]) + (cake_kg * val_add_info["cake_price_per_kg"])
            else:
                proc_kg = raw_kg * (val_add_info["recovery_pct"] / 100.0)
                gross_proc_rev = proc_kg * val_add_info["processed_price_per_kg"]

            net_proc_revenue = gross_proc_rev - proc_cost
            extra_profit_vs_mandi = net_proc_revenue - mandi_net_revenue

            value_addition_summary = {
                "product_type": val_add_info["processed_product"],
                "value_multiplier": val_add_info["value_multiplier"],
                "gross_processed_revenue_inr": round(gross_proc_rev, 0),
                "processing_cost_inr": round(proc_cost, 0),
                "net_processed_revenue_inr": round(net_proc_revenue, 0),
                "incremental_profit_over_mandi_inr": round(extra_profit_vs_mandi, 0),
                "percentage_income_boost": round((extra_profit_vs_mandi / max(1.0, mandi_net_revenue)) * 100.0, 1)
            }

        return {
            "crop_name": crop_name,
            "total_harvest_kg": total_kg,
            "mandi_wholesale": {
                "rate_per_kg_inr": round(mandi_rate_per_kg, 2),
                "net_revenue_per_acre_inr": round(mandi_net_revenue, 0)
            },
            "fpo_collective": {
                "rate_per_kg_inr": round(fpo_rate_per_kg, 2),
                "net_revenue_per_acre_inr": round(fpo_net_revenue, 0),
                "gain_over_mandi_pct": round(((fpo_net_revenue - mandi_net_revenue) / max(1.0, mandi_net_revenue)) * 100.0, 1)
            },
            "direct_to_consumer": {
                "rate_per_kg_inr": round(d2c_rate_per_kg, 2),
                "net_revenue_per_acre_inr": round(d2c_net_revenue, 0),
                "gain_over_mandi_pct": round(((d2c_net_revenue - mandi_net_revenue) / max(1.0, mandi_net_revenue)) * 100.0, 1)
            },
            "msp_procurement": {
                "eligible": bool(msp_inr),
                "msp_rate_per_quintal_inr": msp_inr,
                "net_revenue_per_acre_inr": msp_revenue
            },
            "value_addition": value_addition_summary,
            "storage_advisory": (
                "Hold produce in ventilated hermetic warehouse or solar cold room for 60-90 days post-harvest to capture 25-40% price rise."
                if crop_name in ["Onion", "Garlic", "Mustard / Rapeseed", "Chickpea (Gram / Chana)"]
                else "Perishable produce: Grade, chill to 4-8°C, and route immediately to quick-commerce or wholesale within 24 hours."
            )
        }
