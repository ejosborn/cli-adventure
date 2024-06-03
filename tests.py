"""
Unit tests for CLI adventures.

This module contains unit tests for the functionality of the Character and Enemy classes in
the CLI adventures game.
"""

import unittest
from character import Character
from enemy import Enemy


class TestCharacterCreation(unittest.TestCase):
    """
    Test cases for character creation.
    """

    def test_melee_character_creation(self):
        """
        Test creating a melee character.

        This test checks if a Character object is created successfully
        when creating a character of the 'melee' class.
        """
        name = "Hulk the Strong"
        _class_ = "melee"
        character = Character(name, _class_)

        # Asserting that the character is created with correct attributes
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
        """
        Test creating a ranger character.

        This test checks if a Character object is created successfully
        when creating a character of the 'ranger' class.
        """
        name = "Robin Hood the Accurate"
        _class_ = "ranger"
        character = Character(name, _class_)

        # Asserting that the character is created with correct attributes
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
        """
        Test creating a sorcerer character.

        This test checks if a Character object is created successfully
        when creating a character of the 'sorcerer' class.
        """
        name = "Gandalf the Wise"
        _class_ = "sorcerer"
        character = Character(name, _class_)

        # Asserting that the character is created with correct attributes
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
        """
        Test creating an invalid character.

        This test checks if a Character object is not created successfully
        when creating a character of an invalid class.
        """
        name = "Lord Voldemort"
        _class_ = "Demon"

        with self.assertRaises(ValueError):
            character = Character(name, _class_)


class TestCharacterExpAndLevel(unittest.TestCase):
    """
    Test cases for adding experience and leveling up a character.
    """

    def test_exp_up(self):
        """
        Test adding experience to a character.

        This test checks if a Character object successfully gains experience points.
        """
        name = "Captain America"
        _class_ = "melee"
        character = Character(name, _class_)

        # adding experience to the character
        character.add_exp_up(100)
        self.assertEqual(character.exp, 100)

    def test_lvl_up(self):
        """
        Test leveling up a character.

        This test checks if a Character object successfully levels up after gaining
        experience points.
        """
        name = "Captain America"
        _class_ = "melee"
        character = Character(name, _class_)

        character.add_exp_up(200)
        total_lvl_up = character.exp // 100
        character.add_lvl(total_lvl_up)

        self.assertEqual(character.level, 3)


class TestEnemyCreation(unittest.TestCase):
    """
    Test cases for creating enemies.
    """

    def test_melee_enemy_creation(self):
        """
        Test creating a melee enemy.

        This test checks if an Enemy object is created successfully
        when creating an enemy of the 'melee' class.
        """
        name = "Hercules the Berserk"
        _class_ = "melee"

        enemy = Enemy(name, _class_)

        self.assertEqual(enemy.name, name)
        self.assertEqual(enemy.level, 1)
        self.assertEqual(enemy._class_, _class_)

    def test_ranger_enemy_creation(self):
        """
        Test creating a ranger enemy.

        This test checks if an Enemy object is created successfully
        when creating an enemy of the 'ranger' class.
        """
        name = "Zephyr the Accurate"
        _class_ = "ranger"

        enemy = Enemy(name, _class_)

        self.assertEqual(enemy.name, name)
        self.assertEqual(enemy.level, 1)
        self.assertEqual(enemy._class_, _class_)

    def test_sorcerer_enemy_creation(self):
        """
        Test creating a sorcerer enemy.

        This test checks if an Enemy object is created successfully
        when creating an enemy of the 'sorcerer' class.
        """
        name = "Molthrenar the Evil"
        _class_ = "sorcerer"

        enemy = Enemy(name, _class_)

        self.assertEqual(enemy.name, name)
        self.assertEqual(enemy.level, 1)
        self.assertEqual(enemy._class_, _class_)


if __name__ == "__main__":
    unittest.main()
