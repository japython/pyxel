import random

class Dice:
    def __init__(self,val):
        self.face_num = val
        
    def shoot(self):
        return random.randint(1, self.face_num)
