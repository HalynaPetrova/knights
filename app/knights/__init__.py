from app.options.weapon import Weapon
from app.options.armour import Armour
from app.options.potion import Potion


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            weapon: Weapon,
            armour: list[Armour],
            potion: Potion | None
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0
        self.weapon = weapon
        self.armour = armour
        self.potion = potion


