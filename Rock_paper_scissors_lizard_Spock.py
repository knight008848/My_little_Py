# Rock-paper-scissors-lizard-Spock template in CodeSkulptor
# http://www.codeskulptor.org/#user15_mZZgnUuRnF_0.py
# http://www.codeskulptor.org/#user15_mZZgnUuRnF_1.py

"""
Rock-paper-scissors-lizard-Spock (RPSLS) is a variant of Rock-paper-scissors that allows five choices. Each choice wins against two other choices, loses against two other choices and ties against itself.

The rules of Rock-paper-scissors-lizard-Spock are:

Scissors cut paper
Paper covers rock
Rock crushes lizard
Lizard poisons Spock
Spock smashes (or melts) scissors
Scissors decapitate lizard
Lizard eats paper
Paper disproves Spock
Spock vaporizes rock
Rock breaks scissors

"""
import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions
# A list to store weapons in this game.
weapons = ['rock', 'Spock', 'paper', 'lizard', 'scissors']

def number_to_name(number):
    # fill in your code below
    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    
    if number in range(5):
        name = weapons[number]
    else:
        print("Invaild number")
        name = None
    
    return name

    
def name_to_number(name):
    # fill in your code below

    # convert name to number using if/elif/else
    # don't forget to return the result!
    number = -1
    
    for i in range(5):
        if name == weapons[i]:
            number = i
        
    if number == -1:
        print("Invaild name")
        number = None
    
    return number

def rpsls(name): 
    # fill in your code below

    # convert name to player_number using name_to_number
    player_number = name_to_number(name)

    # compute random guess for comp_number using random.randrange()
    comp_number = random.randint(0,4)

    # compute difference of player_number and comp_number modulo five
    diff = (player_number - comp_number) % 5

    # use if/elif/else to determine winner
    if diff == 1 or diff ==2:
        
        winner = 1
    
    elif diff ==3 or diff ==4:
    
        winner = 2
    
    elif diff == 0:
    
        winner = 0
    
    else:
        winner = None

    # convert comp_number to name using number_to_name
    player_name = name
    comp_name = number_to_name(comp_number)
    
    # print results
    print("Player chooses %s" % player_name)
    print("Computer chooses %s" % comp_name)
    if winner == 1:
        print("Player wins!")
    elif winner == 2:
        print("Computer wins!")
    else:
        print("Player and computer tie!")
        
        
    print("*"*8)

    
# test your code
print("*"*8)
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric




