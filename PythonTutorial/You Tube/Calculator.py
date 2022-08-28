def addition():
    a = float(input("Enter the first number : "))
    b = float(input("Enter the second number : "))
    print(a+b)

def subtraction():
    a = float(input("Enter the first number : "))
    b = float(input("Enter the second number : "))
    print(a-b)

def multiplication():
    a = float(input("Enter the first number : "))
    b = float(input("Enter the second number : "))
    print(a*b)

def division():
    a = float(input("Enter the first number : "))
    b = float(input("Enter the second number : "))
    print(a/b)

operation = input("Please enter +, -, *, / : ")

if operation == '+' :
    addition()
elif operation == '-' :
    subtraction()
elif operation == '*':
    multiplication()
elif operation == '/' :
    division()
else:
    print(" opps!! wrong operation")
