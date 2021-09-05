a="luminar"
e=input("Enter element to check")
flag=0
for i in a:
    if i in e:
        flag=1
if flag==1:
    print("present")
else:
    print("not present")
