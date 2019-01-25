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
    def __init__(self, name, hp, mp, atk, df, magic, itens):
        self.name = name
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.itens = itens
        self.actions = ["Attack", "Magic", "Itens"]

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
        print('\n' + Bcolor.BOLD + self.name + Bcolor.ENDC)
        print(Bcolor.OKBLUE + Bcolor.BOLD + 'ACTIONS' + Bcolor.ENDC)
        for i, item in enumerate(self.actions):
            print(f'\t{i + 1} : {item}')

    def choose_magic(self):
        print('\n' + Bcolor.OKBLUE + Bcolor.BOLD + 'MAGICAL' + Bcolor.ENDC)
        for i, spell in enumerate(self.magic):
            print(f'\t{i+1} : {spell.name} cost = {spell.dmg}')

    def choose_item(self):
        print('\n' + Bcolor.OKGREEN + Bcolor.BOLD + 'Item' + Bcolor.ENDC)
        for i, item in enumerate(self.itens):
            print(f'\t{i+1} : {item["item"].name} type = {item["item"].type} {item["item"].description} '
                  f'prop {item["item"].prop} (x{str(item["quantity"])})')

    def _print_bold_and_color(msg, value1, color1, blocks1, value2, color2, blocks2):
        print(
            Bcolor.BOLD + msg + value1 + color1 + blocks1 + Bcolor.ENDC + value2 + color2 + blocks2 + Bcolor.ENDC + '|')

    @staticmethod
    def print_with_space_after(txt, n):
        i = 0
        while i < n:
            txt += ' '
            i += 1
        return txt

    @staticmethod
    def print_with_space_before(txt, n):
        result = ''
        i = 0
        while i <= n:
            result += ' '
            i += 1
        return result + txt

    def get_stats(self):
        hp_bar = ''
        bar_ticks = (self.hp / self.maxhp) * 100 / 4

        while bar_ticks > 0:
            hp_bar += '█'
            bar_ticks -= 1

        while len(hp_bar) < 25:
            hp_bar += ' '

        mp_bar = ''
        mp_ticks = (self.mp / self.maxmp) * 100 / 10

        while mp_ticks > 0:
            mp_bar += '█'
            mp_ticks -= 1

        while len(mp_bar) < 10:
            mp_bar += ' '

        print('                       _________________________               __________ ')
        print(self.name + ':  ' + self.print_with_space_before(str(self.get_hp()),4) + '/' + str(self.get_max_hp())
              + " |" + Bcolor.OKGREEN + hp_bar + Bcolor.ENDC + '|  ' +
              self.print_with_space_before(str(self.get_mp()),3) + '/' + str(self.get_max_mp()) + ' |'
              + Bcolor.OKBLUE + mp_bar + Bcolor.ENDC + '|')
