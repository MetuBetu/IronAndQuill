import os
def clear():
    os.system("cls" if os.name=="nt" else "clear")

try:
    from termcolor import cprint
except ImportError:
    os.system("pip install termcolor")
    from termcolor import cprint
try:
    import pytest
except ImportError:
    os.system("pip install pytest")
    import pytest
    
# Import / download modules above!
clear()

# Front end code goes here

from Data.iaq_election_process import *
# from Data.iaq_traits_list import *
from GUI.iaq_player_stats_screen import playerStatsScreen as playerStatsScreen
from GUI.iaq_governance_screen import *

# Naming Coventions (To Be Added):
#
# Variables = this_is_a_variable
# Functions = thisIsAFunction

def characterCreation():
    # Needs improvements probably

    global player_first_name
    global player_surname
    global player_age
    global player_health
    global player_influence
    global player_base_momentum
    global player_money
    global player_salary

    player_first_name = input("Name: ")
    player_surname = input("Surname: ")
    choose_age_loop = True
    while choose_age_loop:
        try:
            player_age = (int(input("Age (Choose from 18 to 80): ")) - 1)
        except:
            print("Only numbers between 18 and 80 are allowed!")

        if player_age >= 18 and player_age <= 80:
            choose_age_loop = False
        else:
            print("Only numbers between 18 and 80 are allowed!")
    player_health = 100 - player_age
    player_influence = 0
    player_money = 100 * player_age
    player_salary = 80
    print("Character created!")
    clear()

characterCreation()
while True:
    clear()
    player_health -= 1
    if player_health < 1:
        cprint("YOU DIED!", "light_red", attrs=["blink"])
        characterCreation()
    player_age += 1
    player_base_momentum = 41 - round(player_age / 2)
    player_momentum = player_base_momentum
    player_money += player_salary
    turn = True
    while turn:
        clear()
        print("-" * 20)
        cprint("NAVIGATION", "light_blue")
        cprint("Main Menu", "light_green", attrs=["blink"])
        print("   (1) Your Character")
        print("Momentum left: " + str(player_momentum))
        cprint("(END) End Year", "light_magenta")
        print("-" * 20)
        cprint("Tip: ", "yellow", end="")
        print("You can back up in the hierarcy by entering 'back' or go to a suboption by entering the items associated index, e.g. '3' or 'END'.")
        print("")
        navoption = input("Enter navigation option: ")
        if navoption == "1":
            playerStatsScreen(player_first_name, player_surname, player_age, player_money, player_health, player_influence, player_momentum, player_salary, clear)
        elif navoption == "END":
            turn = False
            print("Proceeding to next year...")
            time.sleep(3)

### General layout idea: (You spend political momentum for actions. End the turn to progress a year and get more momentum.)
# Main Menu
 # Your Character
  # General stats such as:
   # Name and age
   # Current position & party
   # Health
   # Influence
   # Political momentum
   # Money (and salary)
   # Reputation aka traits (non priority)
 # Your Party
  # Stuff
 # Governance
  # View latest election and ruling party stats
   # Perform / View Polls
   # View Other Parties
  # Policies
   # Start vote on policy
   # Vote aye or nay

 ### Progress a year

def tests():
    assert 1 == 1