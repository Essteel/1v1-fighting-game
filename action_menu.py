""" The action menu for the python street fight game

This module creates the action menu using simple_term_menu to
allow the user to choose which action to take. It also runs
the battle sequence once the user has chosen their action.

Functions
---------
action_sequence()
hud()
"""

import clearing
from simple_term_menu import TerminalMenu

from modules import items
from modules import attack
from modules import character

def player_action():
    """ A menu which allows the user to choose an action

    Allows the player to choose an action between making a basic
    attack, special attack, quitting the game or choosing an item
    from the sub menu. Choosing to attack or use an item counts as
    an action and the opponent will then take their turn and attack.
    """
    action_options = ["Basic attack", "Special attack", "Use item", "Quit"]
    action_taken = False
    action_menu = TerminalMenu(action_options,
    clear_screen = False,
    clear_menu_on_exit = True,
    )

    item_options = ["Health item", "Power up", "Back"]
    item_menu_back = False
    item_menu = TerminalMenu(item_options,
    clear_screen = False,
    clear_menu_on_exit = True
    )

    while action_taken is False:
        action_options_sel = action_menu.show()
        if action_options_sel == 0:
            clearing.clear()
            attack.basic_attack()
            action_taken = True
        elif action_options_sel == 1:
            clearing.clear()
            attack.special_attack()
            action_taken = True
        elif action_options_sel == 2:
            item_menu_back = False
            while item_menu_back is False:
                item_options_sel = item_menu.show()
                if item_options_sel == 0:
                    clearing.clear()
                    items.use_health_item()
                    action_taken = True
                    item_menu_back = True
                if item_options_sel == 1:
                    clearing.clear()
                    items.use_pwr_up()
                    action_taken = True
                    item_menu_back = True
                if item_options_sel == 2:
                    item_menu_back = True
        elif action_options_sel == 3:
            character.player.health = 0
            character.opponent.health = 0
            break

if __name__ == "__main__":
    player_action()

def action_sequence():
    """ Runs the battle sequence

    Runs the sequence between player action and opponent attack
    until either the player or opponent health drops to zero. At
    this point a message is printed to the screen.
    """
    while character.player.health > 0 and character.opponent.health > 0:
        hud()
        player_action()
        if character.opponent.health > 0:
            attack.opponent_attack()
    clearing.clear()
    if character.player.health == 0 and character.opponent.health == 0:
        print("Thanks for playing!")
    elif character.opponent.health <= 0:
        print("Congrats! You won")
    elif character.player.health <= 0:
        print("Too bad, you lost!")

def hud():
    """ Displays the player and opponent health and inventory

    Constantly displays  and updates the player and opponent 
    health as well as the contents of the player inventory during
    the action sequence.
    """
    print("\n-------------------------------------------")
    print(f"Player health: {character.player.health}     "
    f"Opponent health: {character.opponent.health}")
    print(f"Health item: {character.player.inventory['Health Potion']}\n"
    f"Power up: {character.player.inventory['Power Up']}\n")
