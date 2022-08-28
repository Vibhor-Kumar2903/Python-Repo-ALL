for num in range(11,51):
    print("Number {} ".format(num))
    if num == 15:
        break

print("\n")
for num in range(1,11):
    print("Number {} ".format(num))
    if num == 6:
        print("Number {} skipped ".format(num))
        continue

print("\n")
# print()
for num in range(21,26):
    if num == 23:
        pass
    else:
        print("Number {} ".format(num))
