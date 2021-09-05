class Vehicle:
    def __init__(self,model,regno,colour):
        self.model=model
        self.regno=regno
        self.colour=colour
    def printval(self):
        print(self.model,self.colour,self.regno)

    def __str__(self):
        return self.model+self.colour

ve=Vehicle("Beleno-2020","KL797333","Magma Grey")
ve.printval()
print(ve)