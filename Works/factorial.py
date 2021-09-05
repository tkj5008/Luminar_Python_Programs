n=int(input("enter number"))
if n>0:
    res=1
    for i in range (1,n+1):
        res=res*i
    print(res)
if n==0:
    print("factorial of 0 is one")
else:
    print("factorial doesnot exist for negative number")