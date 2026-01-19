import json
from core.registry import get_rule_class
from core.engine import RuleEngine

with open("config/rules.json", "r", encoding="utf-8") as f:
    config = json.load(f)

active_rule_names = config.get("active_rules", [])

rules = []
for name in active_rule_names:
    RuleClass = get_rule_class(name)
    rules.append(RuleClass())

engine = RuleEngine(rules)

input_data = {
    "age": 20,
    "score": 40,
    "country": "México"
}

result = engine.run(input_data)

print(json.dumps(result, indent=2, ensure_ascii=False))
