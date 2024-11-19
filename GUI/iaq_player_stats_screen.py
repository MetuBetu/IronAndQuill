import time
from termcolor import cprint

def playerStatsScreen(player_first_name, player_surname, player_age, player_money, player_health, player_influence, player_momentum, player_salary, clear):
	inNav = True
	while inNav:
		clear()
		print("-" * 20)
		cprint("NAVIGATION", "light_blue")
		print("Main Menu")
		cprint("   Your Character", "light_green", attrs=["blink"])
		print("Momentum left: " + str(player_momentum))
		print("-" * 20)
		cprint("Tip: ", "yellow", end="")
		print("You can back up in the hierarcy by entering 'back' or go to a suboption by entering the items associated index, e.g. '3' or 'END'.")
		print("")
		print("Name: " + player_first_name + " " + player_surname)
		print("Age: " + str(player_age))
		print("Money: " + str(player_money))
		print("Salary: " + str(player_salary))
		print("Political Momentum: " + str(player_momentum))

		if player_health > 80:
			print("Health: Perfect ", end="")
			print("(" + str(player_health) + ")")
		elif player_health > 60:
			print("Health: Great ", end="")
			print("(" + str(player_health) + ")")
		elif player_health > 40:
			print("Health: Fine ", end="")
			print("(" + str(player_health) + ")")
		elif player_health > 20:
			print("Health: Weak ", end="")
			print("(" + str(player_health) + ")")
		else:
			print("Health: Terrible")
			print("(" + str(player_health) + ")")

		if player_influence > 8000:
			print("Influence: Dominant ", end="")
			print("(" + str(player_influence) + ")")
		elif player_influence > 6000:
			print("Influence: Significant ", end="")
			print("(" + str(player_influence) + ")")
		elif player_influence > 4000:
			print("Influence: Recognized ", end="")
			print("(" + str(player_influence) + ")")
		elif player_influence > 2000:
			print("Influence: Minor ", end="")
			print("(" + str(player_influence) + ")")
		else:
			print("Influence: Negligible ", end="")
			print("(" + str(player_influence) + ")")

		print("")
		navoption = input("Enter navigation option: ")
		if navoption == "back":
			inNav = False
		else:
			print("That's not a valid navigation option.")
			time.sleep(3)