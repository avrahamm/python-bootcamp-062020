def returns(arg_type):
    def decorator(f):
        def wrapped(func_arg):
            if type(func_arg) != arg_type:
                raise AssertionError(f"Expected {arg_type} argument but got {type(func_arg)}")

            return f(func_arg)

        return wrapped

    return decorator


@returns(str)
def same(word):
    return word


# works:
print(same('hello'))

# raise AssertionError:
# same(10)

try:
    same(10)
except AssertionError as e:
    print(e)


@returns(int)
def same2(num):
    return num


try:
    print(same2(10))
    print(same2('hello'))
except AssertionError as e:
    print(e)
