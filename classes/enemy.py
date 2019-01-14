class Enemy:
    def __init__(self, hp, mp):
        self.hp = hp
        self.max_hp = hp
        self.mp = mp
        self.max_mp = mp

    def get_hp(self):
        return self.hp
