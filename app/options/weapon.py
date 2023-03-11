class Weapon:
    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power


metal_sword = Weapon(name="Metal Sword", power=50)
two_handed_sword = Weapon(name="Two-handed Sword", power=55)
poisoned_sword = Weapon(name="Poisoned Sword", power=60)
sword = Weapon(name="Sword", power=45)
