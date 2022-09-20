import time
from simple_term_menu import TerminalMenu

def main_menu():
    start_options = ['View character stats', 'Select character', 'Quit']
    start_menu = TerminalMenu(start_options)
    
    char_options = ['Bella Brawler', 'Monty Mischief', 'Sayo Swift', 'Dave Danger', 'Back']
    char_menu = TerminalMenu(char_options)

    quit_menu = False

    while quit_menu == False:
        start_options_index = start_menu.show()
        start_options_choice = start_options[start_options_index]
        # char_options_index = char_menu.show()
        # char_options_choice = char_options[char_options_index]

        if(start_options_choice == 'Quit'):
            quit_menu = True
        if(start_options_choice == 'Select character'):
            char_menu.show()
            # if(char_options_choice == 'Back'):
            #     start_menu.show()
        else:
            pass

