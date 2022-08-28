print("Enter a number :: ")
num = int(input())

for i in range(num):
    if i == 2:
        pass
        # pass is to skip the iteration at i==2
    print("loop executed")

print("End")

for i in range(num):
    pass
    # It will work for for loop also
print("End")