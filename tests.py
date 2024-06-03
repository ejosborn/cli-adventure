import unittest
from character import Character
from enemy import Enemy


class TestCharacterCreation(unittest.TestCase):
    """
    Test cases for creating Character instances.
    """

    def setUp(self):
        """
        Sets up common test data for character creation tests.
        """
        self.melee_name = "Hulk the Strong"
        self.ranger_name = "Robin Hood the Accurate"
        self.sorcerer_name = "Gandalf the Wise"
        self.character_inventory = {
            "Gold": 50,
            "Potions": ["Healing Potion"],
            "Items": [],
        }

    def test_melee_character_creation(self):
        """
        Test creating a melee character.

        This test checks if a Character object is created successfully
        when creating a character of the 'melee' class.
        """
        character = Character(self.melee_name, "melee")
        self.assertEqual(character.name, self.melee_name)
        self.assertEqual(character.level, 1)
        self.assertEqual(character._class_, "melee")
        self.assertEqual(character.armor, "Common Metal Armor")
        self.assertEqual(character.weapon, "Common Great Sword")
        self.assertEqual(character.inventory, self.character_inventory)

    def test_ranger_character_creation(self):
        """
        Test creating a ranger character.

        This test checks if a Character object is created successfully
        when creating a character of the 'ranger' class.
        """
        character = Character(self.ranger_name, "ranger")
        self.assertEqual(character.name, self.ranger_name)
        self.assertEqual(character.level, 1)
        self.assertEqual(character._class_, "ranger")
        self.assertEqual(character.armor, "Common Leather Armor")
        self.assertEqual(character.weapon, "Common Bow")
        self.assertEqual(character.inventory, self.character_inventory)

    def test_sorcerer_character_creation(self):
        """
        Test creating a sorcerer character.

        This test checks if a Character object is created successfully
        when creating a character of the 'sorcerer' class.
        """
        character = Character(self.sorcerer_name, "sorcerer")
        self.assertEqual(character.name, self.sorcerer_name)
        self.assertEqual(character.level, 1)
        self.assertEqual(character._class_, "sorcerer")
        self.assertEqual(character.armor, "Common Robe")
        self.assertEqual(character.weapon, "Common Staff")
        self.assertEqual(character.inventory, self.character_inventory)

    def test_invalid_character(self):
        """
        Test creating an invalid character.

        This test checks if a Character object is not created successfully
        when creating a character of an invalid class.
        """
        with self.assertRaises(ValueError):
            Character("Lord Voldemort", "Demon")


class TestCharacterExpAndLevel(unittest.TestCase):
    """
    Test cases for adding experience and leveling up a Character.
    """

    def setUp(self):
        """
        Sets up common test data for experience and leveling tests.
        """
        self.character = Character("Captain America", "melee")

    def test_exp_up(self):
        """
        Test adding experience to a character.

        This test checks if a Character object successfully gains experience points.
        """
        self.character.add_exp_up(100)
        self.assertEqual(self.character.exp, 100)

    def test_lvl_up(self):
        """
        Test leveling up a character.

        This test checks if a Character object successfully levels up after gaining experience points.
        """
        self.character.add_exp_up(200)
        total_lvl_up = self.character.exp // 100
        self.character.add_lvl(total_lvl_up)
        self.assertEqual(self.character.level, 3)


class TestEnemyCreation(unittest.TestCase):
    """
    Test cases for creating Enemy instances.
    """

    def setUp(self):
        """
        Sets up common test data for enemy creation tests.
        """
        self.melee_name = "Hercules the Berserk"
        self.ranger_name = "Zephyr the Accurate"
        self.sorcerer_name = "Molthrenar the Evil"

    def test_melee_enemy_creation(self):
        """
        Test creating a melee enemy.

        This test checks if an Enemy object is created successfully
        when creating an enemy of the 'melee' class.
        """
        enemy = Enemy(self.melee_name, "melee", "common")
        self.assertEqual(enemy.name, self.melee_name)
        self.assertEqual(enemy.level, 1)
        self.assertEqual(enemy._class_, "melee")

    def test_ranger_enemy_creation(self):
        """
        Test creating a ranger enemy.

        This test checks if an Enemy object is created successfully
        when creating an enemy of the 'ranger' class.
        """
        enemy = Enemy(self.ranger_name, "ranger", "uncommon")
        self.assertEqual(enemy.name, self.ranger_name)
        self.assertEqual(enemy.level, 1)
        self.assertEqual(enemy._class_, "ranger")

    def test_sorcerer_enemy_creation(self):
        """
        Test creating a sorcerer enemy.

        This test checks if an Enemy object is created successfully
        when creating an enemy of the 'sorcerer' class.
        """
        enemy = Enemy(self.sorcerer_name, "sorcerer", "boss")
        self.assertEqual(enemy.name, self.sorcerer_name)
        self.assertEqual(enemy.level, 1)
        self.assertEqual(enemy._class_, "sorcerer")


if __name__ == "__main__":
    unittest.main()
