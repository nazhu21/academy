## Data Types

# ! Integers
# print(123)
# print(123_45_456)

# ! Float

# print(154.23)

# ! Boolean

# a = True
# b = False
# print(a)
# # type to check the data type
# print(type(a))

# ? data type conversion
# num_char = len(input("What is your name? "))
# print(type(num_char))
# new_num_char = str(num_char)
# print("Your name has " + new_num_char + " characters.")


# ? other data type conversions
# c = float(123)
# print(type(c))

# print(70 + float("100.5"))
# print(str(70) + str(100))

# TODO: Exercise1
# two_digit_number = input()
# # 🚨 Don't change the code above 👆
# ####################################
# # Write your code below this line 👇
# a = two_digit_number[0]
# b = two_digit_number[1]
# sum = int(a) + int(b)
# print(sum)

##! Mathematical Operations in Python
# print(3 + 5)
# print(7 - 4)
# print(3 * 2)
# print(6 / 3) # division - data type is float
# print(2 ** 3) # exponent
# print("Order '()' 'always left to right' '**' '*/' '+-'")
# print(3*3+3/3-3)

## TODO: exercise2 (BMI)
# # 1st input: enter height in meters e.g: 1.65
# height = input()
# # 2nd input: enter weight in kilograms e.g: 72
# weight = input()
# # 🚨 Don't change the code above 👆

# # Write your code below this line 👇
# bmi = float(weight) / float(height)**2
# print(int(bmi))

##! division other options
# print(8 / 3) # Float
# print(8 // 3) # FLOOR Division
# print(int(8 / 3))
# print(round(8 / 3))
# print(round(8 / 3, 2)) # 2 decimal places

# ##! f-String
# score = 0
# height = 1.8
# iswinning = True
# score += 1
# score += 2
# print(score)
# print(f"Score is {score}, Height is {height}, Winning? {iswinning}")

## TODO: exercise3 Your Life in Weeks
age = input()
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
life_expectancy = 70
life_weeks = life_expectancy * 52
lived_weeks = int(age) * 52
left_weeks = life_weeks - lived_weeks
print(f"You lived {lived_weeks} weeks to this day, and assuming you live to be {life_expectancy} years old, You have {left_weeks} weeks left to live! Each week counts!")

