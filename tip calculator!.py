print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? "))
people = int(input("How many people to split the bill? "))

tip_to_decimal = tip / 100 * bill / people
amount = round(tip_to_decimal, 2)

print(amount)