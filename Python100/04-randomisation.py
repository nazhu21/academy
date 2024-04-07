
## ! Randomisation and Lists in Python
import random
import my_module

random_integer = random.randint(1, 10) # generate random number between 0 and 10, including 10
#print(random_integer)

## ? What is a module?
## complex code gets broken down into modules to build complex projects
#print(my_module.pi)

random_float = random.random() # it's always between 0 and 1, not including 1
print(random_float)
print(random_float * 5) # to generate random floating number between 0 and 5, not including 5

## TODO Heads or Tails
my_module.heads_or_tails()

## ! Python Lists
fruits = ["apple", "banana"] # List data structure

# option z = wrap text to fit screen
us_states = ['Delaware', 'Pennsylvania', 'New Jersey', 'Georgia', 'Connecticut', 'Massachusetts', 'Maryland', 'South Carolina', 'New Hampshire', 'Virginia', 'New York', 'North Carolina', 'Rhode Island', 'Vermont', 'Kentucky', 'Tennessee', 'Ohio', 'Louisiana', 'Indiana', 'Mississippi', 'Illinois', 'Alabama', 'Maine', 'Missouri', 'Arkansas', 'Michigan', 'Florida', 'Texas', 'Iowa', 'Wisconsin', 'California', 'Minnesota', 'Oregon', 'Kansas', 'West Virginia', 'Nevada', 'Nebraska', 'Colorado', 'North Dakota', 'South Dakota', 'Montana', 'Washington', 'Idaho', 'Wyoming', 'Utah', 'Oklahoma', 'New Mexico', 'Arizona', 'Alaska', 'Hawaii']
state_dict = {'AL' : 'Alabama', 'AK' : 'Alaska', 'AZ' : 'Arizona', 'AR' : 'Arkansas', 'CA' : 'California','CO' : 'Colorado', 'CT' : 'Connecticut','DE' : 'Delaware','FL' : 'Florida','GA' : 'Georgia','HI' : 'Hawaii','ID' : 'Idaho','IL' : 'Illinois','IN' : 'Indiana','IA' : 'Iowa','KS' : 'Kansas','KY' : 'Kentucky','LA' : 'Louisiana','ME' : 'Maine','MD' : 'Maryland','MA' : 'Massachusetts','MI' : 'Michigan','MN' : 'Minnesota','MS' : 'Mississippi','MO' : 'Missouri','MT' : 'Montana','NE' : 'Nebraska','NV' : 'Nevada','NH' : 'New Hampshire','NJ' : 'New Jersey','NM' : 'New Mexico','NY' : 'New York','NC' : 'North Carolina','ND' : 'North Dakota','OH' : 'Ohio','OK' : 'Oklahoma','OR' : 'Oregon','PA' : 'Pennsylvania','RI' : 'Rhode Island','SC' : 'South Carolina','SD' : 'South Dakota','TN' : 'Tennessee','TX' : 'Texas','UT' : 'Utah','VT' : 'Vermont','VA' : 'Virginia','WA' : 'Washington','WV' : 'West Virginia','WI' : 'Wisconsin','WY' : 'Wyoming','DC' : 'District of Columbia'}
# us_states[0] = "DeLaware"
# us_states.append("A")
# us_states.extend(["B", "C", "D"])


print(us_states[-1])


## TODO Banker Roulette
names_string = "Naza, Sam, Adi"
names = names_string.split(", ")
players = len(names) - 1
pay_bill = random.randint(0, players)
print(f"{names[pay_bill]} is going to buy the meal today!")

## TODO Treasure Map

line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = "c2" #input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
letter = position[0].lower()
abc = ['a', 'b', 'c']
letter_index = abc.index(letter)
number_index = int(position[1]) - 1
map[number_index][letter_index] = "X"
# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")