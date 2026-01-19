from typing import Type
from core.rule import Rule
from rules.rule_age import AgeRule
from rules.rule_score import ScoreRule
from rules.rule_country import CountryRule

RULE_REGISTRY: dict[str, Type[Rule]] = {
    "age": AgeRule,
    "score": ScoreRule,
    "country": CountryRule
}


def get_rule_class(rule_name: str) -> Type[Rule]:
    if rule_name not in RULE_REGISTRY:
        raise ValueError(f"La regla '{rule_name}' no está registrada.")
    return RULE_REGISTRY[rule_name]
