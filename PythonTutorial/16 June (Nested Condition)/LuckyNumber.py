print('Enter a number : ')
num = int(input())

str_num = str(num)
first_digit = str_num[0] == 9
second_digit = str_num[1] == 9

condition1 = num%9==0
condition2 = first_digit or second_digit

if (condition1 or condition2):
    print("You got a LUCKY NUMBER**")
else:
    print("Better luck next time!!")



