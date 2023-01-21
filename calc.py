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
    num1 = int(input("Enter first number: "))
    choice = input("Enter choice '+','-','*' or '/': ")
    num2 = int(input("Enter second number: "))
    if choice == '+':
        print(num1,"+",num2,"=",add(num1, num2))
    elif choice == '-':
        print(num1,"-",num2,"=",subtract(num1, num2))
    elif choice == '*':
        print(num1,"*",num2,"=",multiply(num1, num2))
    elif choice == '/':
        print(num1,"/",num2,"=",divide(num1, num2))
    else:
        print("wrong input")
        calc = False