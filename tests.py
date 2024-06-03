"""Unit tests for CLI adventures.

This module contains unit tests for the functionality of the Character class in
the CLI adventures game.

"""

import unittest
from character import Character
from enemy import Enemy


class TestCharacterCreation(unittest.TestCase):
    """Test cases for character creation."""

    def test_melee_character_creation(self):
        """Test creating a melee character.

        This test checks if a Character object is created successfully
        when creating a character of the 'melee' class.

        """
        # Creating melee character
        name = "Hulk the Strong"
        _class_ = "melee"
        character = Character(name, _class_)

        # Asserting the the character is created with correct attributes
        self.assertEqual(character.name, name)
        self.assertEqual(character.level, 1)
        self.assertEqual(character._class_, _class_)
        self.assertEqual(character.armor, "Common Metal Armor")
        self.assertEqual(character.weapon, "Common Great Sword")
        self.assertEqual(
            character.inventory,
            {"Gold": 50, "Potions": ["Healing Potion"], "Items": []},
        )

    def test_ranger_character_creation(self):
        """Test creating a ranger character.

        This test checks if a Character object is created successfully
        when creating a character of the 'ranger' class.

        """
        # Creating ranger character
        name = "Robin Hood the Accurate"
        _class_ = "ranger"
        character = Character(name, _class_)

        # Asserting the the character is created with correct attributes
        self.assertEqual(character.name, name)
        self.assertEqual(character.level, 1)
        self.assertEqual(character._class_, _class_)
        self.assertEqual(character.armor, "Common Leather Armor")
        self.assertEqual(character.weapon, "Common Bow")
        self.assertEqual(
            character.inventory,
            {"Gold": 50, "Potions": ["Healing Potion"], "Items": []},
        )

    def test_sorcerer_character_creation(self):
        """Test creating a sorcerer character.

        This test checks if a Character object is created successfully
        when creating a character of the 'sorcerer' class.

        """
        # Creating sorcerer character
        name = "Gandalf the Wise"
        _class_ = "sorcerer"
        character = Character(name, _class_)

        # Asserting the the character is created with correct attributes
        self.assertEqual(character.name, name)
        self.assertEqual(character.level, 1)
        self.assertEqual(character._class_, _class_)
        self.assertEqual(character.armor, "Common Robe")
        self.assertEqual(character.weapon, "Common Staff")
        self.assertEqual(
            character.inventory,
            {"Gold": 50, "Potions": ["Healing Potion"], "Items": []},
        )

    def test_invalid_character(self):
        """Test creating an invalid character.

        This test checks if a Character object is not created successfully
        when creating a character of an invalid class.

        """
        # Creating invalid character
        name = "Lord Voldemort"
        _class_ = "Demon"

        with self.assertRaises(ValueError):
            character = Character(name, _class_)


class testCharacterExpAndLevel(unittest.TestCase):
    """
    Testing level up method.
    """

    def test_exp_up(self):
        # Creating character
        name = "Captain America"
        _class_ = "melee"
        character = Character(name, _class_)

        #
        character.add_exp_up(100)
        self.assertEqual(character.exp, 100)

    def test_lvl_up(self):
        # Creating character
        name = "Captain America"
        _class_ = "melee"
        character = Character(name, _class_)

        # adding exp and lvl
        character.add_exp_up(200)
        total_lvl_up = character.exp / 100
        character.add_lvl(total_lvl_up)

        # asserting Equals
        self.assertEqual(character.level, 3)


class testEnemyCreation(unittest.TestCase):
    """
    Test cases for creating enemies.
    """

    def test_melee_enemy_creation(self):
        name = "Hercules the Berserk"
        _class_ = "melee"

        enemy = Enemy(name, _class_)

        self.assertEqual(enemy.name, name)
        self.assertEqual(enemy.level, 1)
        self.assertEqual(enemy._class_, _class_)

    def test_ranger_enemy_creation(self):
        name = "Zephyr the Accurate"
        _class_ = "ranger"

        enemy = Enemy(name, _class_)

        self.assertEqual(enemy.name, name)
        self.assertEqual(enemy.level, 1)
        self.assertEqual(enemy._class_, _class_)

    def test_sorcerer_enemy_creation(self):
        name = "Molthrenar the Evil"
        _class_ = "sorcerer"

        enemy = Enemy(name, _class_)

        self.assertEqual(enemy.name, name)
        self.assertEqual(enemy.level, 1)
        self.assertEqual(enemy._class_, _class_)


if __name__ == "__main__":
    unittest.main()
