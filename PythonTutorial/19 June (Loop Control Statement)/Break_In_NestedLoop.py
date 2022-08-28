for i in range(2):
    print("Outer :: "+str(i))

    for j in range(4):
        if j == 2:
            break
        print("    input :: "+str(j))