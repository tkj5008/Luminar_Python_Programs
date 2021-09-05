lst=[1,2,3,4,5,6,7,8,9,3,45,543,32,33,]

min=lst[0]
max=lst[0]
for i in lst:
    if i<min:
        min=i

    elif i>max:
        max=i

print("The minimum element is ",min)
print("The maximum element is ",max)


#lst.sort()
#print(lst[0])
#print(lst[1])
