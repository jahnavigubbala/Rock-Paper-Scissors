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

user = input("Rock, Paper, Scissors. 0 for Rock, 1 for Paper, 2 for Scissors.\n")
user = int(user)
print("User:")
if user==0:
  print(rock)
elif user==1:
  print(paper)
else:
  print(scissors)

print("Computer:")
w = random.randint(0,2)
if w==0:
  print(rock)
elif w==1:
  print(paper)
else:
  print(scissors)

if user==w:
  print("Draw")
elif user <w:
  if w==2 and user==0:
    print("You win")
  else:
    print("You lose")
else:
  if user==2 and w==0:
    print("You lose")
  else:
    print("You win")
