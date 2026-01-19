from abc import ABC, abstractmethod
from typing import Dict, Any, List


class Rule(ABC):

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def required_fields(self) -> List[str]:
        pass

    @abstractmethod
    def evaluate(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        pass
