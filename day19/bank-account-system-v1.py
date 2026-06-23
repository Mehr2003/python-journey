class BankAccount:
    def __init__(self, owner, balance) -> None:
        self.owner = owner
        self.balance = balance
        self.last_status = "No transaction yet"
    def deposit(self, amount):
        self.balance += amount
        self.last_status = "Deposit successful! :)"
        return self.balance
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.last_status = "Successful!"
            return True
        else:
            self.last_status = "Failed!"
            return False
    def show_info(self):
        return f"{self.owner} | {self.balance} | {self.last_status}"
accounts = [
    BankAccount("Ali", 2500),
    BankAccount("Sara", 4200),
    BankAccount("Reza", 1800),
    BankAccount("Maryam", 6000),
    BankAccount("Amir", 900)
]

accounts[0].deposit(600)
accounts[1].withdraw(3000)
accounts[2].deposit(2000)
accounts[3].deposit(2500)
accounts[4].withdraw(1000)

for account in accounts:
    print(account.show_info())
