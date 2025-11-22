print("Love Calculator")
name1 = input("what is your name?: ")
name2 = input("what is your crush's name?: ")

combine_names= name1+name2
# print(combine_names)

lower_names = combine_names.lower()
# print(lower_names)

t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")

digit1 = t+r+u+e
digit2 = l+o+v+e
score = int(str(digit1)+str(digit2))

# print(score)

if score<10 or score > 90:
    print(f"Your score is \"{score}\" You go together like coke and mentos")
elif score>=40 and score<=50:
    print(f"Your score is \"{score}\" You are alright together")
else:
    print(f"Your score is \"{score}\"")
    



