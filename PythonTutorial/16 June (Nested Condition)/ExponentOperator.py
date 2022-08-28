# ** is the exponent operator
print('Enter the base number :: ')
a = int(input())
print('Enter the exponential number :: ')
b = int(input())
result1 = a**b      # (^) this symbol is not working here for exponential representation
result2 = b**a

if (result1>result2):
    print('a_power_b is greater')
    print(result1)
else:
    print('b_power_a is greater')
    print(result2)
