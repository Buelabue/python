n=eval(input("enter the ending number to add for natural numbers"))
if(not isinstance(n,int)):
    print("wrong input")



else:
 if(n>0):
     sum=(n*(n+1))/2
     print("sum of natural number is",sum)


 else:
     print("error!!!")



