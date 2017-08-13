class Customer:
	def __init__(self,name,account_no,balance):
		self.name=name
		self.account=account_no
		self.balance=balance
	def withdraw(self,amount):
		if(amount>self.balance):
			raise runtimeerror("Insufficient funds")
		else:
			self.balance-=amount
			return self.balance
	def deposit(self,amount):
		self.balance+=amount
		return self.balance
sagar=Customer('sagar',123456,1000)
print(sagar.withdraw(500))
