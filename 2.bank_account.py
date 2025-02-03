class BankAccount:

    def __init__(self,balance=0):
        self.balance=balance  
    
    def deposit(self,amount):
        if int(amount)>0:
            self.balance+=amount
            print(f"the total amount in the account is:{self.balance}")
        else:
            print("deposit amount must be positive number")
        
    def withdraw(self,amount):
        if amount>0:
            self.balance-=amount
            print(f"the total amount after withdrawal is:{self.balance} ")
        else:
            print("enter the valid amount")
        
ba=BankAccount(int(input("enter the balance:")))
ba.deposit(int(input("enter the amount to be deposited:")))
ba.withdraw(int(input("enter the amount to be withdrawn:")))