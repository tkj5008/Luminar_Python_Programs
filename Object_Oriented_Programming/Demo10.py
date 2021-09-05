class Calc:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def add(self):
        return self.a+self.b

    def sub(self):
        return self.a-self.b

    def mult(self):
        return self.a*self.b

    def div(self):
        return self.a/self.b

a=int(input("Enter No"))
b=int(input("Enter No2"))
obj=Calc(a,b)
print(obj.add())
print(obj.sub())
print(obj.mult())
print(obj.div())