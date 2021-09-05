lst=[1,2,3,4,5,6,7,8,9,0,23,34,34,32,5,56,36,78]

# def lin(lst):
#     if num in list1:
#         print("Number available")
#     else:
#         print("Not Available")
# lin(10)

def lin(lst):
    ele=int(input("Enter the element to search "))
    fla=0
    for i in lst:
        if i==ele:
            fla=1
            break
    if fla==0:
        print("Not found")
    else:
        print("Found")
lin (lst)