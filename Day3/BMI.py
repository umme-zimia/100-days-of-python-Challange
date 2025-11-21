height = float(input())
weight = int(input())

bmi = round(weight/height**2,2)

if bmi<=18.5:
    print(f"your {bmi} bmi is underweight")
elif bmi<=25:
    print(f"your {bmi} bmi is Normal weight")
elif bmi<=30:
    print(f"your {bmi} bmi is Slightly Overweight")
elif bmi<=35:
    print(f"your {bmi} bmi is Obese")
else:
    print(f"your {bmi} bmi is clinically obese")