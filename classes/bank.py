# This is another implementation of a class

class BankAccount:
	def __init__(self, owner, balance=0):
		self.owner = owner
		self.balance = balance

	def deposit(self, amount):
		self.balance += amount
		print(f"New balance: ${self.balance} after Deposition of ${amount}")

	def withdraw(self, amount):
		if amount <= self.balance:
			self.balance -= amount
			print(f"New balance: ${self.balance} after withdrawal of ${amount}")
		else:
			print("Insufficient funds!")

# Using the class to make an object
my_account = BankAccount("Zuxyll", 15000)
my_account.deposit(8000)
my_account.withdraw(10000)
