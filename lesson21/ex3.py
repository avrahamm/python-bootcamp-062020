class Widget:
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

    def add_dependency(self, *args):
        # You don't need to convert to list...
        # self._children += list(args)
        #
        # => yet this will not work:
        # self._children = self._children + args
        # and with converted list(args) will:
        # self._children = self._children + list(args)
        #
        # => Ynon explained that l1 += t1 is not equivalent to l1 = l1 +t1
        # as l1 += t1 uses l1.extend function can get any type of argument.
        # So no need to explicitly convert to list in the case.
        self._children += args

    def build(self):
        # Ynon noted it is better to check first
        # to avoid "empty" recursive call even does nothing
        if not self._built:
            self._built = True

            for child in self._children:
                child.build()

            print(self._name, end=", ")


padme = Widget("Padme Amidala")  # leila, _all
anakin = Widget("Anakin Skywalker")  # leila, darth, _all
leia = Widget("Leia")
leia.add_dependency(padme, anakin)  # _all

hansolo = Widget("Han Solo")  # luke, _all,
yoda = Widget("Yoda")  # luke, obi, _all
luke = Widget("Luke")
luke.add_dependency(hansolo, leia, yoda)  # _all

obi = Widget("Obi-Wan")
obi.add_dependency(yoda)  # _all

darth = Widget("Darth Vader")
darth.add_dependency(anakin)  # _all

_all = Widget("All")
_all.add_dependency(luke, hansolo, leia, yoda, padme, anakin, obi, darth)

# leia.build()
# print()
_all.build()
# code should print: Han Solo, Padme Amidala, Anakin Skywalker, Leia, Yoda, Luke, Obi-Wan, Darth Vader
# (can print with newlines in between modules)
