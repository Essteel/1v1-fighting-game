class Character:
    def __init__(self, name, hp, max_hp, basic_attack, special_attack):
        self.name = name
        self.max_hp = max_hp
        self.hp = hp
        self.basic_attack = basic_attack
        self.special_attack = special_attack

class Player(Character):
    def __init__(self, name, hp, max_hp, basic_attack, special_attack, special_atk_guage, inventory):
        super().__init__(name, hp, max_hp, basic_attack, special_attack)
        self.special_atk_guage = special_atk_guage
        self.inventory = inventory
