class Add:
    def setvalue(self,a,b):
        self.a=a
        self.b=b
        self.sum=a+b
    def printvalue(self):
        print("Sum is ",self.sum)

ad=Add()
ad.setvalue(23,34)
ad.printvalue()
