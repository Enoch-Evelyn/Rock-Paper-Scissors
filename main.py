import random 

# This input is where the user chooses what weapon to use
user_action = input("Enter Choice( rock, paper, scissor):")

# Possible choices for the computer to choose formatted in an array 
computer_possible_actions = ["rock", "paper", "scissor"]

#Computer chooses a random element of the computer_possible_actions array  
computer_action = random.choice(computer_possible_actions )


#Recorded input from and output from computer formated into a literal string and presented on screen, f allows to input literals and the n allows for space between lines
print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

#This is an if/else statement created to print an battle result/outcome dependent on the user_action and the computer_action 
if user_action == computer_action:
    print(f" Both players selected {user_action}. It's a draw💥 !!")
elif user_action == 'rock':
    if computer_action == "scissor":
      print("Rock beats scissors!! You rock you, you rule!!!!")
    else: 
       print("Paper beats rock..You can't cover up this one, haha ")
elif user_action == 'paper':
    if computer_action == "rock":
      print("Paper beats rock...You're really covering new horizons with this one!!")
    else:
      print("Scissors takes out paper...You didn't make the cut chump, haha")
elif user_action == 'scissor':
     if computer_action == "paper":
      print("Scissors cut paper....You're just a cut above the rest, huh?")
     else:
      print("Rock smashes scissors...This might be rock bottom for you, haha")
