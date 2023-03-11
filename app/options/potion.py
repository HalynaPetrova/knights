class Potion:
    def __init__(self, name: str, effect: dict) -> None:
        self.name = name
        self.effect = effect


berserk = Potion(name="Berserk", effect={"power": +15, "hp": -5, "protection": +10})
blessing = Potion(name="Blessing", effect={"hp": +10, "power": +5})
