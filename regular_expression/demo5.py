import re
n='56'
x='[a-z0-9]+'
match =re.fullmatch(x,n)
if match is not None:
    print("Valid")
else:
    print("Invalid")