from functools import wraps


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


def game_initialized_only(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        instance = args[0]
        if instance.game:
            return func(*args, **kwargs)
        else:
            assert 'Game Is Not Initialized'
    return wrapper

