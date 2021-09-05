fm=1000
wd=int(input("enter amount to withdraw"))

if wd>fm:
    print("insufficient amount")

else:
    balance=fm-wd
    print("balance is",balance)