class ATM(object):
    def __init__(self, Cashwithdrawl, Selfquery, amount, model):
        self.Cashwithdrawl = Cashwithdrawl
        self.Selfquery = Selfquery
        self.amount = amount
        self.model = model

    def start(self):
        print("Ready to pay")

    def stop(self):
        print("Thank you for using the ATM")

    def money(self):
        print("The amount you saved is")

        "Amount saved over there"

    def withdraw(self):
        print("Do you want to change the settings of the banking account?")

Machine = ATM("200","Selection of deposit or have NASA bring 150 billion dollars to the moon","$500","Touchless machine")
print(Machine.start())
print(Machine.Cashwithdrawl)
print(Machine.amount)
print(Machine.Selfquery)
print(Machine.model)