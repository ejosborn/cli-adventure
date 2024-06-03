from character import Character


class Enemy(Character):
    """Class representing an enemy in game.

    Attributes:
        name (str): The name of the enemy.
        level (int): The level of the enemy.
        _class_ (str): The class of the enemy.
        health (int): The health of the enemy.
        armor (int): The armor of the enemy.
        attack (int): The attack of the enemy.
    """

    def __init__(self, name, _class_):
        """
        Constructor for Enemy Object.


        """
        super().__init__(name, _class_)
        self.name = name
        self.level = 1
        self._class_ = _class_
        self.health = 1
        self.armor = ""
        self.resist = 0
        self.weapon = ""
        self.attack = 0

        # giving initial class specific attributes
        if self._class_ == "melee":
            self.health = 18
            self.armor = "Common Metal Armor"
            self.resist = 5
            self.weapon = "Common Club"
            self.attack = 3

        elif self._class_ == "ranger":
            self.health = 12
            self.armor = "Common Leather Armor"
            self.resist = 3
            self.weapon = "Common Short Bow"
            self.attack = 5

        else:  # sorcerer
            self.health = 7
            self.armor = "Common Robe"
            self.resist = 1
            self.weapon = "Common Staff"
            self.attack = 8
