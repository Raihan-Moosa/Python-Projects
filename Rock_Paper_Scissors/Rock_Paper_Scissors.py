import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [rock,paper,scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

if 0 < user_choice < 2 :
    print("Invalid Input")
else:
    print("You chose:")
    print(options[user_choice])

computer_choice =  random.randint(0,2)
print("Computer chose:")
print(options[computer_choice])

if user_choice == computer_choice:
    print("It's a draw!")

elif (
        (user_choice == 0 and computer_choice == 2) or
        (user_choice == 1 and computer_choice == 0) or
        (user_choice == 2 and computer_choice == 1)
    ):
        print("You win!")
else:
        print("You lose!")




#Attempt 1
# if user_choice == 0:
#     print(rock)
#     if computer_choice == "rock":
#         print(f"Computer chose: {rock}")
#         print("It's a draw!")
#     elif computer_choice == "paper":
#         print(f"Computer chose: {paper}")
#         print("Paper beats Rock, you lose :(")
#     elif computer_choice == "scissors":
#         print(f"Computer chose: {scissors}")
#         print("Rock beats Scissors, you win!")
#
# if user_choice == 1:
#     print(paper)
#     if computer_choice == "rock":
#         print(f"Computer chose: {rock}")
#         print("Paper beats Rock, you win!")
#     elif computer_choice == "paper":
#         print(f"Computer chose: {paper}")
#         print("It's a draw!")
#     elif computer_choice == "scissors":
#         print(f"Computer chose: {scissors}")
#         print("Scissors beats paper, you lose :(")
#
# if user_choice == 2:
#     print(scissors)
#     if computer_choice == "rock":
#         print(f"Computer chose: {rock}")
#         print("Rock beats Scissors, you lose :(")
#     elif computer_choice == "paper":
#         print(f"Computer chose: {paper}")
#         print("Scissors beats paper, you win!")
#     elif computer_choice == "scissors":
#         print(f"Computer chose: {scissors}")
#         print("Its a draw!")
