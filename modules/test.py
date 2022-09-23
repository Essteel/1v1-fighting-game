import character

class TestSelectCharacter:
    def test_stats_display(self):
        check = 'Name: Bella Brawler'
        assert check == f'Name: {character.bella_brawler.name}'
        check = 'Health: 175'
        assert check == f'Health: {character.dave_danger.max_hp}'
    
    def test_player_name(self):
        character.select_character(character.bella_brawler)
        assert character.player.name == 'Bella Brawler'
        character.select_character(character.monty_mischief)
        assert character.player.name == 'Monty Mischief'

    def test_player_hp(self):
        character.select_character(character.sayo_swift)
        assert character.player.hp == 200
        character.select_character(character.dave_danger)
        assert character.player.hp == 175

    def test_player_special(self):
        character.select_character(character.dave_danger)
        assert character.player.special_attack == 80
        character.select_character(character.bella_brawler)
        assert character.player.special_attack == 50

class TestAttacks:
    def test_attack_power(self):
        character.player = character.Player('Dave Danger', 175, 175, 50, 80, 2, {'Health Potion' : 2, 'Power Up' : 0})
        assert character.player.basic_attack == 50
        character.player = character.Player('Monty Mischief', 200, 200, 40, 70, 2, {'Health Potion' : 2, 'Power Up' : 0})
        assert character.player.basic_attack == 40

    def test_special_power(self):
        character.player = character.Player('Bella Brawler', 350, 350, 30, 50, 2, {'Health Potion' : 2, 'Power Up' : 0})
        assert character.player.special_attack == 50
        character.player = character.Player('Sayo Swift', 200, 200, 50, 60, 2, {'Health Potion' : 2, 'Power Up' : 0})
        assert character.player.special_attack == 60

    def test_attack_damage(self):
        character.player = character.Player('Monty Mischief', 200, 200, 40, 70, 2, {'Health Potion' : 2, 'Power Up' : 0})
        character.opponent = character.Character('Bella Brawler', 350, 350, 30, 50)
        character.opponent.hp = character.opponent.hp - character.player.basic_attack
        assert character.opponent.hp == 310
        character.player = character.Player('Sayo Swift', 200, 200, 50, 60, 2, {'Health Potion' : 2, 'Power Up' : 0})
        character.opponent = character.Character('Dave Danger', 175, 175, 50, 80)
        character.opponent.hp = character.opponent.hp - character.player.basic_attack
        assert character.opponent.hp == 125

    def test_special_damage(self):
        character.player = character.Player('Sayo Swift', 200, 200, 50, 60, 2, {'Health Potion' : 2, 'Power Up' : 0})
        character.opponent = character.Character('Bella Brawler', 350, 350, 30, 50)
        character.opponent.hp = character.opponent.hp - character.player.special_attack
        assert character.opponent.hp == 290
        character.player = character.Player('Monty Mischief', 200, 200, 40, 70, 2, {'Health Potion' : 2, 'Power Up' : 0})
        character.opponent = character.Character('Dave Danger', 175, 175, 50, 80)
        character.opponent.hp = character.opponent.hp - character.player.special_attack
        assert character.opponent.hp == 105
