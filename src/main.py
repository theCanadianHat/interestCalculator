import InputHandler as IH
import menu.MenuController as MC
import sys

ih = IH.InputHandler()
mc = MC.MenuController({
	"Simple" : ih.handleInputForSimpleInterest,
	"Compound" : sys.exit
	})

mc.displayMenu()

# grandTotal = 0
# for card in cards:
# 	# check format of rate - we want it to be a decimal i.e. 50% == .5
# 	# card.interest = float(card.principal * card.rate * card.timeYears)
# 	card = ic.calculateInterest(card)
# 	print("For card "+card.name+", you will pay this amount in interest:$ " + MONEY_FORMAT.format(card.interest))

# 	total = ic.calculateTotal(card)
# 	print("\tand you will pay this amount in total:$ " + MONEY_FORMAT.format(total))
# 	grandTotal += total
# 	print()

# print("For all " + str(len(cards)) + " cards, you will pay:$ " + MONEY_FORMAT.format(grandTotal))