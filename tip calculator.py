print("Welcome to Tip Calculator")
bill = float(input("What was the total bill? $"))
tip_percentage = (float(input("What percentage tip would you like to give? 10, 12, 0r 15 "))) / 100
people = int(input("How many people to split the bill "))
tip = (bill * tip_percentage)
per_person = ((bill + tip) / people)
total = round(per_person, 2)
total = "{:.2f}".format(per_person)
print(f"Each person will pay ${total}")

