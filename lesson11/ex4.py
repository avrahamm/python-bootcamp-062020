from random import randint
trials = 0
while True:
    number = randint(1, 1000000)
    trials += 1
    if number % 7 == 0 and number % 13 == 0 and number % 15 == 0:
        print(f"Found: {number}, trials: {trials}")
        break
