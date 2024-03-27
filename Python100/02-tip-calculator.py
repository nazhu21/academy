
##! Project Tip Calculator

bill = float(input("Welcome to the tip calculator!\nWhat is the total bill? $"))
tip_percent = int(input("How much tip would you like to give? 10, 12, or 15? "))
split_bill = int(input("How many people to split the bill? "))
bill_total = round(bill * ((tip_percent / 100) + 1), 2)
each_pay = "{:.2f}".format(bill_total / split_bill)
print(f"Your total bill is ${bill_total}\nEach person should pay: ${each_pay}")