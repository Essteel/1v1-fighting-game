import clearing
import modules.text_art as text_art
import modules.character as character
import modules.items as items
import start_menu
import action_menu


play = True
replay = False

while play is True and replay is False:
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

    user_input = input('\nEnter \'q\' to exit or \'a\' to try again: ')
    
    try:
        if user_input == 'q':
            print('Thanks for playing!')
            play = False
        elif user_input == 'a':
            replay is True
        elif user_input != 'q' or 'a':
            while user_input != 'q' or 'a':
                raise TypeError
    except TypeError:
        input('Please enter \'q\' or \'a\ and press Enter: ')
