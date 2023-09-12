from typing import List

from .keyvalueproperty import KeyValueProperty

class KeyValueStore:
    """
    This class indicates the logic related to accessing
    key-values. The static methods `add_property` and
    `add_properties` are instrumental to the goal of the
    package.
    """

    def __str__(self):
        return f"""{self.__class__}: {({
            attr: getattr(self, attr)
            for attr in dir(self.__class__)
            if isinstance(getattr(self.__class__, attr), property)
        })}"""

    def get(self, key, default = None):
        raise NotImplementedError

    def set(self, key, values):
        raise NotImplementedError

    @staticmethod
    def add_property(
        recipient, # obj.__class__
        kv_property: KeyValueProperty
    ):
        setattr(
            recipient,
            kv_property.name,
            property(
                fget=kv_property.getter,
                fset=kv_property.setter,
                fdel=None,
                doc=kv_property.documentation,
            ),
        )

    @staticmethod
    def add_properties(
        recipient,  # obj.__class__
        properties: List[KeyValueProperty],
    ):
        for kv_property in properties:
            KeyValueStore.add_property(recipient, kv_property)
