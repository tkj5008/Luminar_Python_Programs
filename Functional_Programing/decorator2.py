def admin_required(func):
    def wrapper(a,b):
        if a!="admin":
            raise Exception("You are not allowed")
        else:
            return func(a,b)
    return wrapper
@admin_required
def change_pin(user,pin):
    mypin=pin
    return mypin
@admin_required
def delet_ac(user,acno):
    return str(acno)+"delete"
print(delet_ac('admin',1147))