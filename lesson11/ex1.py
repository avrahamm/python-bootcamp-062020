strInput = ""
n = 2  # 10
for i in range(n):
    strInput += input("number: ")
    strInput += " "
print(strInput)
strArray = strInput.strip().split(' ')
"""
using key=lambda anonymous function
@link: https://stackoverflow.com/questions/18296755/python-max-function-using-key-and-lambda-expression
"""
print(max(strArray, key=lambda x: int(x)))



