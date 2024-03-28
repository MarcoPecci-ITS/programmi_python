import random, time
position = [0, 0] # x, y
player_health = 100
enemy_health = 15
score = 0

def move(direction):
    if 'w' in direction:
        position[0] += 1
    elif 's' in direction:
        position[0] -= 1
    elif 'a' in direction:
        position[1] -= 1
    elif 'd' in direction:
        position[1] += 1
    print(position)

def enemy_attack():
    global player_health
    enemy_damage = random.randint(2, 10)
    player_health -= enemy_damage
    if player_health < 0:
        player_health = 0
    
def player_attack():
    global enemy_health
    player_damage = random.randint(3, 12)
    enemy_health -= player_damage
    if enemy_health < 0:
        enemy_health = 0


in_fight = False
while player_health > 0:
    while not in_fight:
        player_movement = input('Waiting... ')
        move(player_movement)
    
        if True:#random.randint(1, 5) == 5:
            print('You found an enemy! FIGHT!')
            enemy_health = random.randint(15, 25)
            in_fight = True
        
    while in_fight:
        print(f'Player: {player_health}%  -----  Enemy: {enemy_health}')
        enemy_attack()
        player_attack()
        time.sleep(1)
        
        if enemy_health <= 0 and player_health > 0:
            print('You won the fight!')
            score += 1
            in_fight = False
        if player_health <= 0:
            break 

print(f'\nYou died. You defeated {score} enemies.')