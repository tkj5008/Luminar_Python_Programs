class Student:
    college="ABC"
    def __init__(self,name,rollno,dep):
        self.name=name
        self.rollno=rollno
        self.dep=dep
    def printv(self):
        print(self.name,self.rollno,self.dep,Student.college)
    def __str__(self):
        return self.name+self.dep
st=Student("Anu",2,"CS")
st.printv()
print(st)