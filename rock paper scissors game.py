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

# listing the choices
rps = [rock, paper, scissors]

# welcoming part of the game
print("Welcome to the Rock Paper Scissors Game!")

# input choice area for the user
choice = int(input("Please Choose your favourite option: 0 for Rock, 1 for Paper and 3 for scissors: "))

# computer's play and choice
comp_choice = random.randint(0,2)
# if comp_choice == 0:
#     print(f"The computer chooses: {rock}")
# elif comp_choice == 1:
#     print(f"The computer chooses: {paper}")
# else:
#     print(f"The computer chooses: {scissors}")


# if logic for the user's play

if choice == 0:
    print(f"You have chosen: \n {rps[choice]}")
    if comp_choice == 0:
        print(f"The computer has played: \n {rps[comp_choice]} \n You have come to a draw with the Computer!")
    elif comp_choice == 1:
        print(f"The computer has played: \n {rps[comp_choice]} \n You have lost and the computer wins!")
    elif comp_choice == 2:
        print(f"The computer has played: \n {rps[comp_choice]} \n You have won! and the computer lost!")
elif choice == 1:
    print(f"You have chosen: \n {rps[choice]}")
    if comp_choice == 0:
        print(f"The computer has played: \n {rps[comp_choice]} \n You have won! and the computer lost!")
    elif comp_choice == 1:
        print(f"The computer has played: \n {rps[comp_choice]} \n You have come to a draw with the Computer!")
    elif comp_choice == 2:
        print(f"The computer has played: \n {rps[comp_choice]} \n You have lost and the computer wins!")
elif choice == 2:
    print(f"You have chosen: \n {rps[choice]}")
    if comp_choice == 0:
        print(f"The computer has played: \n {rps[comp_choice]} \n You have lost and the computer wins!")
    elif comp_choice == 1:
        print(f"The computer has played: \n {rps[comp_choice]} \n You have won! and the computer lost!")
    elif comp_choice == 2:
        print(f"The computer has played: \n {rps[comp_choice]} \n You have come to a draw with the Computer!")
else:
    print("Please enter a valid choice from instructions given!")