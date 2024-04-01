import random

pi = 3.14

random_side = random.randint(0, 1)

def heads_or_tails():
    if random_side == 1:
        print("Heads")
    else:
        print("Tails")

heads_or_tails()