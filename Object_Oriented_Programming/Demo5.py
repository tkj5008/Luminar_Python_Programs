#instance variable- relatedtomethods using self
#Static variable related to class
# class Student:
#     def setvalue(self,name,rollno,age,standard):
#         self.name=name
#         self.rollno=rollno
#         self.age=age
#         self.standard=standard
#     def printvalue(self):
#         print("Name",self.name)
#         print("RollNo.",self.rollno)
#         print("Age",self.age)
#         print("Standard",self.standard)
# st=Student()
# st.setvalue("Thomas",12,19,"X")
# st.printvalue()

class Student:
    school="Luminar"
    def setvalue(self,name,rollno,age):
        self.name=name
        self.rollno=rollno
        self.age=age

    def printvalue(self):
        print("Name",self.name)
        print("RollNo.",self.rollno)
        print("Age",self.age)
        print("School",Student.school)
st=Student()
st.setvalue("Thomas",12,19)
st.printvalue()
st1=Student()
st.setvalue("TOM",12,19)
st.printvalue()


