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

game_images = [rock,paper,scissors]
my_choice = int(input("0 = Rock, 1 = Paper, 2 = Scissors\n"))
print("You Chose: ")
print(game_images[my_choice])

random_integer = random.random()
comp_chose = int(random_integer*3)

print("Computer Chose: ")

print(game_images[comp_chose])

if my_choice >= 3 or my_choice < 0:
    print("Invalid Number! You LOSE")
elif my_choice == 0 and comp_chose == 2:
    print("You win!")
elif comp_chose ==0 and my_choice ==2:
    print("You lose!")
elif comp_chose > my_choice:
    print("You lose!")
elif comp_chose < my_choice:
    print("You Win!")
elif comp_chose == my_choice:
    print("Draw!")


