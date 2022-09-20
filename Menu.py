from simple_term_menu import TerminalMenu
import Character

# Create character objects
bella_brawler = Character.Character('Bella Brawler', 350, 30, 50)
monty_mischief = Character.Character('Monty Mischief', 200, 40, 70)
sayo_swift = Character.Character('Sayo Swift', 200, 50, 60)
dave_danger = Character.Character('Dave Danger', 175, 50, 80)

# Create empty player object
player = Character.Character('', 0, 0, 0)

# Function that will allow user to view a list of characters and their stats
def get_character_stats():
    print(bella_brawler.__dict__)
    print(monty_mischief.__dict__)
    print(sayo_swift.__dict__)
    print(dave_danger.__dict__)

# Function for character selection
def select_character(character):
    if character == bella_brawler:
        player.name = bella_brawler.name
        player.max_hp = bella_brawler.max_hp
        player.basic_attack = bella_brawler.basic_attack
        player.special_attack = bella_brawler.special_attack
    elif character == monty_mischief:
        player.name = monty_mischief.name
        player.max_hp = monty_mischief.max_hp
        player.basic_attack = monty_mischief.basic_attack
        player.special_attack = monty_mischief.special_attack
    elif character == sayo_swift:
        player.name = sayo_swift.name
        player.max_hp = sayo_swift.max_hp
        player.basic_attack = sayo_swift.basic_attack
        player.special_attack = sayo_swift.special_attack
    else:
        player.name = dave_danger.name
        player.max_hp = dave_danger.max_hp
        player.basic_attack = dave_danger.basic_attack
        player.special_attack = dave_danger.special_attack

# Code to run the main menu for viewing character stats and character selection
def main_menu():
    start_options = ['View character stats', 'Select character', 'Quit']
    quit_menu = False
    start_menu = TerminalMenu(
        start_options,
        clear_screen = True,
        )
    
    char_options = ['Bella Brawler', 'Monty Mischief', 'Sayo Swift', 'Dave Danger', 'Back']
    char_menu_back = False
    char_menu = TerminalMenu(
        char_options,
        clear_screen = True
        )

    stats_options = ['Back']
    stats_menu_back = False
    stats_menu = TerminalMenu(
        stats_options,
        clear_screen = False
    )

    while quit_menu == False:
        start_options_sel = start_menu.show()
        # start_options_choice = start_options[start_options_index]
        # char_options_index = char_menu.show()
        # char_options_choice = char_options[char_options_index]
        if start_options_sel == 0:
            while stats_menu_back == False:
                get_character_stats() # function to print character stats
                stats_options_sel = stats_menu.show()
                if stats_options_sel == 0:
                    stats_menu.clear_screen = True
                    stats_menu_back = True
        if start_options_sel == 1:
            while char_menu_back == False:
                char_options_sel = char_menu.show()
                if char_options_sel == 0:
                    select_character(bella_brawler)
                elif char_options_sel == 1:
                    select_character(monty_mischief)
                elif char_options_sel == 2:
                    select_character(sayo_swift)
                elif char_options_sel == 3:
                    select_character(dave_danger)
                elif char_options_sel == 4:
                    char_menu_back = True
            char_menu_back = False
        elif start_options_sel == 2:
            quit_menu = True

if __name__ == "__main__":
    main_menu()

print(player.__dict__)