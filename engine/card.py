import random

from engine.shortcuts import deal_damage
from engine.config import DEFAULT_CARD_IMAGE, RAT_STEAL_CHANCE

'''
    Пролог
    
    Роман пробивает броню
    Крыса С шансом 33 процента ворует карту со стола противкника
    Керил нихуя не делает
    Виталя при атаке достаёт из колоды доп карту
    
'''

# TODO: game inited decorator


class Card:
    def __init__(self, name, hp, armor, damage, description, race):
        # meta
        self.name = name
        self.description = description
        self.image = DEFAULT_CARD_IMAGE
        # stats
        self.hp = hp
        self.armor = armor
        self.damage = damage
        self.race = race  # ROMAN, Keril, rat, Vetalya,

        self.game = None
        self.is_played = False # Esli eta hujna na stole

    @property
    def is_alive(self):
        return True if self.hp else False

    def init_game(self, game):
        self.game = game

    def attack(self, target):
        target.handle_attack(self)

    def handle_attack(self, attacker):
        if attacker.race == 'roman':
            deal_damage(self, attacker, ignore_armor=True)

        elif attacker.race == 'keril':
            deal_damage(self, attacker)

        elif attacker.race == 'rat':
            if random.random() < RAT_STEAL_CHANCE:
                card = self.game.next_player.deck.get_card_or_none()
                if card:
                    self.game.current_player.deck.add_card(card)
            deal_damage(self, attacker)

        elif attacker.race == 'vetalya':
            self.game.current_player.deck.take_card()
            deal_damage(self, attacker)

        else:
            assert 'Unknown attacker\'s race'




