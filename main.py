import random 

# This input is where the user chooses what weapon to use
user_action = input("Enter Choice( rock, paper, scissor):")

# Possible choices for the computer to choose formatted in an array 
computer_possible_actions = ["rock", "paper", "scissor"]

#Computer chooses a random element of the computer_possible_actions array  
computer_action = random.choice(computer_possible_actions )


#Recorded input from and output from computer formated into a literal string and presented on screen 
print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")


