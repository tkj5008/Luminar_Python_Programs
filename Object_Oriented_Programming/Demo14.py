class Person:
    def set(self,name,age,adrs):
        self.name=name
        self.age=age
        self.adrs=adrs
        print(self.name,self.age,self.adrs)
class Child:
    def setv(self,school,std):
        self.school=school
        self.std=std
        print(self.school,self.std)
class Student(Person,Child):
    def printv(self,rollno,mark):
        self.rollno=rollno
        self.mark=mark
st=Student()
st.set("anu",27,"abc")
st.setv("Luminar",11)
st.printv(2,98)
