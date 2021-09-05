def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mult(x,y):
    return x*y
def div(x,y):
    return x/y
print("Select Operation")
print("1.Addition")
print("2.Substraction")
print("3.Multiplication")
print("4.Division")

while True:
    choice = int(input("Enter the choice"))
    num1 = float(input("Enter the number 1"))
    num2 = float(input("Enter the number 2"))
    if choice==1:
        print(add(num1,num2))
    elif choice==2:
        print(sub(num1,num2))
    elif choice==3:
        print(mult(num1,num2))
    elif choice==4:
        print(div(num1,num2))
    else:
        print("Invalid choice")
