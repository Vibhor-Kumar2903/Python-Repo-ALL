#
print("Enter a digit : ")
a = int(input())

str_a = str(a)

first_digit = int(str_a[0])
second_digit = int(str_a[1])

if ((first_digit>second_digit) and (a>25)):
    print('Valid solution')
else:
    print('Invalid solution')