num1=int(input("Enter no1"))
num2=int(input("Enter no2"))
if num2>num1:
    raise Exception("no2is Greater")
else:
    print(num1/num2)
