from app.knights import Knight
from app.options.potion import blessing
from app.options.weapon import sword
from app.options.armour import breastplate_red_knight


red_knight = Knight(
        name="Red Knight",
        power=40,
        hp=70,
        weapon=sword,
        armour=[breastplate_red_knight],
        potion=blessing
)

