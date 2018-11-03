n=eval(input("enter the number"))
mul=eval(input("enter the mul"))

if not(n<50 or n%mul==0):
    print("the n",n, "is a multiple of number",mul)

else:
    print("the n", n," is not a multiple of number",mul,"or the number is greater than 50")