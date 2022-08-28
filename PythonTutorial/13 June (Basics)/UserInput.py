var1 = 20
print("Enter a number : ")
num = input()   # here num is store in the form of string not integer
print("Given value is :",num)

#print("Given value is :",num+10)    # it will throw error because you are adding integer and string

print("Given value is :",int(num)+10)   # data type casting

print("Given value is :",int(num)+var1)