a=input("Enter a string")
b="aeiou"
count=0
for i in a:
    if i in b:
        count=count+1
print(count)