
import CreditCard as CC

def handleInput(message):
	value = input(message)
	print()
	return value

def validatePricipal(principal):
	if principal <= 0:
		print("Please enter a non-zero positive value for the principal.")
		return False
	return True

def validateMonths(months):
	if months <= 0:
		print("Please enter a non-zero positive value for the months.")
		return False
	return True

MONEY_FORMAT = "{:5.2f}"

cardCount = int(handleInput("How many credit cards do you have? "))
cards = []
print("==================================\n")

# todo nice error handling for illegal inputs
for i in range(cardCount):
	name = handleInput("What is the name of this card? ")
	principal = 0
	while validatePricipal(principal) == False:
		principal = float(handleInput("What's this card's principal? $ "))
	rate = float(handleInput("What's this card's APR? ")) #todo check format
	months = 0
	while validateMonths(months) == False:
		months = int(handleInput("How many months to pay off this card? "))
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