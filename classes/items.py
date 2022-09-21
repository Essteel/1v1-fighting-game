class HealthItem:
    def __init__(self, name, hp_restored):
        self.name = name
        self.hp_restored = hp_restored

class PowerUp:
    def __init__(self, name, dmg_added):
        self.name = name
        self.dmg_added = dmg_added