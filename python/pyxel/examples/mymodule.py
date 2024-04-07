import random

class Dice:
    face_num = 6
    def shoot(self):
        return random.randint(1, 6)
