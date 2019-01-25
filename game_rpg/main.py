from game_rpg.game import Person, Bcolor
from game_rpg.magic import Spell
from game_rpg.inventory import Item


def _print_blue_msg(msg):
    print(Bcolor.OKBLUE + Bcolor.BOLD + msg + Bcolor.ENDC)


def _print_red_msg(msg):
    print(Bcolor.FAIL + Bcolor.BOLD + msg + Bcolor.ENDC)


def _print_green_msg(msg):
    print(Bcolor.OKGREEN + Bcolor.BOLD + msg + Bcolor.ENDC)


# black magic
fire = Spell('fire', 10, 100, 'black')
thunder = Spell('thunder', 10, 150, 'black')
blizzard = Spell('blizzard', 10, 165, 'black')
meteor = Spell('Meteor', 20, 200, 'black')
quake = Spell('quake', 14, 140, 'black')

# white magic
cure_small = Spell('cure', 12, 120, 'white')
cure_large = Spell('cure', 18, 200, 'white')

# create some itens
potion = Item('Potion', 'potion', 'Heals 50 HP', 50)
high_potion = Item('High Potion', 'potion', 'Heals 100 HP', 100)
super_potion = Item('Super Potion', 'potion', 'Heals 500', 500)
elixir = Item('Elixir', 'elixir', 'Restore HP/MP of one part member', 99999)
high_elixir = Item('High Elixir', 'elixir', 'Fully restore partys HP/MP', 99999)
grenade = Item('Grenade', 'attack', 'Deals 500 damage', 500)

player_spells = [fire, thunder, blizzard, meteor, quake, cure_small, cure_large]
player_itens = [{'item': potion, 'quantity': 15}, {'item': high_potion, 'quantity': 5},
                {'item': super_potion, 'quantity': 5}, {'item': elixir, 'quantity': 5},
                {'item': high_elixir, 'quantity': 2}, {'item': grenade, 'quantity': 5}]

# instance of player
player1 = Person('Artur', 3260, 132, 60, 34, player_spells, player_itens)
player2 = Person('Catia', 4160, 188, 60, 34, player_spells, player_itens)
player3 = Person('Manu ', 3460, 165, 60, 34, player_spells, player_itens)

players = [player1, player2, player3]

enemy = Person('Dark Soul',1200, 65, 450, 25, [], [])

running = True

print(Bcolor.FAIL + Bcolor.BOLD + 'AN ENEMY ATTACK' + Bcolor.ENDC)

while running:
    print('NAMES:                 HP                                      MP          ')
    for player in players:
        player.get_stats()

    for player in players:
        print('\n\n')
        player.get_stats()
        print('\n')

        player.choose_action()
        choose = input('Choose an action:')
        index = int(choose) - 1

        if index == 0:
            dmg = player.generate_damage()
            enemy.take_damage(dmg)
            print()
            _print_blue_msg(f'You attack for {dmg} points in enemy. Hp for enemy is {enemy.get_hp()})')

        elif index == 1:
            player.choose_magic()
            magic_choose = int(input('Choose magic')) - 1

            if magic_choose == -1:
                continue

            spell = player.magic[magic_choose]
            magic_change = spell.generate_damage()

            current_mp = player.get_mp()

            if spell.cost > current_mp:
                _print_red_msg('Not enough MP')
                continue

            player.reduce_mp(spell.cost)

            if spell.type == 'white':
                player.set_hp(magic_change)
                _print_blue_msg(spell.name + ' heal you for ' + str(magic_change) + '. HP is ' + str(player.get_hp()))
            elif spell.type == 'black':
                enemy.take_damage(magic_change)
                _print_blue_msg(spell.name + ' deals ' + str(magic_change) + ' 2 points damage in the enemy')

        elif index == 2:
            player.choose_item()
            item_chooise = int(input('Choose a item')) - 1

            if item_chooise == -1:
                continue

            item = player.itens[item_chooise]['item']

            if player.itens[item_chooise]['quantity'] == 0:
                _print_red_msg('\nNone left ...')
                continue

            player.itens[item_chooise]['quantity'] -= 1

            if item.type == 'potion':
                player.set_hp(item.prop)
                _print_green_msg('\n' + item.name + ' heals for ' + str(item.prop) + ' HP ')

            elif item.type == 'elixir':
                player.hp = player.get_max_hp()
                player.mp = player.get_max_mp()
                _print_green_msg('\n' + item.name + ' heals for ' + str(item.prop) + ' full restore HP/MP ')

            elif item.type == 'attack':
                enemy.take_damage(item.prop)
                _print_red_msg('\n' + item.name + ' heals for ' + str(item.prop) + ' deals ' + str(item.prop) +
                               ' points of damage')

        enemy_dmg = enemy.generate_damage()
        player.take_damage(enemy_dmg)
        _print_red_msg(f'Enemy attack for {enemy_dmg} points in you. Your hp is {player.get_hp()}')

        _print_red_msg('Enemy HP:' + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()))
        _print_green_msg('Your HP:' + str(player.get_hp()) + "/" + str(player.get_max_hp()))
        _print_blue_msg('Your MP:' + str(player.get_mp()) + "/" + str(player.get_max_mp()))

    if enemy.get_hp() == 0:
        _print_green_msg('You win')
        running = False
    elif player.get_hp() == 0:
        _print_red_msg('You loose')
        running = False
