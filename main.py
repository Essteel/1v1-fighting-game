import curses
import time
import text_art
import start_menu, action_menu

# Welcome screen
text_art.title_text()
input('\n Press any key to continue')

start_menu.start_menu_main()

# Calls the function to randomly assign an opponent
start_menu.select_opponent()

# Executes the action menu for selecting options during battle
action_menu.action_menu_main()

# Runs the sequence for battle
while action_menu.player.hp > 0 and action_menu.opponent.hp > 0:
    action_menu.action_menu_main()
    if action_menu.opponent.hp <= 0:
        print('Hooray! You won.')
    elif action_menu.player.hp <= 0:
        print('Oh no! You lost.')

def end(stdscr):
    stdscr.clear()
    stdscr.refresh()
    print('Press \'q\' to exit or \'Enter\' to try again')
    user_input = stdscr.getkey()

    if user_input == curses.KEY_ENTER:
        pass # main() # function wrapper for whole of main actions
    else:
        print('Thanks for playing!')

curses.wrapper(end)
