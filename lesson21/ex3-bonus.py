"""
Registry Design pattern is used to assure Widget with specific "name"
is created only once.
As in base version, each Widget is built/printed only once.
"""


class Widget:
    """
    Dictionary is used to implement registry - not singleton!
    ynonp06/25/2020 noted:
    קלעת בול עם התרגיל בונוס
    רק התבנית נקראת Registry ולא Singleton
    https://martinfowler.com/eaaCatalog/registry.html
    """
    # TODO! consider to delegate to external Registry object
    registry = {}

    def __init__(self, name):
        self._name = name
        # A small naming suggestion -
        # I'd use something like _built or _done
        # instead of _status
        # (because _status can be many things and does not imply boolean)
        #
        # => changed to _built
        self._built = False
        self._children = []
        Widget.registry[name] = self

    @staticmethod
    def get_instance(name):
        try:
            return Widget.registry[name]
        except KeyError:
            instance = Widget(name)
            Widget.registry[name] = instance
            return instance

    def add_dependency(self, *args):
        # You don't need to convert to list...
        # self._children += list(args)
        #
        # => yet this will not work:
        # self._children = self._children + args
        # and with converted list(args) will:
        # self._children = self._children + list(args)
        for name in args:
            instance = Widget.get_instance(name)
            self._children.append(instance)

    def build(self):
        # Ynon noted it is better to check first
        # to avoid "empty" recursive call even does nothing
        if not self._built:
            self._built = True

            for child in self._children:
                child.build()

            print(self._name, end=", ")


leia = Widget("Leia")
leia.add_dependency("Padme Amidala", "Anakin Skywalker")

luke = Widget("Luke")
luke.add_dependency("Han Solo", "Yoda")

obi = Widget("Obi-Wan")
obi.add_dependency("Yoda")

darth = Widget("Darth Vader")
darth.add_dependency("Anakin Skywalker")

_all = Widget("All")
_all.add_dependency("Han Solo", "Yoda", "Padme Amidala", "Anakin Skywalker")

leia.build()
print()

luke.build()
print()

obi.build()
print()

darth.build()
print()

_all.build()
