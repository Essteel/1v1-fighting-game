""" Python street fight game

This script allows the user to play the game until they no longer
wish to continue playing. At the end it asks the user if they
would like to quit or replay the game.

The game uses simple_term_menu for user input as well as typed
interaction for some elements of the game.

This script requires the installation of the following third party
packages in the Python environment you are running this script in:
'clearing', 'readchar', 'simple_term_menu'.

Raises:
    exception.InputError: raised if the user doesn't enter 'q' or 'a'
"""

import clearing
import readchar

from modules import character
from modules import text_art
from modules import items
from modules import exception
import start_menu
import action_menu

PLAY = True
REPLAY = False

# Runs the game until the user decides to replay or quit
while PLAY is True:
    if REPLAY is True:
        # Replenishes players inventory on replay
        items.replay_items()
    character.set_player_opponent()
    # Welcome screen with name of game
    clearing.clear()
    text_art.title_text()
    print(character.player.__dict__)
    print(character.opponent.__dict__)
    print("\n Press any key")

    # Waits for user to press a key before continuing
    key = readchar.readkey()

    # Executes the start menu for selecting a character
    start_menu.start_menu_main()

    # Executes the action menu for selecting options during battle
    action_menu.action_sequence()

    text_art.fight_text()

    # Checks whether the user would like to replay the game
    VALID_INPUT = False
    while VALID_INPUT is False:
        try:
            user_input = input("\nEnter \'q\' to exit or \'a\' to try again: ")
            if user_input not in ("q", "a"):
                raise exception.InputError
        except exception.InputError:
            print("Invalid input, enter \'q\' or \'a\'")
        else:
            if user_input == "q":
                print("See you next time!")
                PLAY = False
                VALID_INPUT = True
            elif user_input == "a":
                PLAY = True
                REPLAY = True
                VALID_INPUT = True
        