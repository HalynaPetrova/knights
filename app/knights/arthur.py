from app.knights import Knight
from app.options.weapon import two_handed_sword
from app.options.armour import breastplate_arthur, helmet, boots


arthur = Knight(
        name="Arthur",
        power=45,
        hp=75,
        weapon=two_handed_sword,
        armour=[breastplate_arthur, helmet, boots],
        potion=None
)
