# without type conversion
a = 10
b = 20
result1 = a+b
print(result1)

# without type conversion and user input
print("Enter first number :: ")
a = input()
print("Enter second number :: ")
b = input()
result2 = a + b     # result will be in string form
print(result2)

# with type conversion and user input
print("Enter first number :: ")
a = input()
a = int(a)      # type conversion from string to integer
print("Enter second number :: ")
b = input()
b = int(b)      # type conversion from string to integer
result2 = a + b     # result will be in integer form
print(result2)
