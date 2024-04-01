
## ! Randomisation and Lists in Python
import random
import my_module

random_integer = random.randint(1, 10)
print(random_integer)

## ? What is a module?
## complex code gets broken down into modules to build complex projects
print(my_module.pi)

random_float = random.random() # it's always between 0 and 1, not including 1
print(random_float)
print(random_float * 5) # to generate random floating number between 0 and 5, not including 5
