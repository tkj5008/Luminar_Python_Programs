n1=int(input("enter n1"))
n2=int(input("enter n2"))
n3=int(input("enter n3"))

if (n1>n2) and (n1>n3):
    print("the Greater number is",n1)
elif (n2>n1) and (n2>n3):
    print("the Greater number is",n2)
elif n2==n1==n3:
    print("Three numbers are equal ")
else:
    print("The greater number is ",n3)