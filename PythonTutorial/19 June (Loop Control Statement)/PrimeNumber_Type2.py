print("Enter a number :: ")
num = int(input())
is_prime = True

for i in range(2,num):
    if(num%i==0):
        is_prime = False


print("Above number is prime ===>>> "+str(is_prime))
