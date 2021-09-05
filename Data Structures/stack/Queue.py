que=[]
size=int(input("Enter the size::"))
front=0
rear=0
n=0
def insert():
    global front,rear,size,que
    if rear>=size:
        print("que is full")
    else:
        p=int(input("Enter the elements want to insert::"))
        que.insert(rear,p)
        #insert(position,element)
        rear+=1
        for i in range(front,rear):
            print(que[i])
def delete():
    global front, rear, size, que
    if rear==front:
        print("Que is empty")
    else:
        front+=1
        for i in range(front,rear):
            print(que[i])
while n!=1:
    print("Enter the operation to perform")
    opt=int(input("Press \n1)Enqueue\n2)Dequeue\n"))
    if opt==1:
        insert()
    elif opt==2:
        delete()

