print("This is the output for Single line comment")

print("Enter a Number: ")

# input() converts entered value into string, by default
a = input()

print("Enter another Number: ")
b = input()

# int() converts string to integer
a = int(a)
b = int(b)

sum = a+b

print("\nSum =", sum)

print('This is the Output for MultiLine Comment')


print("Enter a Number: ")

''' The input() converts the entered value into string, by default.
    So when user enters 12 as input, it gets treated as string.
    That is, a = "12"
'''
a = input()

print("Enter another Number: ")
b = input()

''' Since a = "12", so adding both numbers say a and b
    gives "12" + "34". That is, "1234".
    If user enters 34 as second number.
'''
print("\nSum = ", a+b)

''' The int() converts string to integer.
    So int(a) or int("12") returns 12.
    Similarly, int(b) or int("34") gives 34.
'''
a = int(a)
b = int(b)

sum = a+b
print("\nSum =", sum)

""" Since first parameter of print() above is of 
    string type. Therefore second string must has 
    to be of string type to concatenate using +
    like shown below.
    The str() converts any type into string type
"""
print("\nSum = " + str(sum))
