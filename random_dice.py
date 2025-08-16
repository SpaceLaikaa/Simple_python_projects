import random

how_many = int((input("How many dices you want to roll: ")))


for i in range(how_many):
    random_dice = random.randint(1, 6)
    print(random_dice)



