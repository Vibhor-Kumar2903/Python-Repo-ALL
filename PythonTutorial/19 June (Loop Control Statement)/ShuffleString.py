print("Enter a string :: ")
str = input()

shuffle_str = ""

for i in range(len(str)):
    index = int(input())
    shuffle_str = shuffle_str + str[index]

print(shuffle_str)