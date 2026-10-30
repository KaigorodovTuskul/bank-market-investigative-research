#!/usr/bin/env python3
"""Offline packaging and Agent Skills frontmatter smoke validation."""
from pathlib import Path
import re
root=Path(__file__).resolve().parents[1]
skill=root/'skills'/'bank-market-investigative-research'/'SKILL.md'
assert skill.is_file(), 'missing SKILL.md'
s=skill.read_text(encoding='utf8')
assert s.startswith('---\n') and '\n---\n' in s[4:], 'missing YAML frontmatter'
fm=s.split('---',2)[1]
for key in ('name:','description:','license:'):assert key in fm, f'missing {key}'
desc=next(x.removeprefix('description:').strip() for x in fm.splitlines() if x.startswith('description:'))
assert len(desc)<=250, f'description too long: {len(desc)}'
assert len(s.split())<850, 'Canonical skill too long; move details to references'
for link in re.findall(r'\]\((references/[^)]+)\)',s):
 assert (skill.parent/link).is_file(),f'missing reference {link}'
for f in ['README.md','AGENTS.md','LICENSE','scripts/funding_economics.py','tests/test_funding.py']:
 assert (root/f).is_file(),f'missing {f}'
print('PASS: skill manifest, progressive disclosure, repo structure')
