user_credentials = {
    'apple': 'red',
    'lettuce': 'green',
    'lemon': 'yellow',
    'orange': 'orange',
}

name = input('Please enter your name: ')
password = input('Please enter your password: ')

print(name, password)

try:
    if user_credentials[name] == password:
        print("Welcome Master")
except KeyError:
    print("INTRUDER ALERT")
