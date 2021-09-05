d={1:10,2:20,3:30,4:40,5:50,6:60}
def present(x):
    if x in d:
        print(x,'is present')
    else:
        print(x,'is not present')
x=int(input("Enter Key"))
present(x)