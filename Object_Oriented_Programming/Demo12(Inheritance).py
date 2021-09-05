#Single Inheritance

class Person:#base class/super class/perent class
    def walk(self):
        print("Person is walking")
    def read(self):
        print("Person is reading")
class Student(Person):#derived class/sub class/child class
    def exam(self):
        print("Student is attending exam")
pe=Person()
pe.walk()
pe.read()

st=Student()
st.exam()
st.walk()
st.read()
