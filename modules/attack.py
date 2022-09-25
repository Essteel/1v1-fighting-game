""" Attack functions for python fighter game

Functions
---------
basic_attack(): allows player to attempt a basic attack
opponent_attack(): opponent attack which reduces health of player
special_attack(): player attack which reduces health of opponent
"""

import random

from modules import character

# Basic attack function
def basic_attack():
    """ Allows the player to attempt a basic attack

    Generates a random integer between 0 and 20. If the integer
    is 19 or higher the attack is successful and the opponent health
    is reduced by the damage value of the player's basic attack, a
    power up is added to the player inventory. If the integer is 12 or
    higher the attack is successful and the opponent health is reduced
    by the damage value of the player's basic attack. If the integer
    is below 12 the attack is not successful and a message is printed.
    """
    success = random.randint(0, 20)
    if success >= 19:
        print("Critical hit! You got a power up")
        character.player.inventory["Power Up"] = character.player.inventory.get("Power Up") + 1
    elif success >= 12:
        print("Success! Your attack hit")
        character.opponent.health = character.opponent.health - character.player.basic_attack
    elif success < 12:
        print("Oh no! Your attack missed")

# Opponent attack function
def opponent_attack():
    """ Makes the Opponent perform an attack

    Reduces the player health by the damage value of the opponent's
    basic attack.
    """
    print("\nYour opponent attacked")
    character.player.health = character.player.health - character.opponent.basic_attack

# Special attack function
def special_attack():
    """ Allows the player to perform a special attack

    Checks to see if the player's special attack gauge is higher than
    0. If it is the opponent's health is reduced by the damage value
    of the player's special attack. A message is printed stating how
    many special attack's the player has left. If the special attack
    gauge is 0 a message is printed stating they have no special
    attacks left.
    """
    if character.player.special_atk_gauge > 0:
        character.player.special_atk_gauge -= 1
        print("You used a special attack. You have "
        f"{character.player.special_atk_gauge} special attacks left")
        character.opponent.health = character.opponent.health - character.player.special_attack
    else:
        print("Oh no! You\'re all out of Special Attacks")
