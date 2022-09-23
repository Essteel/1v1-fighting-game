from simple_term_menu import TerminalMenu
import modules.character as character
import modules.exception as exception

# Code to run the start menu for viewing character stats and character selection
def start_menu_main():
    start_options = ['View character stats', 'Select character', 'Quit']
    quit_menu = False
    start_menu = TerminalMenu(start_options, clear_screen = True)
    
    char_options = ['Bella Brawler', 'Monty Mischief', 'Sayo Swift', 'Dave Danger', 'Back']
    char_menu_back = False
    char_menu = TerminalMenu(char_options, clear_screen = True)

    stats_options = ['Back']
    stats_menu_back = False
    stats_menu = TerminalMenu(stats_options,clear_screen = False)

    while quit_menu == False:
        start_options_sel = start_menu.show()
        if start_options_sel == 0:
            stats_menu_back = False
            while stats_menu_back == False:
                character.get_character_stats() # function to print character stats
                stats_options_sel = stats_menu.show()
                if stats_options_sel == 0:
                    stats_menu.clear_screen = True
                    stats_menu_back = True
        if start_options_sel == 1:
            while char_menu_back == False:
                char_options_sel = char_menu.show()
                if char_options_sel == 0:
                    return character.select_character(character.bella_brawler)
                elif char_options_sel == 1:
                    return character.select_character(character.monty_mischief)
                elif char_options_sel == 2:
                    return character.select_character(character.sayo_swift)
                elif char_options_sel == 3:
                    return character.select_character(character.dave_danger)
                elif char_options_sel == 4:
                    char_menu_back = True
            char_menu_back = False
        try:
            if start_options_sel == 2:
                quit_menu = True
                raise exception.QuitGame
        except exception.QuitGame:
            print('Thanks for playing!')

if __name__ == "__main__":
    start_menu_main()
