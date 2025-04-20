import random 

# This input is where the user chooses what weapon to use
user_action = input("Enter Choice( rock, paper, scissor):")

# Possible choices for the computer to choose formatted in an array 
computer_possible_actions = ["rock", "paper", "scissor"]

computer_action = random.choice(computer_possible_actions )

print(user_action)

print(computer_action)