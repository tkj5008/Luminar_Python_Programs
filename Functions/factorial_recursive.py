def fact(x):
    if x==0:
        return 1
    else:
        return x*fact(x-1)
num=int(input("Enter the number"))
print("The factorial is ",fact(num))
