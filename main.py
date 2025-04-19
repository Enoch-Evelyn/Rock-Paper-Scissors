import random 

# This input is where the user chooses what weapon to use
user_action = input("Enter Choice( rock, paper, scissor):")

computer_possible_actions = ("rock, paper, scissor")

computer_action = random.choice(computer_possible_actions )

print(user_action)

print(computer_possible_actions)