import random

names_string = "Naza, Sam, Adi"
names = names_string.split(", ")
players = len(names) - 1
pay_bill = random.randint(0, players)
print(f"{names[pay_bill]} is going to buy the meal today!")