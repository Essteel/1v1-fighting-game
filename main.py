""" Runs the program """

import clearing
import readchar

from modules import text_art
from modules import character
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
    # Welcome screen with name of game
    clearing.clear()
    text_art.title_text()
    print('\n Press any key')

    # Waits for user to press a key before continuing
    key = readchar.readkey()

    # Executes the start menu for selecting a character
    start_menu.start_menu_main()

    # Calls the function to randomly assign an opponent
    character.select_opponent()

    # Executes the action menu for selecting options during battle
    action_menu.action_sequence()

    text_art.fight_text()

    # Checks whether the user would like to replay the game
    VALID_INPUT = False
    while VALID_INPUT is False:
        try:
            user_input = input('\nEnter \'q\' to exit or \'a\' to try again: ')
            if user_input != 'q' and user_input != 'a':
                raise exception.InputError
        except exception.InputError:
            print('Invalid input, enter \'q\' or \'a\'')
        else:
            if user_input == 'q':
                print('See you next time!')
                PLAY = False
                VALID_INPUT = True
            elif user_input == 'a':
                PLAY = True
                REPLAY = True
                VALID_INPUT = True
        