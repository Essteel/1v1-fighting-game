from random import randint
from simple_term_menu import TerminalMenu
import classes.items as items
import classes.attack as attack
from start_menu import player, opponent
import clearing
import text_art
import curses

# Create health items and power ups
health_item = items.HealthItem('Health Potion', 15)
power_up = items.PowerUp('Power Up', 10)

# Basic attack function
def basic_attack():
    success = randint(0, 20)
    if success >= 12:
        print('Success! Your attack hit')
        opponent.hp = opponent.hp - player.basic_attack
    elif success == 20:
        print('Critical hit! You got a power up')
        player.inventory['Power Up'] = player.inventory.get('Power Up') + 1
    elif success < 12:
        print('Oh no! Your attack missed')
print(opponent.__dict__)

# Opponent attack function
def opponent_attack():
    print('Your opponent attacked')
    player.hp = player.hp - opponent.basic_attack

# Special attack function
def special_attack():
    if player.special_atk_guage > 0:
        player.special_atk_guage -= 1
        print(f'You used a special attack. You have {player.special_atk_guage} special attacks left')
        opponent.hp = opponent.hp - player.special_attack
    else:
        print('Oh no! You\'re all out of Special Attacks')

# Use health item function
def use_health_item():
    if player.inventory['Health Potion'] <= 0:
        print('You have no Health Potions')
    else:
        player.inventory['Health Potion'] -= 1
        print(f"You used a Health Potion. You have {player.inventory['Health Potion']} health items left")
        return player.hp + health_item.hp_restored # add in not to go above max health

# Use power up function
def use_pwr_up():
    if player.inventory['Power Up'] <= 0:
        print('You have no Power Ups')
    else:
        player.inventory['Power Up'] -= 1
        print(f"You used a Power Up. You have {player.inventory['Power Up']} power ups left")
        return opponent.hp - (player.basic_attack + power_up.dmg_added)

def player_action():
    action_options = ['Basic attack', 'Special attack', 'Use item', 'Quit game']
    quit_menu = False
    action_taken = False
    action_menu = TerminalMenu(action_options,
    clear_screen = False,
    clear_menu_on_exit = True
    )
    
    item_options = ['Health item', 'Power up', 'Back']
    item_menu_back = False
    item_menu = TerminalMenu(item_options,
    clear_screen = False,
    clear_menu_on_exit = True
    )

    while quit_menu == False and action_taken == False:
        action_options_sel = action_menu.show()
        if action_options_sel == 0:
            clearing.clear()
            basic_attack()
            action_taken = True
        if action_options_sel == 1:
            clearing.clear()
            special_attack()
            action_taken = True
        if action_options_sel == 2:
            while item_menu_back == False:
                item_options_sel = item_menu.show()
                if item_options_sel == 0:
                    use_health_item()
                if item_options_sel == 1:
                    use_pwr_up()
                if item_options_sel == 2:
                    item_menu_back = True
                    item_menu_back = False
        elif action_options_sel == 3:
            end()

if __name__ == "__main__":
    player_action()


def end():
    user_input = input('Enter \'q\' to exit or \'a\' to try again: ')

    if user_input == 'a':
        pass # main() # function wrapper for whole of main actions
    elif user_input == 'q':
        print('Thanks for playing!')

def action_sequence():
    while player.hp > 0 and opponent.hp > 0:
        print('\n-------------------------------------------')
        print(f'Player health: {player.hp}     Opponent health: {opponent.hp}')
        print(f"Health item: {player.inventory['Health Potion']}\nPower up: {player.inventory['Power Up']}\n")
        player_action()
        if opponent.hp > 0:
            opponent_attack()
        # elif opponent.hp <= 0:
        #     print('Congrats! You won')
        #     end()
        # else:
        #     print('Too bad, you lost!')
        #     end()