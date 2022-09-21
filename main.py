import curses
import time

# welcome screen
# def main(stdscr):
#     stdscr.clear()
#     curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)
#     curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_YELLOW)
#     yellow_and_black = curses.color_pair(1)
#     black_and_yellow = curses.color_pair(2)

#     for i in range(30):
#         stdscr.clear()
#         color = black_and_yellow

#         if i % 2 == 0:
#             color = yellow_and_black
        
#         stdscr.addstr('Python Street Fight!\n\n', color)
#         stdscr.addstr('Press any key')
#         stdscr.refresh()
#         time.sleep(0.2)

#     while True:
#         key = stdscr.getkey()
#         if key == curses.KEY_ENTER:
#             break

#     stdscr.getch()
# # stdscr.addstr(0, 0, 'Please select a character:')
# curses.wrapper(main)

# Character.get_character_stats()

import start_menu, action_menu

# Executes the start menu for viewing character stats and character selection
start_menu.start_menu_main()

# Calls the function to randomly assign an opponent
start_menu.select_opponent()

# Executes the action menu for selecting options during battle
action_menu.action_menu_main()
