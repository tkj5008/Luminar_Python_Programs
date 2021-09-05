class Bank:
    def acCreate(self,acno,name,bname):
        self.bname=bname
        self.name =name
        self.acno=acno
        self.minimumbalance=5000
        self.balance=self.minimumbalance
    def deposit(self,amt):
        self.amt=amt
        self.balance=self.amt
        print("Your",self.bname,"account has been credited with amt",self.amt)
        print("Your current balance=",self.balance)
    def withdraw(self,amnt):
        self.amnt=amnt
        if self.amnt>self.balance:
            print("Insufficient Balance")
        else:
            print("Account deboted with ",self.amnt)
            self.balance=self.amnt
            print("Available Balance",self.balance)
obj=Bank()
num=int(input("Enter ac Number"))
obj.acCreate(num,'abc','Thomas')
obj.deposit(2500)
obj.withdraw(1500)



