import sys


def get_numbers_list_from_argsv():
    # You can just leave out the last value when you need the entire list
    input_list = sys.argv[1:]
    # Cool! Though personally I'd just return the list comprehension
    # return [int(n) for n in input_list]
    # => fixed
    return [int(n) for n in input_list]


def count_list_average(numbers_list):
    # Wait - where did "numbers" come from?
    # (yes I can see - it's defined below in the last part of the program
    #  but I hope you can see why using variables from outside your function is
    #  a bad practice. It's hard to spot them or to find bugs)
    # Better to pass numbers as an input argument to the function
    numbers_sum = sum(numbers_list)
    print(f"numbers_sum = {numbers_sum}")
    numbers_count = len(numbers_list)
    print(f"numbers_count = {numbers_count}")
    avg = (numbers_sum/numbers_count)
    print(f"avg = {avg}")
    return avg


numbers = get_numbers_list_from_argsv()
numbers_avg = count_list_average(numbers)
greater_than_avg = [num for num in numbers if num > numbers_avg]

print(f"greater_than_avg = {greater_than_avg}")

