""" Item classes and functions """

from modules import character

class HealthItem:
    """ Health item class """
    def __init__(self, name, hp_restored):
        self.name = name
        self.hp_restored = hp_restored

class PowerUp:
    """ Power up class """
    def __init__(self, name, dmg_added):
        self.name = name
        self.dmg_added = dmg_added

# Create health items and power ups
health_item = HealthItem('Health Potion', 15)
power_up = PowerUp('Power Up', 10)

def use_health_item():
    """ Use health item function """
    if character.player.inventory['Health Potion'] <= 0:
        print('You have no Health Potions')
    else:
        character.player.inventory['Health Potion'] -= 1
        print(f"""You used a Health Potion. You have {character.player.inventory['Health Potion']} health items left""")
        character.player.hp = character.player.hp + health_item.hp_restored
        if character.player.hp > character.player.max_hp:
            character.player.hp = character.player.max_hp

def replay_items():
    """ Add health items back to inventory when user replays """
    character.player.inventory['Health Potion'] = 2

def use_pwr_up():
    """ Use power up function """
    if character.player.inventory['Power Up'] <= 0:
        print('You have no Power Ups')
    else:
        character.player.inventory['Power Up'] -= 1
        print(f"""You used a Power Up. You have
         {character.player.inventory['Power Up']} power ups left""")
        character.opponent.hp = character.opponent.hp - (character.player.basic_attack + power_up.dmg_added)
