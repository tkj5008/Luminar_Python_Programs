# def printval(*args):
#     return(args)
# print(printval(3,4,5,6,7,8,9,10))


# def details(**args):
#     return args
# print(details(name="Anu",Age=22,place='Kochi'))

def printval(*args):
    sum=0
    for i in args:
        sum+=i
    return sum
print(printval(3,4,5,6,7,8,9,10))