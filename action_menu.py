from random import randint
from simple_term_menu import TerminalMenu
import classes.items as items
import classes.attack as attack
from start_menu import player, opponent

# Create health items and power ups
health_item = items.HealthItem('Health Potion', 15)
power_up = items.PowerUp('Power Up', 10)

# Basic attack function
def basic_attack():
    success = randint(0, 20)
    if success >= 12:
        print('Success! Your attack hit')
        opponent.hp = opponent.hp - player.basic_attack
    if success == 20:
        print('Critical hit! You got a power up')
        player.inventory['Power Up'] = player.inventory.get('Power Up') + 1
    else:
        print('Oh no! Your attack missed')
print(opponent.__dict__)

# Opponent attack function
def opponent_attack():
    print('Your opponent attacked')
    player.hp = player.hp - opponent.basic_attack

# Special attack function
def special_attack():
    if player.special_atk_guage > 0:
        print('You used a special attack')
        player.special_atk_guage -= 1
        opponent.hp = opponent.hp - player.special_attack
    else:
        print('Oh no! You\'re all out of Special Attacks')

# Use health item function
def use_health_item():
    if player.inventory['Health Potion'] <= 0:
        print('You have no Health Potions')
    else:
        player.inventory['Health Potion'] -= 1
        print('You used a Health Potion')
        return player.hp + health_item.hp_restored # add in not to go above max health

# Use power up function
def use_pwr_up():
    if player.inventory['Power Up'] <= 0:
        print('You have no Power Ups')
    else:
        player.inventory['Power Up'] -= 1
        print('You used a Power Up')
        return opponent.hp - (player.basic_attack + power_up.dmg_added)

# Code to run the action menu to select whether to attack or use an item
def action_menu_main():
    action_options = ['Basic attack', 'Special attack', 'Use item', 'Quit game']
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

    while action_taken == False:
        action_options_sel = action_menu.show()
        if action_options_sel == 0:
            basic_attack()
            action_taken = True
        elif action_options_sel == 1:
            special_attack()
            action_taken = True
        if action_options_sel == 2:
            while item_menu_back == False:
                item_options_sel = item_menu.show()
                if item_options_sel == 0:
                    use_health_item()
                elif item_options_sel == 1:
                    use_pwr_up()
                elif item_options_sel == 2:
                    item_menu_back = True
            item_menu_back = False
        elif action_options_sel == 3:
            break

if __name__ == "__main__":
    action_menu_main()
