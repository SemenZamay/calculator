import sys

num1 = int(sys.argv[1])
choice = sys.argv[2]
num2 = int(sys.argv[3]) # if I multiply it is error: invalid literal for int() or it is "wrong input"

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

calc = True
while calc == True:
    if choice == '+':
        print(int(add(num1, num2)))
        calc = False
    elif choice == '-':
        print(int(subtract(num1, num2)))
        calc = False
    elif choice == '*':
        print(multiply(num1, num2))
        calc = False
    elif choice == '/':
        print(int(divide(num1, num2)))
        calc = False
    else:
        print("wrong input")
        calc = False