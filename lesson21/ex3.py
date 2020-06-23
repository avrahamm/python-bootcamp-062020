class Widget:
    def __init__(self, name):
        self._name = name
        # A small naming suggestion - 
        # I'd use something like _built or _done
        # instead of _status
        # (because _status can be many things and does not imply boolean)
        self._status = False
        self._children = []

    def add_dependency(self, *args):
        # You don't need to convert to list...
        self._children += list(args)

    def build(self):
        for child in self._children:
            child.build()

        if not self._status:
            print(self._name, end=", ")
            self._status = True


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
