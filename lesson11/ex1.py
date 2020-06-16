strInput = ""
n = 2  # 10
for i in range(n):
    strInput += input("number: ")
    strInput += " "
print(strInput)
strArray = strInput.strip().split(' ')
print(max(strArray, key=lambda x: int(x)))



