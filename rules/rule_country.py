from typing import Dict, Any, List
from core.rule import Rule

class CountryRule(Rule):

    @property
    def name(self) -> str:
        return "country"

    @property
    def required_fields(self) -> List[str]:
        return ["country"]

    def evaluate(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        country = input_data.get("country", "").lower()
        allowed_countries = ["mexico", "colombia", "argentina"]
        if country in allowed_countries:
            return {"rule": self.name, "passed": True, "reason": "País permitido"}
        else:
            return {"rule": self.name, "passed": False, "reason": "País no permitido"}
