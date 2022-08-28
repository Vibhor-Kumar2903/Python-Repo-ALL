# Masking
print("Enter a string : ")
word = input()
first_char = word[0]
length = len(word)
last_char = word[length-1]

no_of_star = length-2
star = (no_of_star) * ("*")

print(first_char + star + last_char)
