def mymul(*args):
    mul = 1
    for item in args:
        try:
            mul *= int(item)
        except Exception:
            continue
    return mul


# returns 200:
print(mymul('foo', 'bar', 10, 20))

# returns 1:
print(mymul())

# returns 7:
print(mymul(7))
