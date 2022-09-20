class Character:
    def __init__(self, name, max_hp, hp, basic_attack, special_attack):
        self.name = name
        self.max_hp = max_hp
        self.hp = hp
        self.basic_attack = basic_attack
        self.special_attack = special_attack

# sub class for player character
# class Player(Character):
#     super().__init__()

# function to assign a character to the player
def select_player():
    while True:
        choice = input('Please choose a character:\n 1 = Bella\n 2 = Monty\n 3 = Sayo\n 4 = Dave\n')
        if choice == '1':
            pass # set character as Bella
        elif choice == '2':
            pass # set character as Monty
        elif choice == '3':
            pass # set character as Sayo
        else:
            pass # set character as Dave
