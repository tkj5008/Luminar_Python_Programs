lst=[1,2,3,4,5,6,7]
i=int(input("Enter the index to be displayed"))
try:
    print(lst[i])
except:
    print("Exception occured")
finally:
    print("Inside Finally")