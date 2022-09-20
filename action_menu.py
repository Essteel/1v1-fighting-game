from simple_term_menu import TerminalMenu
import classes.attack as attack
from start_menu import player, opponent

# Set values for the attack objects for player and opponent
player_basic_atk = attack.Attack(player.basic_attack)
player_special_atk = attack.Attack(player.special_attack)
opponent_basic_atk = attack.Attack(opponent.basic_attack)
opponent_special_atk = attack.Attack(opponent.special_attack)

# Code to run the action menu to select whether to attack or use an item
def action_menu():
    action_options = ['Basic attack', 'Special attack', 'Use item', 'Quit game']
    quit_menu = False
    action_menu = TerminalMenu(action_options, clear_screen = True)

    item_options = ['Health item', 'Power up', 'Back']
    item_menu_back = False
    item_menu = TerminalMenu(item_options, clear_screen = False)

    while quit_menu == False:
        action_options_sel = action_menu.show()
        if action_options_sel == 0:
            pass # function to perform basic attack
        elif action_options_sel == 1:
            pass # function to perform special attack
        elif action_options_sel == 2:
            while item_menu_back == False:
                item_options_sel = item_menu.show()
                if item_options_sel == 0:
                    pass # function to use health item if held
                elif item_options_sel == 1:
                    pass # function to use power up if held
                elif item_options_sel == 2:
                    item_menu_back = True
                item_menu_back = False
        elif action_options_sel == 3:
            quit_menu = True

if __name__ == "__main__":
    action_menu()
