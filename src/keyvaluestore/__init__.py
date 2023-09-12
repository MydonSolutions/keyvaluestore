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
        raise NotImplementedError

    def __hash__(self):
        raise NotImplementedError

    def get(self, key, fallback = None):
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
