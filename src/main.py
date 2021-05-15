
import CreditCard as CC

cardCount = int(input("How many credit cards do you have? "))

for i in range(cardCount):
	print("hi")

principal = int(input("What's your principal? "))
rate = float(input("What's your rate? "))
cc1 = CC.CreditCard(principal, rate, "Credit of USA")
months = int(input("How many months? "))

# check format of rate - we want it to be a decimal i.e. 50% == .5
interest = float(cc1.principal * cc1.rate * months)
print("For "+cc1.name+", you will pay this amount in interest:$ " + "{:5.2f}".format(interest))

total = float(cc1.principal + interest)
print("For "+cc1.name+", you will pay this amount in total:$ " + "{:5.2f}".format(total))
