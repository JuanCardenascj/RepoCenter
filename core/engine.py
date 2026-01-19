from typing import List, Dict, Any
from core.rule import Rule


class RuleEngine: #Yo entiendo el moto como la clase.....

    def __init__(self, rules: List[Rule]):
        self.rules = rules

    def run(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        results = []

        for rule in self.rules:
            try:
                missing_fields = [
                    field for field in rule.required_fields if field not in input_data
                ]
                if missing_fields:
                    result = {
                        "rule": rule.name,
                        "passed": False,
                        "reason": f"Faltan campos requeridos: {missing_fields}"
                    }
                else:
                    result = rule.evaluate(input_data)
                    if "rule" not in result:
                        result["rule"] = rule.name
                    if "passed" not in result:
                        result["passed"] = False
                    if "reason" not in result:
                        result["reason"] = ""
            except Exception as e:
                result = {
                    "rule": rule.name,
                    "passed": False,
                    "reason": f"Error al ejecutar la regla: {e}"
                }

            results.append(result)

        summary = {
            "passed": sum(1 for r in results if r["passed"]),
            "failed": sum(1 for r in results if not r["passed"])
        }

        return {"results": results, "summary": summary}
