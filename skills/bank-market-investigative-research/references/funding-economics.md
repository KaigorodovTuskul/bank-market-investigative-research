# Wholesale funding and agent cost

To compare two quotes: same principal P, currency, maturity D, value date, guarantees, recall terms and counterparty risk. If risk differs, adjust or reject comparison.

`gross_saving = average_actual_balance * (direct_rate - agent_route_rate) * D / day_count`

`net_before_other_costs = gross_saving - one_time_agent_fee - additional_costs`

`breakeven_days = (fee + costs) * day_count / (average_balance * positive_rate_advantage)`

Where `one_time_agent_fee = agreed_initial_principal * fee_rate`; only for an upfront-fee contract. A periodic fee instead accrues according to actual balance and days. Separate contract acquisition cost from per-deal commission and renewal costs. Use a different fee basis when the contract requires it.

Compute scenarios for full funding, partial balances and no renewal. Add verified taxes, reserve requirements, settlement/hedging, legal and AML costs where applicable; leave missing costs explicitly unresolved, not zero. Show all-in margins and stress triggers.

Optional deterministic script `scripts/funding_economics.py` uses `Decimal` and synthetic input JSON; it is a calculation aid, **not** a quotation engine.
