def deal_damage(defender, attacker, ignore_armor=False):
    if ignore_armor:
        defender.hp -= attacker.damage
    else:
        if defender.armor > attacker.damage:
            defender.armor -= attacker.damage
        elif defender.armor + defender.hp > attacker.damage:
            dmg = attacker.damage - defender.armor
            defender.armor = 0
            defender.hp -= dmg
        else:
            defender.armor = 0
            defender.hp = 0
