a=int(input("enter num 1"))
b=int(input("enter num 2"))
c=int(input("enter num 3"))
if(a>b):
    if(a>c):
        {
            print('a is greater')
        }
    else:
        print("c iss greater")
elif(b>c):
    print("b is greater")
else:
    print('c is greater')



a=int(input("enter the num 1"))
b=int(input("enter the num 2"))
c=int(input("enter the num 3"))
if(a>b):
    if(a>c):
        {
            print("a is greater")
        }
    elif(b>a):
        {
            print("b is greater")
        }
    elif(c>a):
        {
            print("c is greater")
        }
else:
    {
        print(" invalid value")
    }