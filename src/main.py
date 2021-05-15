
import CreditCard as CC
import InputHandler as IH

MSG_HOW_MANY_CARDS = "How many credit cards do you have? "
MSG_CARD_NAME = "What is the name of this card? "
MSG_CARD_PRINCIPAL = "What's this card's principal? $ "
MSG_CARD_APR = "What's this card's APR? "
MSG_CARD_TIME = "How many months to pay off this card? "
MONEY_FORMAT = "{:5.2f}"
ih = IH.InputHandler()

cardCount = int(ih.handleInput(MSG_HOW_MANY_CARDS))
cards = []
print("==================================\n")

# todo nice error handling for illegal inputs
for i in range(cardCount):
	name = ih.handleInput(MSG_CARD_NAME)
	principal = 0
	while ih.validatePricipal(principal) == False:
		principal = float(ih.handleInput(MSG_CARD_PRINCIPAL))
	rate = float(ih.handleInput(MSG_CARD_APR)) #todo check format
	months = 0
	while ih.validateMonths(months) == False:
		months = int(ih.handleInput(MSG_CARD_TIME))
	timeYears = float(months / 12.0)
	cards.append(CC.CreditCard(principal, rate, timeYears, name))
	print("==================================\n")

grandTotal = 0
for card in cards:
	# check format of rate - we want it to be a decimal i.e. 50% == .5
	card.interest = float(card.principal * card.rate * card.timeYears)
	print("For card "+card.name+", you will pay this amount in interest:$ " + MONEY_FORMAT.format(card.interest))

	total = float(card.principal + card.interest)
	print("\tand you will pay this amount in total:$ " + MONEY_FORMAT.format(total))
	grandTotal += total
	print()

print("For all " + str(cardCount) + " cards, you will pay:$ " + MONEY_FORMAT.format(grandTotal))