fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")

# Input a Python list of student heights
student_heights = [18, 165, 189, 186, 155, 191, 164, 189] #input().split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇
height_sum = 0
for i in student_heights:
  height_sum += i
print(f"total height = {height_sum}")
print(f"number of students = {len(student_heights)}")
avg_height = height_sum / len(student_heights)
print(f"average height = {round(avg_height)}")


# Input a list of student scores
student_scores = [78, 65, 89, 86, 55, 91, 64, 89] #input().split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])

# Write your code below this row 👇
high_score = 0
for score in student_scores:
  if score > high_score:
    high_score = score
print(f"The highest score in the class is: {high_score}")


# #! For Loop with Range
total_sum = 0
for number in range(1,101):
   total_sum += number
print(total_sum)

## TODO add all the even numbers
target = int(input()) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇
total = 0

for i in range(0, target + 1, 2):
  total += i
print(total)

# Write your code here 👇
fizzbuzz = 20
for i in range(1, fizzbuzz + 1):
  if i % 3 == 0 and i % 5 == 0:
    print("FizzBuzz")
  elif i % 3 == 0:
    print("Fizz")
  elif i % 5 == 0:
    print("Buzz")
  else:
    print(i)