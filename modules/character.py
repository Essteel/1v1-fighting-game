import random

class Character:
    def __init__(self, name, hp, max_hp, basic_attack, special_attack):
        self.name = name
        self.max_hp = max_hp
        self.hp = hp
        self.basic_attack = basic_attack
        self.special_attack = special_attack

class Player(Character):
    def __init__(self, name, hp, max_hp, basic_attack, special_attack, special_atk_guage, inventory):
        super().__init__(name, hp, max_hp, basic_attack, special_attack)
        self.special_atk_guage = special_atk_guage
        self.inventory = inventory

# Create character objects
bella_brawler = Player('Bella Brawler', 350, 350, 30, 50, 2, {'Health Potion' : 2, 'Power Up' : 0})
monty_mischief = Player('Monty Mischief', 200, 200, 40, 70, 2, {'Health Potion' : 2, 'Power Up' : 0})
sayo_swift = Player('Sayo Swift', 200, 200, 50, 60, 2, {'Health Potion' : 2, 'Power Up' : 0})
dave_danger = Player('Dave Danger', 175, 175, 50, 80, 2, {'Health Potion' : 2, 'Power Up' : 0})

# Create empty player and opponent objects
player = Player('', 0, 0, 0, 0, 0, [''])
opponent = Character('', 0, 0, 0, 0)

# Function that will allow user to view a list of characters and their stats
def get_character_stats():
    print(f'Name: {bella_brawler.name} | Health: {bella_brawler.max_hp} | Basic attack power: {bella_brawler.basic_attack} | Special attack power: {bella_brawler.special_attack}\n')
    print(f'Name: {monty_mischief.name} | Health: {monty_mischief.max_hp} | Basic attack power: {monty_mischief.basic_attack} | Special attack power: {monty_mischief.special_attack}\n')
    print(f'Name: {sayo_swift.name} | Health: {sayo_swift.max_hp} | Basic attack power: {sayo_swift.basic_attack} | Special attack power: {sayo_swift.special_attack}\n')
    print(f'Name: {dave_danger.name} | Health: {dave_danger.max_hp} | Basic attack power: {dave_danger.basic_attack} | Special attack power: {dave_danger.special_attack}\n')

# Function for player character selection
def select_character(choice):
    if choice == bella_brawler:
        player.name = bella_brawler.name
        player.hp = bella_brawler.hp
        player.max_hp = bella_brawler.max_hp
        player.basic_attack = bella_brawler.basic_attack
        player.special_attack = bella_brawler.special_attack
        player.special_atk_guage = bella_brawler.special_atk_guage
        player.inventory = bella_brawler.inventory
    elif choice == monty_mischief:
        player.name = monty_mischief.name
        player.hp = monty_mischief.hp
        player.max_hp = monty_mischief.max_hp
        player.basic_attack = monty_mischief.basic_attack
        player.special_attack = monty_mischief.special_attack
        player.special_atk_guage = monty_mischief.special_atk_guage
        player.inventory = monty_mischief.inventory
    elif choice == sayo_swift:
        player.name = sayo_swift.name
        player.hp = sayo_swift.hp
        player.max_hp = sayo_swift.max_hp
        player.basic_attack = sayo_swift.basic_attack
        player.special_attack = sayo_swift.special_attack
        player.special_atk_guage = sayo_swift.special_atk_guage
        player.inventory = sayo_swift.inventory
    else:
        player.name = dave_danger.name
        player.hp = dave_danger.hp
        player.max_hp = dave_danger.max_hp
        player.basic_attack = dave_danger.basic_attack
        player.special_attack = dave_danger.special_attack
        player.special_atk_guage = dave_danger.special_atk_guage
        player.inventory = dave_danger.inventory

# Function for opponent character selection
def select_opponent():
    opponent_options = [bella_brawler.name, monty_mischief.name, sayo_swift.name, dave_danger.name]
    opponent_list = []
    player_choice = player.name
    for i in opponent_options:
        if i != player_choice:
            opponent_list.append(i)
    opponent_choice = random.choice(opponent_list)
    if opponent_choice == 'Bella Brawler':
        opponent.name = bella_brawler.name
        opponent.hp = bella_brawler.hp
        opponent.max_hp = bella_brawler.max_hp
        opponent.basic_attack = bella_brawler.basic_attack
        opponent.special_attack = bella_brawler.special_attack
    elif opponent_choice == 'Monty Mischief':
        opponent.name = monty_mischief.name
        opponent.hp = monty_mischief.hp
        opponent.max_hp = monty_mischief.max_hp
        opponent.basic_attack = monty_mischief.basic_attack
        opponent.special_attack = monty_mischief.special_attack
    elif opponent_choice == 'Sayo Swift':
        opponent.name = sayo_swift.name
        opponent.hp = sayo_swift.hp
        opponent.max_hp = sayo_swift.max_hp
        opponent.basic_attack = sayo_swift.basic_attack
        opponent.special_attack = sayo_swift.special_attack
    elif opponent_choice == 'Dave Danger':
        opponent.name = dave_danger.name
        opponent.hp = dave_danger.hp
        opponent.max_hp = dave_danger.max_hp
        opponent.basic_attack = dave_danger.basic_attack
        opponent.special_attack = dave_danger.special_attack
