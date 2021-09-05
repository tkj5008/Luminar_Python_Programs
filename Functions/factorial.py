def fact(num):
    res=1
    if num>0:
        for i in range(1,num+1):
            res=res*i
        print("factorial", res)
    elif num==0:
        print("factorial of zero is one")
    else:
        print("factorial doesnot exist for -ve numbers")

fact(5)
fact(7)
fact(-2)
