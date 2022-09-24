from simple_term_menu import TerminalMenu
import clearing
import modules.character as character
import modules.exception as exception

# Code to run the start menu for viewing character stats and character selection
def start_menu_main():
    start_options = ['View character stats', 'Select character', 'Quit']
    quit_menu = False
    start_menu = TerminalMenu(start_options, clear_screen = True)
    
    char_options = ['Make selection', 'Back']
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
                character.get_character_stats()
                stats_options_sel = stats_menu.show()
                if stats_options_sel == 0:
                    stats_menu.clear_screen = True
                    stats_menu_back = True
        elif start_options_sel == 1:
            while char_menu_back == False:
                char_options_sel = char_menu.show()
                if char_options_sel == 0:
                    valid_input = False
                    while valid_input == False:
                        try:
                            print('1 = Bella Brawler, 2 = Monty Mischief, 3 = Sayo Swift, 4 = Dave Danger')
                            char_num = int(input('Please select the character you want to play as: '))
                            if char_num == 1:
                                clearing.clear()
                                print('You selected Bella')
                                valid_input = True
                                return character.select_character(character.bella_brawler)
                            elif char_num == 2:
                                clearing.clear()
                                print('You selected Monty')
                                valid_input = True
                                return character.select_character(character.monty_mischief)
                            elif char_num == 3:
                                clearing.clear()
                                print('You selected Sayo')
                                valid_input = True
                                return character.select_character(character.sayo_swift)
                            elif char_num == 4:
                                clearing.clear()
                                print('You selected Dave')
                                valid_input = True
                                return character.select_character(character.dave_danger)
                            elif char_num > 4 or char_num < 1:
                                raise exception.RangeError
                        except ValueError:
                            clearing.clear()
                            print('Please select a character by entering a number between 1-4\n')
                            valid_input = False
                        except exception.RangeError:
                            clearing.clear()
                            print('That wasn\'t a number between 1-4. Please try again\n')
                            valid_input = False
                if char_options_sel == 1:
                    char_menu_back = True
            char_menu_back = False
        elif start_options_sel == 2:
            character.player.hp = 0
            character.opponent.hp = 0
            break

if __name__ == "__main__":
    start_menu_main()
