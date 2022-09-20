import time
from simple_term_menu import TerminalMenu
import Character

# # Create character objects
bella_brawler = Character.Character('Bella Brawler', 350, 350, 30, 50)
monty_mischief = Character.Character('Monty Mischief', 200, 200, 40, 70)
sayo_swift = Character.Character('Sayo Swift', 200, 200, 50, 60)
dave_danger = Character.Character('Dave Danger', 175, 175, 50, 80)

# function that will allow user to view a list of characters and their stats
def get_character_stats():
    print(bella_brawler.__dict__)
    print(monty_mischief.__dict__)
    print(sayo_swift.__dict__)
    print(dave_danger.__dict__)

def main_menu():
    start_options = ['View character stats', 'Select character', 'Quit']
    start_menu = TerminalMenu(start_options)
    quit_menu = False
    
    char_options = ['Bella Brawler', 'Monty Mischief', 'Sayo Swift', 'Dave Danger', 'Back']
    char_menu = TerminalMenu(char_options)
    char_menu_back = False
    

    while quit_menu == False:
        start_options_sel = start_menu.show()
        # start_options_choice = start_options[start_options_index]
        # char_options_index = char_menu.show()
        # char_options_choice = char_options[char_options_index]
        if start_options_sel == 1:
            get_character_stats() # function to print character stats
        if start_options_sel == 1:
            while char_menu_back == False:
                char_options_sel = char_menu.show()
                if char_options_sel == 0:
                    pass # function to set player character as Bella
                elif char_options_sel == 1:
                    pass # function to set player character as Monty
                elif char_options_sel == 2:
                    pass # function to set player character as Sayo
                elif char_options_sel == 3:
                    pass # function to set player character as Dave
                elif char_options_sel == 4:
                    char_menu_back = True
            char_menu_back = False
        elif start_options_sel == 2:
            quit_menu = True

if __name__ == "__main__":
    main_menu()