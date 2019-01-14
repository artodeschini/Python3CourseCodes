import random


class Enemy:

    enemyatkl = 60
    enemyatkh = 80

    def get_attackl(self):
        print(self.enemyatkl)

    def get_attackh(self):
        print(self.enemyatkh)


e = Enemy()
e.get_attackl()
e.get_attackh()