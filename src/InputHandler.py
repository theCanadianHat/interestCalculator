import CreditCard as CC
import InterestCalculator as IC

class InputHandler:
	MSG_HOW_MANY_CARDS = "\nHow many credit cards do you have? "
	MSG_CARD_NAME = "What is the name of this card? "
	MSG_CARD_PRINCIPAL = "What's this card's principal? $ "
	MSG_CARD_APR = "What's this card's APR? "
	MSG_CARD_TIME = "How many months to pay off this card? "
	MONEY_FORMAT = "{:5.2f}"

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

	def handleInputForSimpleInterest(self, callback):
		cardCount = int(self.handleInput(InputHandler.MSG_HOW_MANY_CARDS))
		cards = []
		print("==================================\n")

		# todo nice error handling for illegal inputs
		for i in range(cardCount):
			name = self.handleInput(InputHandler.MSG_CARD_NAME)
			principal = 0
			while self.validatePricipal(principal) == False:
				principal = float(self.handleInput(InputHandler.MSG_CARD_PRINCIPAL))
			rate = float(self.handleInput(InputHandler.MSG_CARD_APR)) #todo check format
			months = 0
			while self.validateMonths(months) == False:
				months = int(self.handleInput(InputHandler.MSG_CARD_TIME))
			timeYears = float(months / 12.0)
			cards.append(CC.CreditCard(principal, rate, timeYears, name))
			print("==================================\n")

		ic = IC.InterestCalculator()
		grandTotal = 0
		for card in cards:
			# check format of rate - we want it to be a decimal i.e. 50% == .5
			# card.interest = float(card.principal * card.rate * card.timeYears)
			card = ic.calculateInterest(card)
			print("For card "+card.name+", you will pay this amount in interest:$ " + InputHandler.MONEY_FORMAT.format(card.interest))

			total = ic.calculateTotal(card)
			print("\tand you will pay this amount in total:$ " + InputHandler.MONEY_FORMAT.format(total))
			grandTotal += total
			print()

		print("For all " + str(len(cards)) + " cards, you will pay:$ " + InputHandler.MONEY_FORMAT.format(grandTotal))
		callback()