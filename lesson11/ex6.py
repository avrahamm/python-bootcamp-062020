from random import randint


def read_numeric_value_in_range(range_bottom, range_top):
    while True:
        try:
            guess_num = int(input(f"Guess number in range [{range_bottom}, {range_top}]: "))
            if guess_num not in range(range_bottom, range_top):
                continue
            return guess_num
        except Exception:
            continue


range_limit = 11  # 101
num = randint(1, range_limit)
trials = 0
guess = -1


# I would prefer to write a function that reads stubbornly a numeric value
# in range and call it from here
# guess = read_numeric_value_in_range(1, range_limit)
# (instead of writing the try/except here)
#
# => Fixed
while True:
    guess = read_numeric_value_in_range(1, range_limit )
    trials += 1
    if guess == num:
        print(f"You won! The number is {num}, trials = {trials}")
        break
    elif trials % 3 == 0:
        print("Greater :-)")
    elif guess < num:
        print("Smaller")
    else:
        print("Greater")
