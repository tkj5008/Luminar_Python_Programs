class Person:
    def set(self,name,age,adrs):
        self.name=name
        self.age=age
        self.adrs=adrs
        print(self.name,self.age,self.adrs)



        
class Employee(Person):
    def setval(self,id,salary,dprtmnt):
        self.id=id
        self.salary=salary
        self.dprtmnt=dprtmnt
        print(self.id,self.salary,self.dprtmnt)



