def memoize(f):
    fibs_registry = {}

    def wrapper(n):
        try:
            return fibs_registry[n]
        except Exception:
            fibs_registry[n] = f(n)
            return fibs_registry[n]

    return wrapper


@memoize
def fib(n):
    print("fib(%d)" % n)
    if n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(10))
