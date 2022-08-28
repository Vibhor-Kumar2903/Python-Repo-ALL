print('Enter first number : ')
num1 = int(input())
print('Enter second number : ')
num2 = int(input())
print('Enter third number : ')
num3 = int(input())

if ((num1>num2) and (num1>num3)):
    print("First number is greatest : "+str(num1))
else:
    if (num2>num3):
        print("Second number is greatest : "+str(num2))
    else:
        print("Third number is greatest : "+str(num3))






