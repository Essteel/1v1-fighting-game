import random
import character

# Basic attack function
def basic_attack():
    success = random.randint(0, 20)
    if success == 20:
        print('Critical hit! You got a power up')
        character.player.inventory['Power Up'] = character.player.inventory.get('Power Up') + 1
    elif success >= 12:
        print('Success! Your attack hit')
        character.opponent.hp = character.opponent.hp - character.player.basic_attack
    elif success < 12:
        print('Oh no! Your attack missed')

# Opponent attack function
def opponent_attack():
    print('Your opponent attacked')
    character.player.hp = character.player.hp - character.opponent.basic_attack

# Special attack function
def special_attack():
    if character.player.special_atk_guage > 0:
        character.player.special_atk_guage -= 1
        print(f'You used a special attack. You have {character.player.special_atk_guage} special attacks left')
        character.opponent.hp = character.opponent.hp - character.player.special_attack
    else:
        print('Oh no! You\'re all out of Special Attacks')