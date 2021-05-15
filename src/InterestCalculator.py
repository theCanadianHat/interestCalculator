class InterestCalculator:
	def calculateInterest(self, creditCard):
		creditCard.interest = float(creditCard.principal * creditCard.rate * creditCard.timeYears)
		return creditCard

	def calculateTotal(self, creditCard):
		return float(creditCard.principal + creditCard.interest)