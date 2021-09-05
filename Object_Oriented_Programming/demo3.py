class Employee:
    def setvalue(self,name,id,age,salary):
        self.name=name
        self.id=id
        self.age=age
        self.salary=salary
    def printvalue(self):
        print("Name",self.name)
        print("ID",self.id)
        print("Age",self.age)
        print("Salary",self.salary)
em=Employee()
em.setvalue("Thomas","TJ618N",32,75000)
em.printvalue()
em1=Employee()
em1.setvalue("Albert","AA2807",31,70000)
em.printvalue()

