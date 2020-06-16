from random import randint


def find_greatest_common_divisor(a, b):
    """
    Simplified version of gcd in assumption numbers are in range [1,10]
    :param a:int
    :param b:int
    :return: int
    """
    # same numbers
    if a == b:
        return a
    # numbers are not same
    bigger_num = max(a, b)
    smaller_num = min(a, b)

    if bigger_num % smaller_num == 0:
        return smaller_num

    divider = smaller_num
    while divider > 1:
        if bigger_num % divider == 0 and smaller_num % divider == 0:
            return divider
        else:
            divider -= 1

    return 1


def find_least_common_multiple(a, b):
    """
    According to algorithm from
    @link: https://he.wikipedia.org/wiki/%D7%9B%D7%A4%D7%95%D7%9C%D7%94_%D7%9E%D7%A9%D7%95%D7%AA%D7%A4%D7%AA_%D7%9E%D7%99%D7%A0%D7%99%D7%9E%D7%9C%D7%99%D7%AA
    :param a: int
    :param b: int
    :return: int
    """
    gcd = find_greatest_common_divisor(a, b)
    lcm = (a * b) / gcd
    return lcm


num1 = randint(1, 10)
num2 = randint(1, 10)

lcm_result = find_least_common_multiple(num1, num2)
print(f"num1 = {num1}, num2 = {num2}, lcm = {lcm_result}")

