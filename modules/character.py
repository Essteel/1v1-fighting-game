""" Character classes and functions for python fighter game

Classes
-------
Character: class used to represent a character
Player: subclass of character used to represent the player

Functions
---------
get_character_stats(): prints the main stats of each character
select_character(): selects the player character
select_opponent(): selects the opponent character
copy_attr_opp(charattr, oppatrr): copies the attributes of the
selected character to the opponent
copy_attr_player(characttr, playattr): copies the attributes of
the selected character to the player
set_player_opponent(): resets the player and opponent attributes

Objects
-------
bella_brawler: one of the playable character class objects
monty_mischief: one of the playable character class objects
sayo_swift: one of the playable character class objects
dave_danger: one of the playable character class objects
player: the player class object
opponent: the opponent class object
"""

import random

class Character:
    """ A class used to represent characters

    Attributes
    ----------
    name : str
        the name of the character
    health : int
        the current health of the character
    max_hp : int
        the maximum total health of the character
    basic_attack : int
        the value of the character's basic attack damage
    special_attack : int
        the value of the character's special attack damage
    """

    def __init__(self, name, health, max_hp, basic_attack):
        self.name = name
        self.max_hp = max_hp
        self.health = health
        self.basic_attack = basic_attack

class Player(Character):
    """ A subclass of Character used to represent the player

    This class inherits most of the functionality of the Player
    class but adds additional attributes special_atk_gauge and
    inventory.

    Attributes
    ----------
    name : str
        the name of the character
    health : int
        the current health of the character
    max_hp : int
        the maximum total health of the character
    basic_attack : int
        the value of the character's basic attack damage
    special_attack : int
        the value of the character's special attack damage
    special_atk_gauge : int
        the current number of special attacks available
    inventory : dict
        stores the number of available health potions and power ups
    """

    def __init__(self, name, health, max_hp, basic_attack,
     special_attack, special_atk_gauge, inventory
    ):
        super().__init__(name, health, max_hp, basic_attack)
        self.special_attack = special_attack
        self.special_atk_gauge = special_atk_gauge
        self.inventory = inventory

# Create character objects
bella_brawler = Player("Bella Brawler", 350, 350, 30, 50, 2,
{"Health Potion" : 2, "Power Up" : 0})
monty_mischief = Player("Monty Mischief", 200, 200, 40, 70, 2,
{"Health Potion" : 2, "Power Up" : 0})
sayo_swift = Player("Sayo Swift", 200, 200, 50, 60, 2,
{"Health Potion" : 2, "Power Up" : 0})
dave_danger = Player("Dave Danger", 175, 175, 50, 80, 2,
{"Health Potion" : 2, "Power Up" : 0})

# Create player and opponent objects
player = Player("", 0, 0, 0, 0, 0, {})
opponent = Character("", 0, 0, 0)

# Function that will allow user to view a list of characters and their stats
def get_character_stats():
    """ Function to print out important character stats

    Prints out the name, health, basic attack and special
    attack values for each of the four playable characters.
    """
    print(f"Name: {bella_brawler.name} | Health: {bella_brawler.max_hp} | Basic attack power:"
    f" {bella_brawler.basic_attack} | Special attack power: {bella_brawler.special_attack}\n")

    print(f"Name: {monty_mischief.name} | Health: {monty_mischief.max_hp} | Basic attack power:"
    f" {monty_mischief.basic_attack} | Special attack power: {monty_mischief.special_attack}\n")

    print(f"Name: {sayo_swift.name} | Health: {sayo_swift.max_hp} | Basic attack power:"
    f" {sayo_swift.basic_attack} | Special attack power: {sayo_swift.special_attack}\n")

    print(f"Name: {dave_danger.name} | Health: {dave_danger.max_hp} | Basic attack power:"
    f" {dave_danger.basic_attack} | Special attack power: {dave_danger.special_attack}\n")

# Function for player character selection
def select_character(choice):
    """ Function to assign selected character as player

    Depending on the selected character this function calls the
    copy_attributes() function to copy the attributes of the selected
    character to the player class object.
    Args:
        choice (class object): contains the attributes for each character
    """
    if choice == bella_brawler:
        copy_attr_player(bella_brawler, player)
    elif choice == monty_mischief:
        copy_attr_player(monty_mischief, player)
    elif choice == sayo_swift:
        copy_attr_player(sayo_swift, player)
    else:
        copy_attr_player(dave_danger, player)

# Function for opponent character selection
def select_opponent():
    """ Function to assign selected character as opponent

    Checks the 'opponent_option' list against the character selected
    by the user and appends the three characters not selected by the
    user to the 'opponent_list' list. A character is then
    chosen at random from this list. Depending on the selected
    character this function calls the copy_attributes() function to
    copy the attributes of the selected character to the opponent
    class object.
    """
    opponent_options = [bella_brawler.name, monty_mischief.name, sayo_swift.name, dave_danger.name]
    opponent_list = []
    player_choice = player.name
    for i in opponent_options:
        if i != player_choice:
            opponent_list.append(i)
    opponent_choice = random.choice(opponent_list)
    if opponent_choice == "Bella Brawler":
        copy_attr_opp(bella_brawler, opponent)
    elif opponent_choice == "Monty Mischief":
        copy_attr_opp(monty_mischief, opponent)
    elif opponent_choice == "Sayo Swift":
        copy_attr_opp(sayo_swift, opponent)
    elif opponent_choice == "Dave Danger":
        copy_attr_opp(dave_danger, opponent)

# Function to copy selected character attributes to opponent
def copy_attr_opp(charattr, oppattr):
    """ Function to copy selected character attributes to opponent

    This function iterates through the list 'names' and if the string matches
    the name of an attribute it copies that value to the opponent object.
    Args:
        charattr (class object): contains attributes for one of the characters
        oppattr (class object): contains attributes for the opponent
    """
    names = ["name", "health", "max_hp", "basic_attack"]
    for name in names:
        if hasattr(charattr, name):
            value = getattr(charattr, name)
            setattr(oppattr, name, value)

def copy_attr_player(charattr, playattr):
    """ Function to copy selected character attributes to player

    This function iterates through the list 'names' and if the string matches
    the name of an attribute it copies that value to the player object.
    Args:
        charattr (class object): contains attributes for one of the characters
        oppattr (class object): contains attributes for the opponent
    """
    names = ["name", "health", "max_hp", "basic_attack",
     "special_attack", "special_atk_gauge", "inventory"
     ]
    for name in names:
        if hasattr(charattr, name):
            value = getattr(charattr, name)
            setattr(playattr, name, value)

def set_player_opponent():
    """ Function to reset player and opponent on replay

    Checks if the player and opponent object attributes are
    empty or equal to zero. If they are not it resets them
    in preparation for the player character and opponent
    character to be selected by the user.
    """
    player_reset = Player("", 0, 0, 0, 0, 0, [""])
    opponent_reset = Character("", 0, 0, 0)

    if player != Player("", 0, 0, 0, 0, 0, [""]):
        names = ["name", "health", "max_hp", "basic_attack",
        "special_attack", "special_atk_gauge"]
        for name in names:
            if hasattr(player_reset, name):
                value = getattr(player_reset, name)
                setattr(player, name, value)
    if opponent != Character("", 0, 0, 0):
        names = ["name", "health", "max_hp", "basic_attack"]
        for name in names:
            if hasattr(opponent_reset, name):
                value = getattr(opponent_reset, name)
                setattr(opponent, name, value)
