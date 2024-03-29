# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

# if height >= 120:
#     print("You can ride the rollercoaster!")
# else:
#     print("Sorry, you have togrow taller before you can ride.")

## ! Comparison Operators
# <, >, =, >=, <=, ==, !=

## TODO: even or odd numbers
# # Which number do you want to check?
# number = int(input())
# # 🚨 Don't change the code above 👆

# # Write your code below this line 👇
# a = number
# if a%2==0:
#     print("This is an even number.")
# else:
#     print("This is an odd number.")

## ? Nested if/else statements
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

# if height >= 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("What is your age? "))
#     if age < 12:
#         print("Please pay $5")
#     elif age <= 18:
#         print("Please pay $7")
#     else:
#         print("Please pay $12")
# else:
#     print("Sorry, you have to grow taller before you can ride.")

## TODO: BMI 2.0
# Enter your height in meters e.g., 1.55
height = float(input("Height in meters: "))
# Enter your weight in kilograms e.g., 72
weight = int(input("Weight in kilograms: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = round(weight / float(height)**2, 2)
if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")

# ## TODO: Leap year?
# year = 2000#int(input())

# if year % 4 == 0:
#     # leap year 
#     if year % 100 == 0:
#         # not a leap year

#         if year % 400 == 0:
#             # leap year
#             print("Leap year")
#         else:
#             print("Not leap year")

#     else:
#         print("Leap year")
# else:
#     print("Not leap year")


## TODO: Leap Year?
year1 = int(input("Year: "))
if (year1 % 4 == 0 and year1 % 100 != 0) or (year1 % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")


# #! Multiple If Statements in Succession
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7")
    else:
        bill = 12
        print("Adult tickets are $12")
    
    wants_photo = input("Do you want a photo taken? Y or N. ").upper()
    if wants_photo == "Y":
        bill += 3
    
    print(f"Your final bill is ${bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")