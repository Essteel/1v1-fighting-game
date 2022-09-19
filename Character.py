class Character:
    def __init__(self, name, max_hp, hp, basic_attack, special_attack):
        self.name = name
        self.max_hp = max_hp
        self.hp = hp
        self.basic_attack = basic_attack
        self.special_attack = special_attack

# function that will allow user to view a list of characters and their stats
def get_character_stats():
    user_input = input('View character stats (y/n): ').lower()
    if user_input == 'y':
        return print(f'Please pick a character:\n{bella_brawler.__dict__}\n{monty_mischief.__dict__}\n{sayo_swift.__dict__}\n{dave_danger.__dict__}')

# sub class for player character
class Player(Character):
    super().__init__()

# function to assign a character to the player
def select_player(choice):
    print('Please choose a character:\n 1 = Bella\n 2 = Monty\n 3 = Sayo\n 4 = Dave\n')
    if choice == '1':
        pass # set character as Bella
    elif choice == '2':
        pass # set character as Monty
    elif choice == '3':
        pass # set character as Sayo
    else:
        pass # set character as Dave
