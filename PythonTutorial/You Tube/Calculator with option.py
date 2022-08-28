on = True

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

while on == True:
    operation = input("Please enter +, -, *, /, q (for quit) : ")

    if operation == '+' :
        addition()
    elif operation == '-' :
        subtraction()
    elif operation == '*':
        multiplication()
    elif operation == '/' :
        division()
    elif operation == 'q':
        on = False
    else:
        print(" opps!! wrong operation")
