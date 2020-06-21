import sys


def get_numbers_list_from_argsv():
    input_list = sys.argv[1:len(sys.argv)]
    numbers_list = [int(n) for n in input_list]
    return numbers_list


def count_list_average():
    numbers_sum = sum(numbers)
    print(f"numbers_sum = {numbers_sum}")
    numbers_count = len(numbers)
    print(f"numbers_count = {numbers_count}")
    avg = (numbers_sum/numbers_count)
    print(f"avg = {avg}")
    return avg


numbers = get_numbers_list_from_argsv()
numbers_avg = count_list_average()
greater_than_avg = [num for num in numbers if num > numbers_avg]

print(f"greater_than_avg = {greater_than_avg}")

