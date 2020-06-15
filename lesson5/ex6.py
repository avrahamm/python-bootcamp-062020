print("Arithmetic progression!")
first = int(input("Enter first : "))
d = int(input("Enter d: "))
n = int(input("Enter n: "))

last = first + (n-1)*d

progressionSum = (n * (first + last)) / 2

print(f'Arithmetic progression sum = {progressionSum}')
print('End')
