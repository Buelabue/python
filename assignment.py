def main():
    mylist = []
    while (True):
        print("push1")
        print("pop2")
        print("display3")
        print("exit4")
        eva = eval(input("enter ur choice"))
        if(eva==1):
            mylist=push(mylist)
            print(mylist)
            # mylist=push(mylist)
        elif(eva == 2):
            mylist = pop(mylist)
        elif(eva == 3):
            # mylist = pop(mylist)
            print(mylist)
        elif(eva == 4):
            exit(0)

def push(mylist):
    ele = input("enter the ele")
    mylist.append(ele)
    ele = input("pop2")
    return mylist


def pop(mylist):
    ele=input("pop2")
    mylist.pop()
    ele = input("pop2")
    return mylist


def display():
    ele =input("display3")
    mylist.append(ele)
    return mylist

main()
result = print
