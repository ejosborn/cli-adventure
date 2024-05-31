""""""


class Character:
    """Class representing a character in a game.

    Attributes:
        name (str): The name of the character.
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
            _class_ (str): The class of the character

        Raises:
            ValueError: If an invalid character class is provided.
        """
        self.name = name
        self.exp = 0
        self._class_ = _class_
        self.armor = ""
        self.weapon = ""
        self.inventory = {"Gold": 50, "Potions": ["Healing Potion"], "Items": []}

        if self._class_ == "melee":
            self.armor = "Common Metal Armor"
            self.weapon = "Common Great Sword"
        elif self._class_ == "ranger":
            self.armor = "Common Leather Armor"
            self.weapon = "Common Bow"
        elif self._class_ == "sorcerer":
            self.armor = "Common Robe"
            self.weapon = "Common Staff"
        else:
            raise ValueError(f"Invalid Character class: {_class_}")
