from game_rpg.game import Person, Bcolor


magic = [{'name': 'fire', 'cost': 10, 'dmg': 60},
         {'name': 'thunder', 'cost': 10, 'dmg': 60},
         {'name': 'blizzard', 'cost': 10, 'dmg': 60}]

player = Person(460, 65, 60, 34, magic)


for i in range(0,3):
    print(f'call {i} generate_damage', player.generate_damage())

for i in range(0,3):
    print(f'call {i} generate_spell_damage', player.generate_spell_damage(i))