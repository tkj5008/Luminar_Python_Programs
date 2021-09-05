class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printval(self):
        print("Name",self.name)
        print("Age",self.age)
class Employee(Person):
    def __init__(self,company,id,salary,name,age):
        super().__init__(name,age)
        self.company=company
        self.id=id
        self.salary=salary
    def print(self):
        print(self.company)
        print(self.id)
        print(self.salary)
em=Employee("Luminar","TJ618N",45000,"Thomas",30)
em.printval()
em.print()