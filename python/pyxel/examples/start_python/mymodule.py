import random

class Dice:
    def __init__(self,val=6):
        self.face_num = val  
        # Set the number of faces to 6 by default. If a different number is provided, it will be used instead. 6 is a common choice for a standard six-sided die. 
        # 12, 20, 24, 30, 40, or any other number of faces can be used as well. 12-sided dice are also known as d12, d12+1, d12c, and d12s. 20-sided dice are known as d20. 24-sided dice are known as d24. 30-sided dice are known as d30. 40-sided dice are known as d40. 100-sided dice are known as d100. 1000-sided dice are known as d100

    def shoot(self):
        return random.randint(1, self.face_num)
