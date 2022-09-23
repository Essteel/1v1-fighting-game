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
        pass

    def test_special_power(self):
        pass

    def test_attack_damage(self):
        pass

    def test_special_damage(self):
        pass
