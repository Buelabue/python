n=eval(input("enter the number"))
if(not isinstance(n,int)):
    print("wrong input")
else:
    if(n>7):
        if(n%7==0):
            print("n of multiple numbers of 7")
        else:
            print("Not Divisible")
