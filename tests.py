"""Unit tests for CLI adventures"""

import unittest
from character import *


class TestCharacterCreation(unittest.TestCase):
    """Test cases for character creation."""

    def test_melee_character_creation(self):
        """Test creating a melee character.

        This test checks if a Character object is created successfully
        when creating a character of the 'melee' class.

        """
        # Creating melee character
        name = "Hulk"
        _class_ = "melee"
        character = Character(name, _class_)

        # Asserting the the character is created with correct attributes
        self.assertEqual(character.name, name)
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
        # Creating melee character
        name = "Robin Hood"
        _class_ = "ranger"
        character = Character(name, _class_)

        # Asserting the the character is created with correct attributes
        self.assertEqual(character.name, name)
        self.assertEqual(character._class_, _class_)
        self.assertEqual(character.armor, "Common Leather Armor")
        self.assertEqual(character.weapon, "Common Bow")
        self.assertEqual(
            character.inventory,
            {"Gold": 50, "Potions": ["Healing Potion"], "Items": []},
        )


if __name__ == "__main__":
    unittest.main()
