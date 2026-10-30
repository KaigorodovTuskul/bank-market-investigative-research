# Bank market data boundary

A **stock** is outstanding amount as of date. A **flow/turnover** is transactions over interval; mean daily turnover differs from summed monthly volume. Never add or directly compare these as one numerator.

| Source | Appropriate use | Caution |
|---|---|---|
| CBR Form 0409101 | Per-bank first-order balance accounts | 2026 public 320+321 and 313+314 aggregated; no overnight tenor breakdown |
| CBR Form 0409501 | Interbank loan/deposit reporting for a specific bank | Not public bank-by-bank agent attribution; permission required for internal records |
| CBR deposits at CBR | Day-start bank deposits in central bank | Not lending to private bank; missing published cells do not equal zero |
| CBR money-market turnover | Repo/MBK average daily volume | Not specifically the banking sector's net placement |
| RUONIA | Sample of overnight unsecured interbank deals | Not all overnight transactions |
| CBR REPO operations | CBR lending liquidity to banks when it supplies funds | Opposite cash direction from deposits at CBR |
| BIS LBS | Cross-border banking claims/liabilities | Coverage/country bases differ from Russian external debt |

For Form 101, the **2026 public disclosure** is constrained by the Bank of Russia Board decision of 19 Dec 2025: https://www.cbr.ru/rbr/dir_decisions/rsd_2025-12-19_23_02/. Always recheck for the relevant period.

If working with parsed CSV and code: verify units, first-order aggregation, active/passive balance, each bank's ID, duplicate rows, population coverage, missing data versus zero and common periods. If comparing Jan-Sep to full year, compute Jan-Sep for all years. If a result is a **simple mean of monthly means**, call it that and avoid calling it trading-day-weighted annual average.
