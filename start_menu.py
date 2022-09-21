from simple_term_menu import TerminalMenu
import classes.character as character
import random

# Create character objects
bella_brawler = character.Player('Bella Brawler', 350, 350, 30, 50, 2, {'Health Potion' : 2, 'Power Up' : 0})
monty_mischief = character.Player('Monty Mischief', 200, 200, 40, 70, 2, {'Health Potion' : 2, 'Power Up' : 0})
sayo_swift = character.Player('Sayo Swift', 200, 200, 50, 60, 2, {'Health Potion' : 2, 'Power Up' : 0})
dave_danger = character.Player('Dave Danger', 175, 175, 50, 80, 2, {'Health Potion' : 2, 'Power Up' : 0})

# Create empty player and opponent objects
player = character.Player('', 0, 0, 0, 0, 0, [''])
opponent = character.Character('', 0, 0, 0, 0)

# Function that will allow user to view a list of characters and their stats
def get_character_stats():
    print(bella_brawler.__dict__)
    print(monty_mischief.__dict__)
    print(sayo_swift.__dict__)
    print(dave_danger.__dict__)

# Function for player character selection
def select_character(choice):
    if choice == bella_brawler:
        player.name = bella_brawler.name
        player.hp = bella_brawler.hp
        player.max_hp = bella_brawler.max_hp
        player.basic_attack = bella_brawler.basic_attack
        player.special_attack = bella_brawler.special_attack
        player.special_atk_guage = bella_brawler.special_atk_guage
        player.inventory = bella_brawler.inventory
    elif choice == monty_mischief:
        player.name = monty_mischief.name
        player.hp = monty_mischief.hp
        player.max_hp = monty_mischief.max_hp
        player.basic_attack = monty_mischief.basic_attack
        player.special_attack = monty_mischief.special_attack
        player.special_atk_guage = monty_mischief.special_atk_guage
        player.inventory = monty_mischief.inventory
    elif choice == sayo_swift:
        player.name = sayo_swift.name
        player.hp = sayo_swift.hp
        player.max_hp = sayo_swift.max_hp
        player.basic_attack = sayo_swift.basic_attack
        player.special_attack = sayo_swift.special_attack
        player.special_atk_guage = sayo_swift.special_atk_guage
        player.inventory = sayo_swift.inventory
    else:
        player.name = dave_danger.name
        player.hp = sayo_swift.hp
        player.max_hp = dave_danger.max_hp
        player.basic_attack = dave_danger.basic_attack
        player.special_attack = dave_danger.special_attack
        player.special_atk_guage = dave_danger.special_atk_guage
        player.inventory = dave_danger.inventory

# Function for opponent character selection
def select_opponent():
    opponent_options = [bella_brawler.name, monty_mischief.name, sayo_swift.name, dave_danger.name]
    opponent_list = []
    player_choice = player.name
    for i in opponent_options:
        if i != player_choice:
            opponent_list.append(i)
    opponent_choice = random.choice(opponent_list)
    if opponent_choice == 'Bella Brawler':
        opponent.name = bella_brawler.name
        opponent.hp = bella_brawler.hp
        opponent.max_hp = bella_brawler.max_hp
        opponent.basic_attack = bella_brawler.basic_attack
        opponent.special_attack = bella_brawler.special_attack
    elif opponent_choice == 'Monty Mischief':
        opponent.name = monty_mischief.name
        opponent.hp = monty_mischief.hp
        opponent.max_hp = monty_mischief.max_hp
        opponent.basic_attack = monty_mischief.basic_attack
        opponent.special_attack = monty_mischief.special_attack
    elif opponent_choice == 'Sayo Swift':
        opponent.name = sayo_swift.name
        opponent.hp = sayo_swift.hp
        opponent.max_hp = sayo_swift.max_hp
        opponent.basic_attack = sayo_swift.basic_attack
        opponent.special_attack = sayo_swift.special_attack
    elif opponent_choice == 'Dave Danger':
        opponent.name = dave_danger.name
        opponent.hp = dave_danger.hp
        opponent.max_hp = dave_danger.max_hp
        opponent.basic_attack = dave_danger.basic_attack
        opponent.special_attack = dave_danger.special_attack

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
                    return select_character(bella_brawler)
                elif char_options_sel == 1:
                    return select_character(monty_mischief)
                elif char_options_sel == 2:
                    return select_character(sayo_swift)
                elif char_options_sel == 3:
                    return select_character(dave_danger)
                elif char_options_sel == 4:
                    char_menu_back = True
            char_menu_back = False
        elif start_options_sel == 2:
            quit_menu = True

if __name__ == "__main__":
    start_menu_main()
