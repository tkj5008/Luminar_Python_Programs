lst=[1,2,3,4,5,6,7,8,9,11,1,12,2,3,8]
b=[]
for i in lst:
    if i not in b:
        b.append(i)
    else:
        print(i)

