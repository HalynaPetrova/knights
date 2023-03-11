from app.knights import Knight


def prepare_battle(knight: Knight):
    knight.power += knight.weapon.power
    knight.protection += sum([armour.protection for armour in knight.armour])

    if knight.potion:
        if knight.potion.name == "Berserk":
            knight.power += knight.potion.effect["power"]
            knight.hp += knight.potion.effect["hp"]
            knight.protection += knight.potion.effect["protection"]

        if knight.potion.name == "Blessing":
            knight.power += knight.potion.effect["power"]
            knight.hp += knight.potion.effect["hp"]

    return knight.name, knight.power, knight.protection, knight.hp

