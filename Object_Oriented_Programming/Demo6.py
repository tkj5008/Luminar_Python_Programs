class Employee:
    company="AT&T"
    def setvalue(self,name,empid,salary):
        self.name=name
        self.empid=empid
        self.salary=salary
    def printvalue(self):
        print("Name",self.name)
        print("EmpId",self.empid)
        print("Salary",self.salary)
        print("Company",Employee.company)
em=Employee()
em.setvalue("Thomas","TJ618N",75000)
em.printvalue()
