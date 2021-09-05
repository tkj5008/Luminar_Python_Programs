lst=[1,2,4,6,7,8,9,12,43,34,23,67,54,87,78,98,68]
def bsearch():
    lst.sort()
    print(lst)
    ele=int(input("Enter the Element"))
    fla=0
    low=0
    upp=len(lst)-1
    while low<=upp:
        mid=(low+upp)//2

        if ele>lst[mid]:
            low=mid+1
        elif ele<lst[mid]:
            upp=mid-1
        elif ele==lst[mid]:
            #print(mid)
            fla=1
            break
    if fla==1:
        print("Found at",mid)
    else:
        print("Not Found")
bsearch()


#can update values using index values

#lst[0]=4