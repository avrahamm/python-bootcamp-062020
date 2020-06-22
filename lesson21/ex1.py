class Summer:
    def __init__(self):
        self._total = 0

    def add(self, *args):
        self._total += sum(list(args))

    def print_total(self):
        print(self._total)


s = Summer()
t = Summer()

s.add(10, 20)
t.add(50)
s.add(30)

# should print 60
s.print_total()

# should print 50
t.print_total()
