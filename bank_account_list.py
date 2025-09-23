class BankAccount: 
  def __init__(self, first_name,last_name,account_id,account_type, pin, balance):
    self.first_name = first_name
    self.last_name = last_name
    self.account_id = account_id
    self.account_type = account_type
    self.pin = pin
    self.balance = balance

  def deposit(self,deposit_amount):
    self.deposit_amount = deposit_amount
    self.balance = self.balance + deposit_amount
    

  def withdraw(self,withdraw_amount):
    self.withdraw_amount = withdraw_amount
    self.balance = self.balance - withdraw_amount

  def display_balance(self):
    print(f'Balance {self.balance}')


account = BankAccount('Gero','Pereyra',101,'Debit Card',1234,5000)


account.deposit(96)
account.withdraw(25)
account.display_balance()
