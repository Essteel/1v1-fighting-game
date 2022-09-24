import clearing
from simple_term_menu import TerminalMenu

from modules import items
from modules import attack
from modules import character

def player_action():
    """ Runs the sequence to allow the user to choose an action """
    action_options = ['Basic attack', 'Special attack', 'Use item', 'Quit']
    action_taken = False
    action_menu = TerminalMenu(action_options,
    clear_screen = False,
    clear_menu_on_exit = True,
    )

    item_options = ['Health item', 'Power up', 'Back']
    item_menu_back = False
    item_menu = TerminalMenu(item_options,
    clear_screen = False,
    clear_menu_on_exit = True
    )

    while action_taken is False:
        action_options_sel = action_menu.show()
        if action_options_sel == 0:
            clearing.clear()
            attack.basic_attack()
            action_taken = True
        elif action_options_sel == 1:
            clearing.clear()
            attack.special_attack()
            action_taken = True
        elif action_options_sel == 2:
            item_menu_back = False
            while item_menu_back is False:
                item_options_sel = item_menu.show()
                if item_options_sel == 0:
                    clearing.clear()
                    items.use_health_item()
                    action_taken = True
                    item_menu_back = True
                if item_options_sel == 1:
                    clearing.clear()
                    items.use_pwr_up()
                    action_taken = True
                    item_menu_back = True
                if item_options_sel == 2:
                    item_menu_back = True
        elif action_options_sel == 3:
            character.player.hp = 0
            character.opponent.hp = 0
            break

if __name__ == "__main__":
    player_action()

def action_sequence():
    """ Runs the battle sequence """
    while character.player.hp > 0 and character.opponent.hp > 0:
        hud()
        player_action()
        if character.opponent.hp > 0:
            attack.opponent_attack()
    clearing.clear()
    if character.player.hp == 0 and character.opponent.hp == 0:
        print('Thanks for playing!')
    elif character.opponent.hp <= 0:
        print('Congrats! You won')
    elif character.player.hp <= 0:
        print('Too bad, you lost!')

def hud():
    """ Displays the player and opponent health and inventory """
    print('\n-------------------------------------------')
    print(f'Player health: {character.player.hp}     Opponent health: {character.opponent.hp}')
    print(f"Health item: {character.player.inventory['Health Potion']}\nPower up: {character.player.inventory['Power Up']}\n")
