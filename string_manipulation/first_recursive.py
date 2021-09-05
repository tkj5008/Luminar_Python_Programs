a=input("Enter the string")
b=""
for i in a:
    if i not in b:
        b=b+i
    else:
        print(i)
        break        #use break if only first recursive character is required