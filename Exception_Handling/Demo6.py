print("Welcome to Vaccination Schedule")
age=int(input("Enter the Age"))
if age<18:
    raise Exception("Not Eligible for Vaccination")
else:
    print("Eligible for vaccination")