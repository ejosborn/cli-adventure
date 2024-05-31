""""""


class Character:
    def __init__(self):
        """Constructor for Character Object"""
        self.name = ""
        self.exp = 0
        self._class_ = ""
        self.inventory = {"Gold": 0, "Potions": [], "Items": []}
