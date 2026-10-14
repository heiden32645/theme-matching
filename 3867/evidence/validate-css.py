from pathlib import Path
import json
import re
import sys

sys.path.insert(0, 'C:/Users/haida/AppData/Local/Temp/snazzy-css-python')
import tinycss2

source = Path('3867/1.6.0.css').read_text(encoding='utf-8')
errors = []
selectors = []

def inspect(rules):
    for rule in rules:
        if rule.type == 'error':
            errors.append(str(rule))
        elif rule.type == 'at-rule' and rule.content is not None:
            inspect(tinycss2.parse_rule_list(rule.content, skip_comments=True, skip_whitespace=True))
        elif rule.type == 'qualified-rule':
            selectors.append(tinycss2.serialize(rule.prelude).strip())
            for declaration in tinycss2.parse_declaration_list(rule.content, skip_comments=True, skip_whitespace=True):
                if declaration.type != 'declaration':
                    errors.append(str(declaration))

inspect(tinycss2.parse_stylesheet(source, skip_comments=True, skip_whitespace=True))
defined = set(re.findall(r'(--gpo-theme-[\w-]+)\s*:', source))
used = set(re.findall(r'var\((--gpo-theme-[\w-]+)', source))
result = dict(file='3867/1.6.0.css', rules=len(selectors), errors=errors,
              unused_tokens=sorted(defined-used), undefined_tokens=sorted(used-defined),
              all_selectors_scoped=all('.gpo-app' in selector for selector in selectors))
Path('3867/evidence/syntax-validation.json').write_text(json.dumps(result, indent=2))
print(json.dumps(result))
assert not errors and defined == used and result['all_selectors_scoped']
