stk=[]
size=int(input("Enter the size"))
top=0
n=0
def push():
    global size,top
    if (top>size):
        print("stack is full")
    else:
        p=int(input("Enter the element want to push"))
        stk.append(p)
        top+=1
def pop():
    global top,size
    if(top<=0):
        print("stack is empty")
    else:
        stk.pop()
        top-=1
def display():
    print(stk)
while(n!=1):
    print("Enter the operation want to perform")
    opt=int(input("press 1)push 2)pop 3)display"))
    if(opt==1):
        push()
    elif(opt==2):
        pop()
    elif(opt==3):
        display()
    n=int(input("do you want to continue press 1 for exit"))

