def after5(f):
    counter = 0

    def wrapper():
        nonlocal counter
        if counter > 4:
            f()
        counter += 1

    return wrapper


@after5
def doit():
    print("Yo!")


# ignore the first 5 calls
doit()
doit()
doit()
doit()
doit()

# so only print yo once
doit()
