import itertools


def uniq(seq):
    uniq_set = set()
    while True:
        try:
            seq_val = next(seq)
            # print('checking')
            if seq_val not in uniq_set:
                uniq_set.add(seq_val)
                yield seq_val
        except StopIteration:
            break


l1 = [1, 2, 3, 2, 3, 4, 5]
it1 = (n for n in l1)
tens = itertools.repeat(10, 4)
it1 = tens

u = uniq(it1)

while True:
    try:
        val = next(u)
        if val > 100:
            break
        print(val)
    except StopIteration:
        break
