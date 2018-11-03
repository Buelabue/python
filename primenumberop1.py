
num=int(input("enter the positive number to check whether it is prime or not"))
if num >1:

 for i in range(2,num):
    if (num%i)==0:
     print(num," is not a prime number")
    break

else:
    print(num,"is a prime number")

print(num,"is not a prime number")




