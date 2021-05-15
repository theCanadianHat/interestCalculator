
import CreditCard as CC

cardCount = int(input("How many credit cards do you have? "))
cards = []
print()

# todo nice error handling for illegal inputs
for i in range(cardCount):
	name = input("What is the name of this card? ")
	principal = float(input("What's your principal? "))
	rate = float(input("What's your APR? "))
	timeYears = float(int(input("How many months? ")) / 12.0)
	cards.append(CC.CreditCard(principal, rate, timeYears, name))
	print() # new line

grandTotal = 0
for card in cards:
	# check format of rate - we want it to be a decimal i.e. 50% == .5
	card.interest = float(card.principal * card.rate * card.timeYears)
	print("For card "+card.name+", you will pay this amount in interest:$ " + "{:5.2f}".format(card.interest))

	total = float(card.principal + card.interest)
	print("\tand you will pay this amount in total:$ " + "{:5.2f}".format(total))
	grandTotal += total
	print()

print("For all " + str(cardCount) + " cards, you will pay:$ " + "{:5.2f}".format(grandTotal))