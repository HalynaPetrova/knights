class Armour:
    def __init__(self, name: str, protection: int) -> None:
        self.name = name
        self.protection = protection


helmet = Armour(name="helmet", protection=15)
boots = Armour(name="boots", protection=10)
breastplate_arthur = Armour(name="breastplate", protection=20)
breastplate_mordred = Armour(name="breastplate", protection=15)
breastplate_red_knight = Armour(name="breastplate", protection=25)
