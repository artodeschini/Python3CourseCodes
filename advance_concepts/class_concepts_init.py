"""
    Program Enemy
    Author: Artur Todeschni Crestani

    This is a comment for multiple line
"""


class Enemy:

    def __init__(self, enemyatkl, enemyatkh):
        self.enemyatkl = enemyatkl
        self.enemyatkh = enemyatkh

    # this a comment for unique line
    def get_attackl(self):
        print(self.enemyatkl)

    def get_attackh(self):
        print(self.enemyatkh)


e = Enemy(60, 80)
e.get_attackl()
e.get_attackh()