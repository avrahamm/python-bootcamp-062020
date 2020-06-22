class Widget:
    def __init__(self, name):
        self.name = name
        self.status = False
        self.children = []

    def add_dependency(self, *args):
        self.children += list(args)

    def build(self):
        for child in self.children:
            child.build()

        if not self.status:
            print(self.name, end=", ")
            self.status = True


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
