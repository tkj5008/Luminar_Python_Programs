import re
n=input("Enter the vehicle number to validate")
x='[K][L][0-9]{2}[A-Z]{2}\d{4}$'
match =re.fullmatch(x,n)
if match is not None:
    print("Valid")
else:
    print("Invalid")