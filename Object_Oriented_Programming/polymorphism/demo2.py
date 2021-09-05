#overriding
# same method name and same num of parameters
# Child class method  overide parent class method

class Person:
    def printval(self,name):
        self.name=name
        print("Inside Parent",self.name)
class Child(Person):
    def printval(self,class1):
        self.class1=class1
        print("Inside Child",self.class1)
ch=Child()
ch.printval("abc")
