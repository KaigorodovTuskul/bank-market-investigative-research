# Source and claim discipline

## Hierarchy

A: regulator, statutory text, official statistics, court original, executed contract, bank audited filing.
B: reliable professional reproduction of a court document, rating agency, primary reporter with traceable sources.
C: marketing page, product catalogue, interview or commentary.
D: rumor, unsupported inference, unverified third-party repost.

Classification is about provenance, not truth. Note status, date, exact passage and caveat for each decision-relevant claim. Court texts must distinguish (i) allegations of parties, (ii) established circumstances, (iii) operative ruling. Historical fact does not validate modern law.

## Minimum ledger

`source_id, publisher, title, original_url, document_date, observation_date, accessed_at, source_class, passage, limitation, access_status`.

Claim ledger: `claim_id, statement, source_ids, evidence_type, confidence, contradicted_by, unresolved_dependency`.

No invented citations. If an original fails to open, retry via another access mechanism; identify the mirror as a retrieval aid, not independent corroboration. A second site reproducing the same court judgment is not a second independent observation.

## Negative evidence

Maintain a compact search-events log when claiming no modern cases found: `date, query, language, source, hits, screened, retained, exclusion_reason`. Never write "the market does not exist" solely because no public disclosure was found.
