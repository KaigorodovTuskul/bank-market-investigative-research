#!/usr/bin/env python3
"""Synthetic funding economics. No market, legal or tax assumptions embedded."""
import argparse
import json
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path


def D(v):
    return Decimal(str(v))


def calculate(data):
    p = D(data["principal_rub"])
    avg = D(data["average_balance_rub"])
    days = D(data["days"])
    basis = D(data.get("day_count", 365))
    spread = D(data["direct_rate"]) - D(data["agent_rate"])
    fee = p * D(data["upfront_fee_rate"])
    costs = D(data.get("other_costs_rub", "0"))
    if min(p,avg,days,basis,fee,costs) < 0 or basis == 0:
        raise ValueError("Principal, balance, days, basis, fees and costs must be nonnegative; basis > 0")
    gross = avg * spread * days / basis
    net = gross - fee - costs
    breakeven = (fee + costs) * basis / (avg * spread) if spread > 0 and avg > 0 else None
    q = Decimal("0.01")
    return {"spread_pp": str(spread * 100),
            "gross_saving_rub": str(gross.quantize(q, rounding=ROUND_HALF_UP)),
            "agent_fee_rub": str(fee.quantize(q, rounding=ROUND_HALF_UP)),
            "other_costs_rub": str(costs.quantize(q, rounding=ROUND_HALF_UP)),
            "net_before_other_costs_rub": str(net.quantize(q, rounding=ROUND_HALF_UP)),
            "breakeven_days": str(breakeven.quantize(q, rounding=ROUND_HALF_UP)) if breakeven is not None else None,
            "status": "synthetic_model_not_market_quote"}


def main():
    parser=argparse.ArgumentParser();parser.add_argument("--input",required=True)
    args=parser.parse_args();inp=json.loads(Path(args.input).read_text(encoding="utf-8"))
    print(json.dumps(calculate(inp), ensure_ascii=False,indent=2))
if __name__=='__main__':main()
