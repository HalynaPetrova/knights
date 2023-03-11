from app.knights import Knight
from app.options.potion import berserk
from app.options.weapon import poisoned_sword
from app.options.armour import breastplate_mordred, boots


mordred = Knight(
        name="Mordred",
        power=30,
        hp=90,
        weapon=poisoned_sword,
        armour=[breastplate_mordred, boots],
        potion=berserk
)


