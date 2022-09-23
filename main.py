import text_art
import start_menu, action_menu
import clearing


play = True
replay = False

while play == True and replay == False:
# Welcome screen
    if replay == True:
        action_menu.replay_items()
    clearing.clear()
    text_art.title_text()
    input('\n Press Enter to continue')

    start_menu.start_menu_main()

    # Calls the function to randomly assign an opponent
    start_menu.select_opponent()

    # Executes the action menu for selecting options during battle
    action_menu.action_sequence()

    text_art.fight_text()

    user_input = input('\nEnter \'q\' to exit or \'a\' to try again: ')
    if user_input == 'q':
        print('Thanks for playing!')
        play = False
    elif user_input == 'a':
        replay == True
