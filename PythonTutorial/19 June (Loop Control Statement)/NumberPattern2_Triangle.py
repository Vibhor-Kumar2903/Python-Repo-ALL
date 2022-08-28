print("Enter the number of rows :: ")
row = int(input())

for i in range(0, row):
    row_output = ""
    col = row - i

    while col > 0:
        row_output = row_output + str(col) + " "
        col = col - 1
    print(row_output)
