class Character:
    """Class representing a character in a game.

    Attributes:
        name (str): The name of the character.
        level (int): The level of the character
        exp (int): The experience points of the character.
        _class_ (str): The class of the character.
        armor (str): The armor equipped by the character.
        weapon (str): The weapon equipped by  the character.
        inventory (dict): The inventory of a character, including gold, potions,
            and items.
    """

    def __init__(self, name, _class_):
        """
        Constructor for Character Object.

        Args:
            name (str): The name of the character.
            _class_ (str): The class of the character.

        Raises:
            ValueError: If an invalid character class is provided.
        """
        self.name = name
        self.level = 1
        self.exp = 0
        self._class_ = _class_
        self.health = 1
        self.armor = ""
        self.resist = 0
        self.weapon = ""
        self.attack = 0
        self.inventory = {"Gold": 50, "Potions": ["Healing Potion"], "Items": []}

        # giving initial class specific attributes
        if self._class_ == "melee":
            self.health = 18
            self.armor = "Common Metal Armor"
            self.resist = 5
            self.weapon = "Common Great Sword"
            self.attack = 7

        elif self._class_ == "ranger":
            self.health = 12
            self.armor = "Common Leather Armor"
            self.resist = 3
            self.weapon = "Common Bow"
            self.attack = 7

        elif self._class_ == "sorcerer":
            self.health = 7
            self.armor = "Common Robe"
            self.resist = 1
            self.weapon = "Common Staff"
            self.attack = 12
        else:
            raise ValueError(f"Invalid Character class: {_class_}")

    def add_exp_up(self, new_exp):
        """
        This method adds the exp of the fight to the Character exp attribute.

        Args:
            self (Character): The Character object.
            new_exp (int): The experience points to be added.

        Returns:
            int: The updated experience points of the Character.
        """
        self.exp += new_exp
        return self.exp

    def add_lvl(self, lvl_up):
        """
        Increase the level of the Character by the given amount.

        Args:
            self (Character): The Character object.
            lvl_up (int): The amount of levels the Character gains.

        Returns:
            int: The updated level of the Character.
        """
        self.level += lvl_up
        return self.level
