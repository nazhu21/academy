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

#Write your code below this line 👇

rock_paper_scissors = [rock, paper, scissors]

your_choice = int(input("Type 0 for Rock, 1 for Paper or 2 for Scissors "))

computer_choice = random.randint(0, 2)


# if your_choice >= 3 or your_choice < 0:
#     print("You chose a wrong number, you lose")
# else:
#     print(f"You chose:\n {rock_paper_scissors[your_choice]}")
#     print(f"Computer chose:\n {rock_paper_scissors[computer_choice]}")
#     if your_choice == 0 and computer_choice == 1:
#         print("You lose")
#     elif your_choice == 0 and computer_choice == 2:
#         print("You win")
#     elif your_choice == 1 and computer_choice == 0:
#         print("You win")
#     elif your_choice == 1 and computer_choice == 2:
#         print("You lose")
#     elif your_choice == 2 and computer_choice == 0:
#         print("You lose")
#     elif your_choice == 2 and computer_choice == 1:
#         print("You win")
#     elif your_choice == computer_choice:
#         print("You draw")


if your_choice >= 3 or your_choice < 0:
    print("You chose a wrong number, you lose")
else:
    print(f"You chose:\n {rock_paper_scissors[your_choice]}")
    print(f"Computer chose:\n {rock_paper_scissors[computer_choice]}")
    if your_choice == 0 and computer_choice == 2:
        print("You win!")
    elif your_choice == 2 and computer_choice == 0:
        print("You lose!")
    elif your_choice > computer_choice:
        print("You win")
    elif your_choice < computer_choice:
        print("You lose")
    elif your_choice == computer_choice:
        print("You draw")