import random

print("ROCK, PAPER, SCISSORS.")
a_user = input("Type 0 for Rock, 1 for Paper, 2 for Scissors.\n")
a_comp = random.randint(0,2)

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

if a_user == "0":
    print(f"User: {rock}")
elif a_user == "1":
    print(f"User: {paper}")
elif a_user == "2":
    print(f"User: {scissors}")
else:
    print("Invalid Input")

if a_comp == 0:
    print(f"Computer: {rock}")
elif a_comp == 1:
    print(f"Computer: {paper}")
elif a_comp == 2:
    print(f"Computer: {scissors}")
else:
    print("Error1")

if a_user == "0":
    if a_comp == 0:
        print("It's a tie")
    elif a_comp == 1:
        print("You Lose! Computer Wins")
    elif a_comp == 2:
        print("You Win! Computer Lost")
    else:
        print("Error2")
elif a_user == "1":
    if a_comp == 0:
        print("You Win! Computer Lost")
    elif a_comp == 1:
        print("It's a tie")
    elif a_comp == 2:
        print("You Lose! Computer Wins")
    else:
        print("Error3")
elif a_user == "2":
    if a_comp == 0:
        print("You Lose! Computer Wins")
    elif a_comp == 1:
        print("You Win! Computer Lost")
    elif a_comp == 2:
        print("It's a tie")
    else:
        print("Error4")
else:
    print("Error5")
