
class BankAccount:
    ROI = 10.0

    def __init__(self, name, amount):
        self.Name = name
        self.Amount = amount

    def Display(self):
        print("Account Holder Name:", self.Name)
        print("Account Balance:", self.Amount)

    def Deposit(self):
        value = int(input("Enter amount to deposit: "))
        self.Amount += value
        print("Amount deposited successfully")

    def Withdraw(self):
        value = int(input("Enter amount to withdraw: "))
        if value <= self.Amount:
            self.Amount -= value
            print("Amount withdrawn successfully")
        else:
            print("Insufficient balance")

    def CalculateInterest(self):
        interest = (self.Amount * BankAccount.ROI) / 100
        return interest

obj1 = BankAccount("Amit", 10000)
obj1.Display()
obj1.Deposit()
obj1.Withdraw()
print("Interest:", obj1.CalculateInterest())
obj1.Display()