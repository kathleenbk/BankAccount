class BankAccount:
    bank_accounts = []

    def __init__(self, name, int_rate, balance): 
        self.name = name
        self.int_rate = int_rate
        self.balance = balance
        
        BankAccount.bank_accounts.append(self)

        
    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        self.balance -= amount
        return self
    
    def display_account_info(self):
        print(f"{self.name} Balance: {self.balance}")
        return self
    
    def yield_interest(self):
        self.balance = self.balance * self.int_rate
        return self

    @classmethod
    def print_all(cls):
        for account in cls.bank_accounts:
            print(f"{account.name} Balance: {account.balance}")

Account1 = BankAccount("Checking",1.01,0)
Account2 = BankAccount("Savings",1.01,0)

Account1.deposit(400).deposit(500).deposit(200).withdraw(100).yield_interest().display_account_info()

Account2.deposit(13000).deposit(2000).withdraw(1000).withdraw(1000).withdraw(1000).withdraw(1000).yield_interest().display_account_info()

BankAccount.print_all()