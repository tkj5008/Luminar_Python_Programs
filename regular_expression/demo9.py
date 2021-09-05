import re
n=input("Enter the String to validate")
x='[a-zA-Z0-9]+[@][a-z]+[.][a-z]{2,3}$'
match =re.fullmatch(x,n)
if match is not None:
    print("Valid")
else:
    print("Invalid")

# Starting with a and ending with b
# x=^a[a-zA-Z0-9\W]*b$

# Minimum 8 and maximum 15 without numbers
# x="([\D]{8,15})"

# Starting with  Upper case Letter and then anything

#x="(^[A-Z][a-z0-9\W]*)"