import text_art
import start_menu, action_menu

# Welcome screen
text_art.title_text()
input('\n Press any key to continue')

start_menu.start_menu_main()

# Calls the function to randomly assign an opponent
start_menu.select_opponent()

# Executes the action menu for selecting options during battle
action_menu.action_sequence()

action_menu.end()
