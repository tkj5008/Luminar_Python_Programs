class Student:
    college="Luminar"
    def __init__(self,name,age,course,mark):
        self.name=name
        self.age=age
        self.course=course
        self.mark=mark
    def printval(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Course:",self.course)
        print("Mark:",self.mark)
    def __str__(self):
        return(Student.college)
f1=open("student1","r")
for line in f1:
    #print(line)
    l=line.split(",")
    name=l[0]
    age=l[1]
    course=l[2]
    mark=l[3]
    st=Student(name,age,course,mark)
    print(st)
    st.printval()