from random import randint
trials = 0
while True:
    number = randint(1, 1000000)
    trials += 1
    if number % 7 == 0 and number % 13 == 0 and number % 15 == 0:
        print(f"Found: {number}, trials: {trials}")
        break

    # Here's an alternative for those who like shorter lines :)
    if number % 7  != 0: continue
    if number % 13 != 0: continue
    if number % 15 != 0: continue
    break


