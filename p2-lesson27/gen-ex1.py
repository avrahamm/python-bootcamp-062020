def squares():
    x = 1
    while True:
        yield x*x
        x += 1


for index, val in enumerate(squares()):
    if index >= 10:
        break
    print(index, val)

s = squares()

for index in range(10):
    if index >= 10:
        break
    print(next(s))
