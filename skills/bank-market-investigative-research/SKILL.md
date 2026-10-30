---
name: bank-market-investigative-research
description: Investigate banking funding markets, interbank deposits, agents and liquidity with primary sources, auditable calculations and executive-ready reports. Use for Russian banking market intelligence and institution-level funding studies.
license: MIT
metadata:
  version: "1.0.0"
  language: ru
  domain: banking
---

# Bank Market Investigative Research

**Purpose:** deliver decision-useful, traceable institutional banking research. Do not optimize for report length or apparent certainty.

## Entry criteria

Activate for bank funding/interbank markets, deposit brokerage, money-market liquidity, regulatory disclosures, banking intermediary models or source-backed executive reports. For unrelated work do not load this skill.

Determine the decision, bank's role (borrower/lender), jurisdictions, instruments, horizon, as-of date, audience and required file type. If unresolved details are not material, proceed with labeled assumptions.

## Workflow

1. **Define market boundary.** Distinguish resident/nonresident bank, corporate depositor, individual client, counterparty versus agent, principal versus broker, bank-specific balance versus market turnover, credit versus REPO.
2. **Build evidence ledger.** Primary regulator, court, contract or official filing sources first; commercial statements are claims about services, not transaction proof. Consult [source evidence](references/source-evidence.md) only for substantial research.
3. **Search narrowly.** Russian and English; instrument-specific legal terms and court case numbers. Expand to international language only if counterparties require it. Consult [source map](references/sources-and-search.md) when source discovery is the bottleneck.
4. **Extract and reconcile.** Define units, date, stock/flow, bank sample, resident status, currency, maturity, reporting coverage and publication date. See [market data](references/bank-market-data.md) when using regulatory series.
5. **Assess legal and financial risks** separately from operational feasibility. Read [legal checks](references/legal-and-compliance.md) when contracts, taxes, foreign agents or sanctions matter. A research report is not a legal opinion.
6. **Model economics** with transparent assumptions and a direct comparable case. Read [cost model](references/funding-economics.md) if commissions or funding price are relevant; use the Python script for synthetic arithmetic.
7. **Write for the decision owner.** Lead with conclusion, observed facts, implications and specific conditional decision. For management reports read [writing standard](references/management-report.md). Cite every material factual claim beside the statement.
8. **Judge pass before delivery.** Verify source reachability, exact dates, arithmetic, scope confusion, contradicted claims, missing evidence and output rendering. Stop revising when another iteration would only reword conclusions.

## Evidence status (always apply)

- **Established**: supported by traceable primary document measuring the exact claim.
- **Reported**: a business's own claim about its service or market; do not promote it to an executed transaction.
- **Derived**: mathematical transformation; expose source and formula.
- **Hypothesis**: plausible but unproven explanation; never present as fact.
- **Unresolved**: essential evidence absent; do not synthesize its value.

A bank agent's role needs evidence of introduction/mandate; a **completed bank-to-bank funding transaction** additionally needs lender-bank identity, borrower, contract, cash movement and fee attribution. Client onboarding or corporate deposits do not establish the latter.

## Tool routing (optional, capability-dependent)

Use a connected GitHub tool to inspect user-cited repositories. Use web search plus dedicated browser/extraction (e.g., TinyFish), if available; try `https://r.jina.ai/https://...` as a **fallback reader**, then validate against original material. Use Bank of Russia, MOEX and BIS for original series. A market-data MCP such as Simulacre AI may help with rates and market context, **not** with proving brokered-deposit transactions. Never assume a tool or data source is connected. Avoid broad searches after saturation unless new search vocabulary arises.

## Deliverables and stop condition

Produce requested format (typically `.docx` plus optional private audit ledger), not an internal agent diary. Keep exploratory searches, review scores, previous-version notes and workflow labels **out of the leadership report**. Cite stable URLs with descriptive titles; no tool-specific citation tokens.

Stop when the question is decision-ready, material known gaps are clearly disclosed, relevant primary sources were checked, calculations pass and the actual file was visually inspected. Otherwise deliver what is proven without inventing the rest.
