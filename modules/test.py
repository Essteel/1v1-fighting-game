""" Test cases for python fighter game

Tests elements of two main features of the game: character
selection and attacks.

Classes
-------
TestSelectCharacter
TestAttacks

Functions
---------
test_player_name()
test_player_hp()
test_player_special()
test_copy_attr()
test_attack_power()
test_special_power()
test_attack_damage()
teset_special_damage()
"""

import character

class TestSelectCharacter:
    """ Tests that the user can select a character """
    def test_player_name(self):
        """ Tests that the value of the player name attribute is correctly assigned """
        character.select_character(character.bella_brawler)
        assert character.player.name == "Bella Brawler"

        character.select_character(character.monty_mischief)
        assert character.player.name == "Monty Mischief"

    def test_player_hp(self):
        """ Tests that the value of the player hp attribute is correctly assigned """
        character.select_character(character.sayo_swift)
        assert character.player.health == 200

        character.select_character(character.dave_danger)
        assert character.player.health == 175

    def test_player_special(self):
        """ Tests that the value of the player special attack attribute is correctly assigned """
        character.select_character(character.dave_danger)
        assert character.player.special_attack == 80

        character.select_character(character.bella_brawler)
        assert character.player.special_attack == 50

    def test_copy_attr(self):
        """ Tests that the function correctly assigns the values for the character selected """
        character.copy_attributes(character.bella_brawler, character.player)
        assert character.player.__dict__ == character.bella_brawler.__dict__

        character.copy_attributes(character.dave_danger, character.player)
        assert character.player.__dict__ == character.dave_danger.__dict__

class TestAttacks:
    """ Tests that attack values are calculated correctly"""
    def test_attack_power(self):
        """ Tests that the attack attribute value for the player has been correctly assigned """
        character.player = character.dave_danger
        assert character.player.basic_attack == 50

        character.player = character.monty_mischief
        assert character.player.basic_attack == 40

    def test_special_power(self):
        """ Tests that the players special attack attribute value has been correctly assigned """
        character.select_character(character.bella_brawler)
        assert character.player.special_attack == 50

        character.select_character(character.sayo_swift)
        assert character.player.special_attack == 60

    def test_attack_damage(self):
        """ Tests the value calculated for opponent hp after player performs a basic attack """
        character.select_character(character.bella_brawler)
        character.opponent = character.Character("Monty Mischief", 200, 200, 40, 70)
        character.opponent.health = character.opponent.health - character.player.basic_attack
        assert character.opponent.health == 170

        character.select_character(character.sayo_swift)
        character.opponent = character.Character("Dave Danger", 175, 175, 50, 80)
        character.opponent.health = character.opponent.health - character.player.basic_attack
        assert character.opponent.health == 125

    def test_special_damage(self):
        """ Tests the value calculated for opponent hp after player performs a special attack """
        character.select_character(character.sayo_swift)
        character.opponent = character.Character("Bella Brawler", 350, 350, 30, 50)
        character.opponent.hp = character.opponent.health - character.player.special_attack
        assert character.opponent.health == 290
        character.select_character(character.dave_danger)
        character.opponent = character.Character("Monty Mischief", 200, 200, 40, 70)
        character.opponent.health = character.opponent.health - character.player.special_attack
        assert character.opponent.health == 120
