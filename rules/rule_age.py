from typing import Dict, Any, List
from core.rule import Rule

class AgeRule(Rule):

    @property
    def name(self) -> str:
        return "age"

    @property
    def required_fields(self) -> List[str]:
        return ["age"]

    def evaluate(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        age = input_data.get("age", 0)
        if age >= 18:
            return {"rule": self.name, "passed": True, "reason": "Edad suficiente"}
        else:
            return {"rule": self.name, "passed": False, "reason": "Menor de edad"}
