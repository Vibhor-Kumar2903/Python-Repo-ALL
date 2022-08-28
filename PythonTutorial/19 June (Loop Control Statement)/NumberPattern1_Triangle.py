print("Enter the number of row :: ")
row = int(input())

for i in range(1, row+1):
    print_row = ""
    for j in range(1, i+1):
        print_row = print_row + str(j) + " "
    print(print_row)