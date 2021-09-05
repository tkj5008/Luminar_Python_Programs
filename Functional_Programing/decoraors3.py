def vaccine_a(func):
    def wrapper(a,b,c):
        if b<18:
            raise Exception("Not Eligible")
        else:
            return func(a,b,c)
    return wrapper
@vaccine_a
def vaccine(name,age,place):
    return "Eligible"
print(vaccine("anu",21,"Kochi"))