class BankAccount:
	def __init__(self, initial_balance=0):
		if not isinstance(initial_balance, (int, float)):
			raise TypeError("Initial balance must be a number.")
		if initial_balance < 0:
			raise ValueError("Initial balance cannot be negative.")
		self._account_balance = initial_balance
	def deposit(self, amount):
		if not isinstance(amount, (int, float)):
			raise TypeError("Deposit amount must be a number.")
		if amount <= 0:
			raise ValueError("Deposit amount must be positive.")
		self._account_balance += amount
	def withdraw(self, amount):
		if not isinstance(amount, (int, float)):
			raise TypeError("withdraw amount must be a number")
		if amount <= 0:
			raise ValueError("withdraw amount must be positive.")
		if self._account_balance >= amount:
			self._account_balance -= amount
			return True
		else:
			return False
	def display_balance(self):
		print(f"Current Balance: ${self._account_balance:.2f}")

	@property
	def balance(self):
		return self._account_balance
