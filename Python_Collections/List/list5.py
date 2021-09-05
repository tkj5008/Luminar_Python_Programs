l1 =[1,23,45,67,-34,-21,-12,-1,65]

l2=[]
while l1:
    min=l1[0]
    for i in l1:
        if i<min:
            min=i
    l2.append(min)
    l1.remove(min)
print(l1)
print(l2)