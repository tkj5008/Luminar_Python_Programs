class Teacher:
    college_name="Luminar"
    def __init__(self,name,id,department,subject):
        self.name=name
        self.id=id
        self.department=department
        self.subject=subject
    def printval(self):
        print(self.name)
        print(self.id)
        print(self.department)
        print(self.subject)
        print(Teacher.college_name)
te=Teacher("Anu",1,"CS","Python")
te.printval()