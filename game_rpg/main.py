from game_rpg.game import Person, Bcolor
from game_rpg.magic import Spell
from game_rpg.inventory import Item


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
player = Person(460, 65, 60, 34, player_spells, player_itens)
enemy = Person(1200, 65, 45, 25, [], [])

running = True

print(Bcolor.FAIL + Bcolor.BOLD + 'AN ENEMY ATTACK' + Bcolor.ENDC)

while running:
    print('================================')
    player.choose_action()
    choose = input('Choose an action:')
    print(f'You choose a {choose} \n')
    index = int(choose) - 1

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print(f'You attack for {dmg} points in enemy. Hp for enemy is {enemy.get_hp()}')

    elif index == 1:
        player.choose_magic()
        magic_choose = int(input('Choose magic')) - 1

        if magic_choose == -1:
            continue

        spell = player.magic[magic_choose]
        magic_change = spell.generate_damage()

        current_mp = player.get_mp()

        if spell.cost > current_mp:
            print(Bcolor.FAIL + 'Not enough MP' + Bcolor.ENDC)
            continue

        player.reduce_mp(spell.cost)

        if spell.type == 'white':
            player.set_hp(magic_change)
            print(Bcolor.OKBLUE + Bcolor.BOLD + spell.name +
                  ' heal you for ' + str(magic_change) + '. HP is ' + str(player.get_hp()) + Bcolor.ENDC)
        elif spell.type == 'black':
            enemy.take_damage(magic_change)
            print(Bcolor.OKBLUE + spell.name + ' deals '
                  + str(magic_change) + ' 2 points damage in the enemy' + Bcolor.ENDC)

    elif index == 2:
        player.choose_item()
        item_chooise = int(input('Choose a item')) - 1

        if item_chooise == -1:
            continue

        item = player.itens[item_chooise]['item']
        player.itens[item_chooise]['quantity'] -= 1

        if player.itens[item_chooise]['quantity'] == 0:
            print('\n' + Bcolor.FAIL + Bcolor.BOLD + 'None left ...' + Bcolor.ENDC)
            continue

        if item.type == 'potion':
            player.set_hp(item.prop)
            print('\n' + Bcolor.OKGREEN + Bcolor.BOLD + item.name +
                  ' heals for ' + str(item.prop) + ' HP ' + Bcolor.ENDC)

        elif item.type == 'elixir':
            player.hp = player.get_max_hp()
            player.mp = player.get_max_mp()
            print('\n' + Bcolor.OKGREEN + Bcolor.BOLD + item.name +
                  ' heals for ' + str(item.prop) + ' full restore HP/MP ' + Bcolor.ENDC)

        elif item.type == 'attack':
            enemy.take_damage(item.prop)
            print('\n' + Bcolor.FAIL + Bcolor.BOLD + item.name +
                  ' heals for ' + str(item.prop) + ' deals ' + str(item.prop) +
                  ' points of damage' + Bcolor.ENDC)

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print(f'Enemy attack for {enemy_dmg} points in you. Your hp is {player.get_hp()}')

    print('Enemy HP:' + Bcolor.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + Bcolor.ENDC)
    print('Your HP:' + Bcolor.OKGREEN + str(player.get_hp()) + "/" + str(player.get_max_hp()) + Bcolor.ENDC)
    print('Your MP:' + Bcolor.OKBLUE + str(player.get_mp()) + "/" + str(player.get_max_mp()) + Bcolor.ENDC)

    if enemy.get_hp() == 0:
        print(Bcolor.OKGREEN + 'You win' + Bcolor.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(Bcolor.FAIL + 'You loose' + Bcolor.ENDC)
        running = False
