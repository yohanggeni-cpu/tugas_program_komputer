from random import randint

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        result = randint(1, self.sides)
        print(result)
        return result

for sides in (6, 10, 20):
    print(f"\nDadu {sides} sisi:")
    die = Die(sides)
    for _ in range(10):
        die.roll_die()
