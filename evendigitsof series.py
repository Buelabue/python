n=int(input("enter the number of even digit"))
if(isinstance(n,int)):
 for i in  range (0,n,2):

  if( i%2==0 and not i%3==0):
    print(i)
    for i in range(0,n,2):
        for j in range(1,n,2):
            print(i,j)