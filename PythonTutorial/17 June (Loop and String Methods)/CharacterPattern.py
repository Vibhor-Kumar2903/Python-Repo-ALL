print('Enter a string : ')
str = input()
l = len(str)
char_str = str[0]

for i in range(1,l):
    char_str = char_str + '-' + str[i]

print(char_str)