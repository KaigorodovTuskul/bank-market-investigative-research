# Compatibility

- **Canonical path:** `skills/bank-market-investigative-research/SKILL.md`.
- **Progressive disclosure:** load the frontmatter/short skill first; references only when the task needs them.
- `AGENTS.md` is a small fallback for CLIs with no Agent Skills discovery.
- Optional tools: general web search; GitHub for supplied repositories; browser extraction; Python for deterministic computations; Word renderer for final layout.
- Tool names and permissions vary by product. An agent must discover what is connected and should never claim use of tools unavailable in its session.
- No background tasks unless the runtime explicitly supports scheduling.
