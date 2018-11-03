





print("program to simple interest")
principle=eval(input("enter the principle amount"))
time=eval(input("enter the time"))
rate=eval(input("enter the rate"))

if(not isinstance(principle,int)):
    print("errorin principle input")

if(rate==0):
    print("simple interest is zero")
else:
    simple_interest=(principle*time*rate)/100
    print(simple_interest)