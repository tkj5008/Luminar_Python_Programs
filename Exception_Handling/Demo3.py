lst=[1,2,3,4,5]
pos=int(input("Enter the index"))
try:
    print(lst[pos])
except Exception as e:
    print(e.args)