from game_rpg.game import Person, Bcolor


magic = [{'name': 'fire', 'cost': 10, 'dmg': 60},
         {'name': 'thunder', 'cost': 10, 'dmg': 60},
         {'name': 'blizzard', 'cost': 10, 'dmg': 60}]

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

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print(f'Enemy attack for {enemy_dmg} points in you. Your hp is {player.get_hp()}')

    running = False
