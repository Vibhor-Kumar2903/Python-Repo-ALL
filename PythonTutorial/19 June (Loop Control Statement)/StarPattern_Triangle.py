row = int(input())
spc = row-1

for i in range(1, row+1):
    space = " " * spc
    star = "* " * i
    print(space + star)
    spc = spc-1
