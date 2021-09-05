class Person:
    def set(self,name,age,adrs):
        self.name=name
        self.age=age
        self.adrs=adrs
        print(self.name,self.age,self.adrs)
class Child(Person):
    def setv(self,school,std):
        self.school=school
        self.std=std
        print(self.school,self.std)
class Student(Child):
    def printv(self,rollno,mark):
        self.rollno=rollno
        self.mark=mark
        print(self.rollno,self.mark)
class Parent(Person):
    def setval(self,job,salary):
        self.job=job
        self.salary=salary
        print(self.job,self.salary)
pa=Parent()
pa.set("Thomas",32,"abc")
pa.setval("Engineer",45000)

st=Student()
st.set("Anu",17,"abc")
st.setv("Luminar",11)
st.printv(1,98)