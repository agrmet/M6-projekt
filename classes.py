from random import randint

class Player:
    def __init__(self, name, health, inventory, weapon, weakness, resistance, speed):
        self.name = name
        self.health = health
        self.inventory = inventory
        self.weapon = weapon
        self.weakness = weakness
        self.resistance = resistance
        self.speed = speed
    def add_Item(self, item):
        item_Dict = {'Health Potion':0,'Mana Potion':1}
        if self.inventory[item_Dict[item]] < 3:
            self.inventory[item_Dict[item]] += 1
            print(f"{item} has been added to your inventory")
        else:
            print(f'You already have 3 {item}!')
    
    def view_inventory(self):
        inventory_Dict = {0:'Health Potion(s)', 1:'Attack Potion(s)'}
        items = "Inventory:\n\n"
        for i in range(len(self.inventory)):
            items += f'{ inventory_Dict[i]}: {self.inventory[i]}\n'
        print(items)

    def view_Stats(self, arguments):
        stats = {'name':self.name, 'health':self.health, 'damage':self.weapon.damage, 'weapon':self.weapon.name, 'weakness':self.weakness, 'resistance':self.resistance, 'speed':self.speed}
        s = ''
        for i in range(len(arguments)):
            s += f' {arguments[i]}: {stats[arguments[i].lower()]}\n'
        print(s)
    
    def get_Stat(self, arguments): #Return chosen player stat(s)
        stats = {'name':self.name, 'health':self.health, 'damage':self.weapon.damage, 'weapon':self.weapon.name, 'weakness':self.weakness, 'resistance':self.resistance, 'speed':self.speed}
        lst = []
        for i in range(len(arguments)):
            lst.append(stats[arguments[i].lower()])
        return lst

    def view_Inventory(self):
        inventory = self.inventory
        if not inventory:
            print('Your inventory is empty!')
        else:
            s = f'{self.name}\'s inventory:\n'
            for i in range(len(inventory)):
                s += f' {i + 1}) {inventory[i].name}\n'
            print(s)

    def get_Inventory_to_Dictionary(self):
        inventory = {}
        count = 1
        for i in self.inventory:
            inventory[str(count)] = i.name
            count += 1
        inventory['q'] = 'Close inventory'
        return inventory

class Enemy:
    def __init__(self, race, name, health, weakness, resistance, weapon, speed):
        self.race = race
        self.name = name
        self.health = health
        self.weakness = weakness
        self.resistance = resistance
        self.weapon = weapon
        self.speed = speed

    def view_Stats(self, arguments):
        stats = {'race':self.race, 'name':self.name, 'health':self.health, 'weakness':self.weakness, 'resistance': self.resistance, 'damage':self.weapon.damage, 'speed':self.speed}
        s = ''
        for i in range(len(arguments)):
            s += f' {arguments[i]}: {stats[arguments[i].lower()]}\n'
        print(s)

    def get_Stat(self, arguments): #Return chosen player stat(s)
        stats = {'name':self.name, 'health':self.health, 'weakness':self.weakness, 'resistance': self.resistance,'damage':self.weapon.damage, 'speed':self.speed}
        lst = []
        for i in range(len(arguments)):
            lst.append(stats[arguments[i].lower()])
        return lst

class Weapon:
    def __init__(self, name, damage, type, accuracy, rarity):
        self.name = name
        self.damage = damage
        self.type = type
        self.accuracy = accuracy
        self.rarity = rarity

    def view_Stats(self, arguments):
        stats = {'name':self.name, 'health':self.health, 'weakness':self.weakness, 'weapon':self.weapon}
        s = ''
        for i in range(len(arguments)):
            s += f' {arguments[i]}: {stats[arguments[i].lower()]}\n'
        return s

#class DamageTypes: Could be good for later if we want implement damage effects etc
#    def __init__(self, type):
#        self.type = type

class Rarities:
    def __init__(self, rarity, probabilty):
        self.rarity = rarity
        self.probabilty = probabilty

class Potion:
    def __init__(self, name, effect, rarity):
        self.name = name
        self.effect = effect #Int that determines how much health the user will restore
        self.rarity = rarity #Int that determines the probabilty of spawning


#Damage Types
#Blunt = DamageTypes('Blunt')
#Piercing = DamageTypes('Piercing')
#Fire = DamageTypes('Fire')

#Rarities
Legendary = Rarities('Legendary', 1)
Rare = Rarities('Rare', 3)
Average = Rarities('Average', 5)
Common = Rarities('Common', 8)


#Potions
healthPotion_Max = Potion("Maximum Health Potion", 100, Legendary)
healthPotion_Large = Potion("Large Health Potion", 60, Rare)
healthPotion_Medium = Potion("Medium Health Potion", 40, Average)
healthPotion_Small = Potion("Small Health Potion", 20, Common)

potions = [healthPotion_Small, healthPotion_Medium, healthPotion_Large, healthPotion_Max]
lst = []
for x in potions:
    for i in range(x.rarity.probabilty):
        lst.append(x)
potions = lst

#Weapons
Fist = Weapon("Fist", 15, 'Blunt', 80, Common)
Sword = Weapon('Sword', 20, 'Piercing', 90, Rare)

weapons = [Fist, Sword]
lst = []
for x in weapons:
    for i in range(x.rarity.probabilty):
        lst.append(x)
weapons = lst


#Enemies
Orc_noob = Enemy('Orc', 'Agron', 50, 'Piercing', 'Fire', Fist, 5)
Orc_pro = Enemy('Orc', 'Pouria', 150, None, 'Piercing', Sword, 5)


player = Player('Erik', 100, [healthPotion_Large, healthPotion_Small, healthPotion_Large], Fist, None, None, 10)

