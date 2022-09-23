import clearing
import modules.text_art as text_art
import modules.character as character
import modules.items as items
import modules.exception as exception
import start_menu
import action_menu


play = True
replay = False

while play is True:
# Welcome screen
    if replay is True:
        items.replay_items()
    clearing.clear()
    text_art.title_text()
    input('\n Press Enter to continue')

    start_menu.start_menu_main()

    # Calls the function to randomly assign an opponent
    character.select_opponent()

    # Executes the action menu for selecting options during battle
    action_menu.action_sequence()

    text_art.fight_text()

    # Checks whether the user would like to replay the game
    valid_input = False
    while valid_input is False:
        try:
            user_input = input('\nEnter \'q\' to exit or \'a\' to try again: ')
            if user_input != 'q' and user_input != 'a':
                raise exception.InputError
        except exception.InputError:
            print('Invalid input, enter \'q\' or \'a\'')
        else:
            if user_input == 'q':
                print('Thanks for playing!')
                play = False
                valid_input = True
            elif user_input == 'a':
                play = True
                replay = True
                valid_input = True
        