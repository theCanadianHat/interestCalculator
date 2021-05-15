class CreditCard:
	def __init__(self, principal, rate, timeYears, name="Unamed"):
		self.principal = principal
		self.rate = rate
		self.timeYears = timeYears
		self.name = name
		self.interest = 0