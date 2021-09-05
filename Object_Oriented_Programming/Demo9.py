class Employee:
    company="AT&T"
    def __init__(self,name,empid,salary):
        self.name=name
        self.empid=empid
        self.salary=salary
    def printvalue(self):
        print(Employee.company,self.name,self.empid,self.salary,)
obj=Employee("Thomas","TJ618N",25000)
obj.printvalue()
