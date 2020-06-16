numStr = input("Enter a number: ")

# So this works but actually I'm not sure you need two variables
# For example this version has one less variable
# and IMHO it's even more readable
# (but of course it's a matter of taste)
if '7' in numStr or int(numStr) % 7 == 0:
    print('Boom')

print('End')
