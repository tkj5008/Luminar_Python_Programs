class A:
    def printA(self):
        print("Inside A")
class B(A):
    def printB(self):
        print("Inside B")
class C(B):
    def printC(self):
        print("Inside C")
a=A()
a.printA()
b=B()
b.printA()
b.printB()
c=C()
c.printA()
c.printB()
c.printC()