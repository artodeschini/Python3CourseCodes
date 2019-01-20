from game_rpg.game import Person, Bcolor


magic = [{'name': 'fire', 'cost': 10, 'dmg': 100},
         {'name': 'thunder', 'cost': 10, 'dmg': 135},
         {'name': 'blizzard', 'cost': 10, 'dmg': 100}]

player = Person(460, 65, 60, 34, magic)
enemy = Person(1200, 65, 45, 25, magic)

running = True

print(Bcolor.FAIL + Bcolor.BOLD + 'AN ENEMY ATTACK' + Bcolor.ENDC)

while running:
    print('================================')
    player.choose_action()
    choose = input('Choose an action:')
    print(f'You choose a {choose}')
    index = int(choose) - 1

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print(f'You attack for {dmg} points in enemy. Hp for enemy is {enemy.get_hp()}')
    elif index == 1:
        player.choose_magic()
        magic_choose = int(input('Choose magic')) - 1
        magic_dmg = player.generate_spell_damage(magic_choose)
        spell_name = player.get_spell_name(magic_choose)
        cost = player.get_spell_cost(magic_choose)

        current_mp = player.get_mp()

        if cost > current_mp:
            print(Bcolor.FAIL + 'Not enough MP' + Bcolor.ENDC)
            continue

        player.reduce_mp(cost)
        enemy.take_damage(magic_dmg)
        print(Bcolor.OKBLUE + spell_name + ' deals ' + str(magic_dmg) + ' 2points damage in the enemy' + Bcolor.ENDC)

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
