print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size of pizza? S, M, or L: ").upper() # What size pizza do you want? S, M, or L
add_pepperoni = input("Add pepperoni? Y or N: ").upper() # Do you want pepperoni? Y or N
extra_cheese = input("Add extra cheese? Y or N: ").upper() # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

price = 0

if size == "S":
    price = 15
    print(f"Small pizza (S): ${price}")
    if add_pepperoni == "Y":
        price += 2
elif size == "M":
    price = 20
    print(f"Medium pizza (M): ${price}")
    if add_pepperoni == "Y":
        price += 3
elif size == "L":
    price = 25
    print(f"Large pizza (L): ${price}")
    if add_pepperoni == "Y":
        price += 3
else:
    None

if extra_cheese == "Y":
    price += 1
print(f"Thank you for choosing Python Pizza Deliveries!\nYour final bill is: ${price}")