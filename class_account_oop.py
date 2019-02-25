class Account():

    def __init__(self,owner,balance=0):

        self.owner = owner
        self.balance = balance

    def deposit(self,dep_amt):
         self.balance = self.balance + dep_amt
        print(f"Added {dep_amt} to the balance")
