import random


playerhp = 260
enemyatkl = 60
enemyatkh = 80

while playerhp > 0:
    dmg = random.randrange(enemyatkl,enemyatkh)
    playerhp = playerhp - dmg

    if playerhp <= 30:
        playerhp = 30

    print('Enemy striker for ', dmg, 'points of damage. Current HP is', playerhp)

    if playerhp == 30:
        print("You have low health. You've been teleported, as you to the near inn")
        break