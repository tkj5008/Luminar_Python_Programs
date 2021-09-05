import re
n=input("Enter the String to validate")
x='[a-zA-Z]+\d$'
match =re.fullmatch(x,n)
if match is not None:
    print("Valid")
else:
    print("Invalid")