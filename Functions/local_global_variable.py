x=5


def foo():
    #x=5
    global x
    x+=10
    print("localx:",x)
foo()
print("global x:",x)

