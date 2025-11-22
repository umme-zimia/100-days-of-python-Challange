import random

names_string = "Angela, Ben, Jenny, Zimia, Ayshee"

names = names_string.split(", ")

random_integer = random.random()
x = int(random_integer*(len(names)))

print(f"{names[x]} is going to buy the meal today! ")






