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
        if kv_property.valueGetter is None:
            assert (
                kv_property.key is not None
            ), f"Cannot use default getter without a key for {kv_property.name}"
            getter = lambda self: self.get(kv_property.key)
        else:
            getter = kv_property.valueGetter

        if kv_property.valueSetter is None:
            assert (
                kv_property.key is not None
            ), f"Cannot use default setter without a key for {kv_property.name}"
            setter = lambda self, value: self.set(kv_property.key, value)
        elif kv_property.valueSetter is False:
            setter = None
        else:
            setter = kv_property.valueSetter

        setattr(
            recipient,
            kv_property.name,
            property(
                fget=getter,
                fset=setter,
                fdel=None,
                doc=kv_property.valueDocumentation,
            ),
        )


    @staticmethod
    def add_properties(
        recipient,  # obj.__class__
        properties: List[KeyValueProperty],
    ):
        for kv_property in properties:
            KeyValueStore.add_property(recipient, kv_property)
