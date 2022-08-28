print("Enter a sentence :: ")
str = input() # Python is a programming language.

first_space_index = 0

for char in str:
    if char == " ":
        break
    else:
        first_space_index = first_space_index + 1

first_word = str[:first_space_index]

first_word_upper = first_word.upper()

new_str = first_word_upper + str[first_space_index:]

print(new_str)