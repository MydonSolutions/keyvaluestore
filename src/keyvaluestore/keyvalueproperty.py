from typing import Callable, Any


class KeyValueProperty:
    DefaultAccessor = object()

    def __init__(self,
        name: str,
        key: str,
        getter: Callable[[Any], Any] = DefaultAccessor, # always receives an instance of the class
        setter: Callable[[Any], Any] = DefaultAccessor, # always receives an instance of the class
        documentation: str = None,
    ):
        self.name = name

        if getter is KeyValueProperty.DefaultAccessor:
            assert key is not None, f"Cannot instantiate default getter without a key for '{name}'."
            getter = lambda self: self.get(key)

        if setter is KeyValueProperty.DefaultAccessor:
            assert key is not None, f"Cannot instantiate default setter without a key for '{name}'."
            setter = lambda self, value: self.set(key, value)
        
        self.getter = getter
        self.setter = setter
        self.documentation = documentation
