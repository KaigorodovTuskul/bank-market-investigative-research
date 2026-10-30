# Evaluation protocol (proposed, not yet run)

Test against a varied banking research task set: bank funding intermediaries, deposit market liquidity, CBR 101 limitations, cross-border borrowings, and court-case provenance.

1. Prepare identical source-access configurations for baseline and skill-assisted agent.
2. Judge blindly on factual accuracy, decision usefulness, court holdings vs allegations, dated legal editions, calculation correctness, source coverage and executive presentation.
3. Hard failures: invented court cases, invented tariffs, stock/flow conflation, unmarked synthetic quotes, fabricated official data, missing mandatory source URLs.
4. Measure response tokens and run time only where outputs pass the quality gate. Publish negative and neutral outcomes.
5. Existing tests exercise arithmetic and repository structure only; **there is no validated performance or token-savings claim**.
