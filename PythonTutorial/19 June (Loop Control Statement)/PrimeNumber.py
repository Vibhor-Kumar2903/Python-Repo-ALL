print("Enter a digit :: ")
digit = int(input())
factor = 0;

for i in range(2,digit): # Last index is not included (so it is ranging up-to [digit-1])
    if (digit%i == 0):
        factor = factor + 1

if (factor == 0):
    print("Given digit is a PRIME NUMBER")
else:
    print("Given digit is not a PRIME NUMBER")