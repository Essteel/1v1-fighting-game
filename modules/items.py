""" Item classes and functions for python fighter game

Classes
-------
HealthItem: class used to represent health items
PowerUp: class used to represent power up items

Functions
---------
use_health_item(): adds health item value to player health
replay_items(): adds health items back to inventory on replay
use_pwr_up(): adds power up item value to basic attack

Objects
-------
health_item: stores the name and value of a health item
power_up: stores the name and value of a power up item
"""

from modules import character

class HealthItem:
    """ A class used to represent health items

    Attributes
    ----------
    name: string
        the name of the health item
    hp_restored : int
        the value added to player health when the item is used
    """
    def __init__(self, name, hp_restored):
        self.name = name
        self.hp_restored = hp_restored

class PowerUp:
    """ A class used to represent power items

    Attributes
    ----------
    name: string
        the name of the power up item
    hp_restored : int
        the value added to player basic attack when the 
        item is used
    """
    def __init__(self, name, dmg_added):
        self.name = name
        self.dmg_added = dmg_added

# Create health items and power ups
health_item = HealthItem("Health Potion", 50)
power_up = PowerUp("Power Up", 15)

def use_health_item():
    """ Allows the player to use a health item

    Checks if the player has a health item in their inventory.
    If they do, removes 1 health item from the inventory, lets
    them know  how many health items they have left and updates
    the player's health, adding on the value of the health item.
    If they don't have a health item, prints a message telling
    them so.
    """
    if character.player.inventory["Health Potion"] <= 0:
        print("You have no Health Potions")
    else:
        character.player.inventory["Health Potion"] -= 1
        print("You used a Health Potion. You have "
        f"{character.player.inventory['Health Potion']} health items left")
        character.player.health = character.player.health + health_item.hp_restored
        if character.player.health > character.player.max_hp:
            character.player.health = character.player.max_hp

def use_pwr_up():
    """ Allows the player to use a power up item

    Checks if the player has a power up item in their inventory.
    If they do, removes 1 power up item from the inventory, lets
    them know  how many power up items they have left and performs
    a basic attack with the added damage value of the power up item.
    If they don't have a power up item, prints a message telling
    them so.
    """
    if character.player.inventory["Power Up"] <= 0:
        print("You have no Power Ups")
    else:
        character.player.inventory["Power Up"] -= 1
        print("You used a Power Up. You have "
        f"{character.player.inventory['Power Up']} power ups left")
        character.opponent.health = character.opponent.health - (
            character.player.basic_attack + power_up.dmg_added
            )

def replay_items():
    """ Resets the player inventory when the user replays

    When the user chooses to play another game this function
    resets the players inventory to contain 2 health items and
    0 power ups.
    """
    character.player.inventory["Health Potion"] = 2
    character.player.inventory["Power Up"] = 0
