<div align="center">
  <h1>Bank Market Investigative Research</h1>
  <p><strong>Evidence first. Executive-ready banking analysis.</strong></p>
  <p>An open-source Agent Skill for investigating banking funding markets, interbank deposits,<br>intermediaries, regulatory statistics, and institutional competitors with traceable primary sources.</p>
  <p>
    <a href="https://www.skills.sh/kaigorodovtuskul/bank-market-investigative-research/bank-market-investigative-research"><img src="https://img.shields.io/badge/skills.sh-Bank%20Market%20Research-111111" alt="skills.sh"></a>
    <a href="https://agentskills.io/specification"><img src="https://img.shields.io/badge/Agent_Skills-open_standard-00B8C8" alt="Agent Skills"></a>
    <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-586776" alt="MIT"></a>
    <img src="https://img.shields.io/badge/version-1.0.0-00B8C8" alt="Version 1.0.0">
    <img src="https://img.shields.io/badge/python-3.10+-blue.svg" alt="Python 3.10+">
  </p>
  <p><a href="#quick-start">Quick start</a> · <a href="#what-it-covers">What it covers</a> · <a href="#how-it-runs">How it runs</a> · <a href="#example">Example</a> · <a href="#methodology">Methodology</a></p>
  <p><strong>English</strong> · <strong>Русский</strong></p>
</div>

---

## Why Bank Market Investigative Research?

Conducting due diligence and institutional research on banking funding markets requires avoiding critical cognitive traps:
- **Commercial Claims ≠ Completed Transactions:** Marketing statements by brokers or service providers do not prove executed bank-to-bank deals.
- **Conflation of Roles:** An agent introducing corporate depositors is not engaging in interbank lending.
- **Traceable Rigor:** Every factual finding must be backed by a primary regulatory, court, or contract source with a formal evidence status classification.

Canonical skill specification: [`skills/bank-market-investigative-research/SKILL.md`](skills/bank-market-investigative-research/SKILL.md).

---

## Quick Start

### Install for AI Agents (Antigravity, Codex, Claude Code, Cursor)

Via Agent Skills CLI:
```bash
npx skills add KaigorodovTuskul/bank-market-investigative-research --skill bank-market-investigative-research
```

Or install locally with the zero-dependency Python installer:
```bash
python scripts/install.py --project /path/to/your/project
```

### Give the AI Agent a task:
```text
Use bank-market-investigative-research.
Investigate how Russian banks use intermediaries to attract wholesale deposits.
Separately assess evidence for bank-to-bank transactions, corporate deposits, and client onboarding.
Prepare a management memo with primary source links, legal verification, and reproducible fee modeling.
```

---

## What It Covers

- **Market Definition & Primary Sources:** Bank of Russia (CBR), MOEX, BIS, official filings, court records.
- **Intermediary & Brokerage Models:** Deposit brokers, agency commissions, wholesale funding, bank/nonbank counterparty verification.
- **Five-Tier Evidence Standard:** Established, Reported, Derived, Hypothesis, Unresolved.
- **Deterministic Economics:** Reproducible funding cost models with explicit assumptions via Python arithmetic.
- **Executive Writing Standard:** Restrained, precise prose; primary citations; executive memos.

---

## How It Runs

1. Read the **compact** `SKILL.md` (~50 lines) only when relevant; do not preload heavy references into context.
2. Load specialized topic guides on demand:
   - `sources-and-search`: Discovery strategies and search syntax.
   - `source-evidence`: Evidentiary standards and transaction verification.
   - `bank-market-data`: Bank of Russia series, Form 101, stock vs flow reconciliations.
   - `legal-and-compliance`: Contract law, banking secrecy, tax, and sanctions checks.
   - `funding-economics`: Mathematical cost-of-funds and fee model.
   - `management-report`: Executive report structure and memo formatting.
3. Validate citations and calculations before delivering. Stop when additional search has low marginal value.

---

## Repository Structure

```text
bank-market-investigative-research/
├── skills/
│   └── bank-market-investigative-research/
│       ├── SKILL.md                 # Agent entry point (token-optimized frontmatter)
│       ├── references/              # Progressive disclosure references
│       │   ├── bank-market-data.md
│       │   ├── funding-economics.md
│       │   ├── legal-and-compliance.md
│       │   ├── management-report.md
│       │   ├── source-evidence.md
│       │   └── sources-and-search.md
│       └── examples/                # Synthetic case templates
│           ├── case_brief.md
│           └── synthetic_funding_case.json
├── scripts/
│   ├── funding_economics.py         # Cost-of-funds calculator
│   ├── install.py                   # Zero-dependency multi-agent installer
│   └── validate_skill.py            # Spec compliance validator
├── tests/
│   └── test_funding.py              # Quantitative unit tests
├── docs/
│   ├── COMPATIBILITY.md
│   └── EVALUATION.md
├── AGENTS.md                        # Fallback instructions for LLMs
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE                          # MIT License
└── requirements.txt
```

---

## Quality and Limitations

This is a **research workflow**, not an automatic source of legal or regulatory authority. It cannot substitute for a formal legal opinion, primary bank deal records, or compliance approval. Historical case law and commercial provider statements do not prove current market volume.

---

## Validation

```bash
python scripts/validate_skill.py
python -m unittest discover -s tests -v
python scripts/funding_economics.py --input skills/bank-market-investigative-research/examples/synthetic_funding_case.json
```

---

## License

MIT License (c) 2026 Tuskul Kaigorodov. See [LICENSE](LICENSE) for details.
