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
        copy_attributes(bella_brawler, player)
    elif choice == monty_mischief:
        copy_attributes(monty_mischief, player)
    elif choice == sayo_swift:
        copy_attributes(sayo_swift, player)
    else:
        copy_attributes(dave_danger, player)

# Function to copy selected character attributes to opponent
def copy_attributes(charattr, oppattr):
    names = ['name', 'hp', 'max_hp', 'basic_attack', 'special_attack', 'special_atk_guage', 'inventory']
    for name in names:
        if hasattr(charattr, name):
            value = getattr(charattr, name)
            setattr(oppattr, name, value)

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
        copy_attributes(bella_brawler, opponent)
    elif opponent_choice == 'Monty Mischief':
        copy_attributes(monty_mischief, opponent)
    elif opponent_choice == 'Sayo Swift':
        copy_attributes(sayo_swift, opponent)
    elif opponent_choice == 'Dave Danger':
        copy_attributes(dave_danger, opponent)
