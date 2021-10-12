from classes import *
from random import randint
def splash():
    print('\n\n  ____        _   _   _      _                    \n |  _ \      | | | | | |    | |                   \n | |_) | __ _| |_| |_| | ___| |_ _   _ _ __ _ __  \n |  _ < / _` | __| __| |/ _ \ __| | | | \'__| \'_ \ \n | |_) | (_| | |_| |_| |  __/ |_| |_| | |  | | | |\n |____/ \__,_|\__|\__|_|\___|\__|\__,_|_|  |_| |_|\n                                                  \n                                                  \n')

def viewOptions(dictionary):
    items = 'Possible options:\n\n'
    for key, value in dictionary.items():
        items += f'   {key}:\n'
        for i in range(len(value)):
            items += f'    {i+1}: {value[i]}\n'
    print(items)

def menu(title, prompt, options):
    print(f'{title}\n')
    for key, value in options.items():
        print(f'   {key}) {value}')
    print()
    while True:
        usr_choice = input(prompt)
        if usr_choice in options:
            return usr_choice

def battle(player, enemy):
    def attack(attacker, target):
        def hit_or_miss(weapon_accuracy):
            if randint(1, 100) <= weapon_accuracy:
                return True
            else:
                return False

        def damage_multiplier(attacker_weapon_type, target_weakness, target_resistance):
            if attacker_weapon_type == target_weakness:
                #return randint(150, 250)
                return 200
            elif attacker_weapon_type == target_resistance:
                #return randint(25, 75)
                return 100
            else:
                return 100
        
        if hit_or_miss(attacker.weapon.accuracy):
            attack_damage = attacker.weapon.damage * (damage_multiplier(attacker.weapon.type, target.weakness, target.resistance)/100)
            target.health = target.health - attack_damage
            print(f'Hit! {attacker.name} hits {target.name} for {attack_damage} damage.')
        else:
            print(f'Miss! {target.name} evades {attacker.name}\'s attack.')

    def who_starts(player, enemy):
        if enemy.speed > player.speed:
            return 2
        elif enemy.speed < player.speed:
            return 1
        else:
            return randint(1, 2)
    
    def print_turn(who_started, turn):
        if who_started == 2:
            print(f'Turn {turn - 1}')
        else:
            print(f'Turn {turn}')
    
    def use_item(player):
        item_menu = player.get_Inventory_to_Dictionary()
        user_choice = menu('What item would you like to use?', 'Option: ', item_menu)
        for index, item in item_menu.items():
            if user_choice == index:
                item_effect = player.inventory[int(index) - 1].effect
                player.health += item_effect
                print(f'{player.name} used {item} and gained +{item_effect} health! {player.health - item_effect} --> {player.health}')
                del player.inventory[int(index) - 1]
                return True
            elif user_choice == 'q':
                return False
    turn = who_starts(player, enemy)
    while True:
        print_turn(who_starts, turn)
        print(f'{player.name}\'s Health: {player.health}\n{enemy.name}\'s Health: {enemy.health}')
        if turn % 2 != 0:
            print(f'{player.name}\'s turn')
            while True:
                battle_menu = {'1':'Attack!', '2':'Use item'}
                user_choice = menu('What do you want to do?', 'Option: ', battle_menu)
                if user_choice == '1':
                    attack(player, enemy)
                    break
                elif user_choice == '2':
                    if use_item(player):
                        break
        else:
            print(f'{enemy.name}\'s turn')
            attack(enemy, player)
        if player.health <= 0:
            return False
        elif enemy.health <= 0:
            return True
        turn += 1
        print()

#def new_Room():
#    def generate_Room():
#        room = []
#        if randint(0,1):
#            

all_players_stats = ['Name', 'Health', 'Damage', 'Weapon']

while True: #Gameloop
    splash()
    player = Player('Erik', 100, [healthPotion_Large, healthPotion_Small, healthPotion_Large], Fist, None, None, 10)

    #Fight
    battle(player, Orc_noob)
    break

