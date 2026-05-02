#!/usr/bin/env python3
from pathlib import Path
import re, sys

root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parents[2]
refs_dir = root / 'coding-common' / 'references'
errors = []

MAX_SKILLS = 24
MAX_REFS = 30
MAX_SKILL_LINES = 120
MAX_REFS_PER_SKILL = 8
MAX_TOTAL_MD_WORDS = 9000

required_refs = {
    'all': {'workflow-contract.md'},
    'edit': {'surgical-change-policy.md'},
    'security': {'security-boundaries.md'},
    'handoff': {'coding-agent-handoff.md'},
}
edit_skills = {'coding-implementation', 'dev-bootstrap-repair'}
security_skills = {'security-review-gate', 'security-attacker-validation'}
handoff_skills = {'coding-implementation', 'dev-bootstrap-repair', 'engineering-fix-orchestrator', 'code-review-gate', 'repro-pack-builder'}
proof_terms = ('proof', 'verification', 'verify', 'gate')


def parse_frontmatter(text, skill_name):
    if not text.startswith('---\n'):
        errors.append(f'{skill_name}/SKILL.md missing frontmatter')
        return {}
    parts = text.split('---\n', 2)
    if len(parts) < 3:
        errors.append(f'{skill_name}/SKILL.md malformed frontmatter')
        return {}
    data = {}
    for line in parts[1].splitlines():
        if ':' not in line:
            errors.append(f'{skill_name}/SKILL.md invalid frontmatter line: {line}')
            continue
        key, value = line.split(':', 1)
        data[key.strip()] = value.strip().strip('"')
    return data

skill_dirs = []
for child in sorted(root.iterdir()):
    if not child.is_dir() or child.name.startswith('.'):
        continue
    if child.name == 'coding-common':
        if (child / 'SKILL.md').exists():
            errors.append('coding-common must not contain SKILL.md')
        continue
    if (child / 'SKILL.md').exists():
        skill_dirs.append(child)
    else:
        errors.append(f'{child.name}/ missing SKILL.md')

if not skill_dirs:
    errors.append('no installable skills found')
if len(skill_dirs) > MAX_SKILLS:
    errors.append(f'too many skills: {len(skill_dirs)} > {MAX_SKILLS}')

all_refs = sorted(refs_dir.glob('*.md'))
if len(all_refs) > MAX_REFS:
    errors.append(f'too many references: {len(all_refs)} > {MAX_REFS}')

for skill in skill_dirs:
    path = skill / 'SKILL.md'
    text = path.read_text()
    lower = text.lower()
    lines = text.splitlines()
    fm = parse_frontmatter(text, skill.name)
    if fm.get('name') != skill.name:
        errors.append(f'{skill.name}/SKILL.md name mismatch')
    if not fm.get('description'):
        errors.append(f'{skill.name}/SKILL.md missing non-empty description')
    if len(lines) > MAX_SKILL_LINES:
        errors.append(f'{skill.name}/SKILL.md too long: {len(lines)} lines')
    if 'read first:' not in lower:
        errors.append(f'{skill.name}/SKILL.md missing Read first section')
    if 'workflow:' not in lower:
        errors.append(f'{skill.name}/SKILL.md missing Workflow section')
    if not any(term in lower for term in proof_terms):
        errors.append(f'{skill.name}/SKILL.md missing proof/verification wording')

    refs = set(re.findall(r'`\.\./coding-common/references/([^`]+\.md)`', text))
    if len(refs) > MAX_REFS_PER_SKILL:
        errors.append(f'{skill.name}/SKILL.md references too many refs: {len(refs)} > {MAX_REFS_PER_SKILL}')
    for ref in refs:
        if not (refs_dir / ref).exists():
            errors.append(f'{skill.name} references missing {ref}')

    expected = set(required_refs['all'])
    if skill.name in edit_skills:
        expected |= required_refs['edit']
    if skill.name in security_skills:
        expected |= required_refs['security']
    if skill.name in handoff_skills:
        expected |= required_refs['handoff']
    for ref in sorted(expected):
        if ref not in refs:
            errors.append(f'{skill.name} missing required safety/workflow ref {ref}')

    # Resolve Markdown references that look like local .md files.
    for md in re.findall(r'(?<![\w/-])([A-Za-z0-9_-]+\.md)', text):
        if md in refs:
            continue
        if not (refs_dir / md).exists() and not (skill / md).exists():
            errors.append(f'{skill.name}/SKILL.md has unresolved markdown reference {md}')

for ref in all_refs:
    text = ref.read_text()
    if not text.strip():
        errors.append(f'empty reference: {ref.name}')
    if not text.lstrip().startswith('#'):
        errors.append(f'{ref.name} missing top-level heading')


orch = refs_dir / 'orchestrator-workflows.md'
if orch.exists():
    orch_text = orch.read_text()
    for term in ['Browser-visible bug to fix','Design handoff to React implementation','Contract drift across backend/frontend','Migration/backend/frontend coordinated change','Review-only coding work','Coding handoff package','Gate proof rule','Degraded complete output']:
        if term not in orch_text:
            errors.append(f'orchestrator-workflows.md missing sentinel {term}')
else:
    errors.append('missing orchestrator-workflows.md')

word_count = sum(len(p.read_text(errors='ignore').split()) for p in root.rglob('*.md') if '.git' not in p.parts)
if word_count > MAX_TOTAL_MD_WORDS:
    errors.append(f'total markdown word count too high: {word_count} > {MAX_TOTAL_MD_WORDS}')

if errors:
    print('FAIL')
    for e in errors:
        print('-', e)
    sys.exit(1)
print(f'OK: {len(skill_dirs)} skills, {len(all_refs)} references, {word_count} markdown words')
