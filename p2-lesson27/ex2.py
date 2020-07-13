import collections


def group_by(func, *args):
    dict = collections.defaultdict(list)
    for item in args:
        key = func(item)
        dict[key].append(item)
    return dict


# returns: { h: ['hello', 'hi', 'help', 'here'], b: ['bye'] }
print(group_by(lambda s: s[0], 'hello', 'hi', 'help', 'bye', 'here'))

# def filter_func(n):
#     return n % 5 == 0
#
#
# print(list(filter(lambda n: n % 5 == 0, range(2, 101))))
# print(list(filter(filter_func, range(2, 101))))
