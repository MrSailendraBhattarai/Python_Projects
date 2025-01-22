

class BankAccount:
    def __init__(self,account):
        self.account=account
        self.amount=0

    def deposit(self):
            dep=float(input("Enter Amount to Deposit>>"))
            if dep>0:
                self.amount +=dep
            else:
                print("Enter Amount Greater than 0")
    def withdraw(self):
        draw=float(input("Enter Amount to WithDraw>>"))
        if self.amount<draw:
            print("Insufficient Balance")
        else:
            self.amount-=draw
    
    def view(self):
        print(f"Your Account Number : {self.account}")
        print(f"You Have {self.amount} in your Account")


Bank=BankAccount('0215751937661001')
while True:
    option=int(input("""Enter One Option :
    1: Deposit
    2: WithDraw
    3: View Details \n"""))

    if option==1:
        Bank.deposit()
    elif option==2:
        Bank.withdraw()
    elif option==3:
        Bank.view()
    else:
        print("Invalid!!")
