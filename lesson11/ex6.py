from random import randint

range_limit = 10  # 100
num = randint(1, range_limit)
trials = 0
guess = -1

while True:
    # I would prefer to write a function that reads stubbornly a numeric value
    # in range and call it from here
    # guess = read_numeric_value_in_range(1, range_limit)
    # (instead of writing the try/except here)
    try:
        guess = int(input(f"Guess number in range [1,{range_limit}]: "))
    except Exception:
        continue

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
