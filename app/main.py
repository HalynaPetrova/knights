from app.knights import Knight
from app.knights.arthur import arthur
from app.knights.lancelot import lancelot
from app.knights.mordred import mordred
from app.knights.red_khight import red_knight
from app.prepare_battle import prepare_battle


def battle(knights: list[Knight]):

    for knight in knights:
        prepare_battle(knight)

    lancelot.hp -= mordred.power - lancelot.protection
    mordred.hp -= lancelot.power - mordred.protection
    arthur.hp -= red_knight.power - arthur.protection
    red_knight.hp -= arthur.power - red_knight.protection

    for knight in knights:
        if knight.hp <= 0:
            knight.hp = 0

    print({knight.name: knight.hp for knight in knights})


knights_list = [arthur, lancelot, mordred, red_knight]
battle(knights_list)
