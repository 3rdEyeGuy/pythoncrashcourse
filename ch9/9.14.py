from random import randint

class Die():
    def __init__(self,sides = 6):
        self.sides = sides

    def roll_die(self):
        self.dieRolls = 10
        print()
        print('***', str(self.sides), 'sided die ***')
        for i in range(self.dieRolls):
            print('roll', str(1+i) +':', str(randint(1,self.sides)))

sixDie = Die()
sixDie.roll_die()

tenDie = Die(10)
tenDie.roll_die()

twentyDie = Die(20)
twentyDie.roll_die()
print()
