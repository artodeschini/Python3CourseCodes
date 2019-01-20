import random


class Bcolor:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Person:
    def __init__(self, hp, mp, atk, df, magic):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.actions = ["Attack", "Magic"]

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def take_damage(self, dmg):
        self.hp -= dmg

        if self.hp < 0:
            self.hp = 0

        return self.hp

    def set_hp(self, more):
        self.hp += more

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

        return self.mp

    def choose_action(self):
        print('Actions')
        for i, item in enumerate(self.actions):
            print(Bcolor.OKBLUE + Bcolor.BOLD + f'{i + 1} : {item}' + Bcolor.ENDC)

    def choose_magic(self):
        print('Magical')
        for i, spell in enumerate(self.magic):
            print(Bcolor.OKGREEN + Bcolor.BOLD + f'{i+1} : {spell.name} cost = {spell.dmg}' + Bcolor.ENDC)