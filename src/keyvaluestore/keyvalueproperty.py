from dataclasses import dataclass
from typing import Callable, Any

@dataclass
class KeyValueProperty:
    name: str
    key: str
    valueGetter: Callable[[Any], Any] # always receives the instance of the class
    valueSetter: Callable[[Any], Any] # always receives the instance of the class
    valueDocumentation: str = None
