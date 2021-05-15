class InputHandler:
	def handleInput(self, message):
		value = input(message)
		print()
		return value

	def validatePricipal(self, principal):
		if principal <= 0:
			print("Please enter a non-zero positive value for the principal.")
			return False
		return True

	def validateMonths(self, months):
		if months <= 0:
			print("Please enter a non-zero positive value for the months.")
			return False
		return True