from typing import Dict, Any, List
from core.rule import Rule

class ScoreRule(Rule):

    @property
    def name(self) -> str:
        return "score"

    @property
    def required_fields(self) -> List[str]:
        return ["score"]

    def evaluate(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        score = input_data.get("score", 0)
        if score >= 50:
            return {"rule": self.name, "passed": True, "reason": "Puntaje suficiente"}
        else:
            return {"rule": self.name, "passed": False, "reason": "Puntaje insuficiente"}
