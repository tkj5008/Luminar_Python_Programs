a=set()
b=set()
lmt=int(input("enter the limit"))
for i in range(lmt):
    element=int(input("enter element"))
    a.add(element)
for i in a:
    b.add(i**2)
print(a)
print(b)

