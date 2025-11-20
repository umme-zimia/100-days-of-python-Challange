print("*** Welcome to the tip calculator ***")
bill =float(input("What was the total bill? $" ))
percentage = input("What percent? 10, 12 or 15?: " )
split = int(input("split between how many people?: " ))

tip= bill*(float(percentage)/100)
each = round((bill+tip)/split,2)

print(f"each person should pay ${each}")