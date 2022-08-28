print("A" > "a")    # False
print("a" > "A")    # True

print("0" > "9")    # False
print("9" > "0")    # True

print("$" > "@")    # False

print("?" > " ")    # True
print(" " > "?")    # False

# Python compare the string, character by character
print("chr" > "str")    # False
print("str" > "chr")    # True

print("BAD" > "BAT")    # False
print("BAT" > "BAD")    # True
print("BDD" > "BAT")    # True

print("98" > "101")    # True
print("098" > "101")    # False



