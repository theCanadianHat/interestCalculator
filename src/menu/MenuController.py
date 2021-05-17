import sys

class MenuController:
	def __init__(self, menuOptions):
		#map options to method callbacks so we know what to invoke on option selection
		self.menuOptions = menuOptions
		self.menuOptions["Quit"] = self.confirmQuit

	def quit(self):
		sys.exit()

	def displayMenu(self):
		selectionMap = {}
		print("========== Main Menu ==========\n")
		
		for index, option in enumerate(self.menuOptions):
			print("[" + str(index) + "]\t" + option)
			selectionMap[str(index)] = option
		
		selectedOption = input("\nPlease select and option: ")
		self.menuOptions[selectionMap[selectedOption]](self.displayMenu)


	def confirmQuit(self, callback):
		confirmation = input("\nAre you sure you want to quit (y/n)? ")
		if confirmation == "y" or confirmation == "Y":
			quit()