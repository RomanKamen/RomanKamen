from engine.shortcuts import deal_damage, game_initialized_only


class Player:
    def __init__(self, deck):
        self.game = None
        self.deck = deck
        self.client_id = 1
        self.side = ''
        self.hp = 30

    def init_game(self, game):
        self.game = game

    def set_side(self, side):
        self.side = side
        for c in self.deck.cards:
            c.side = side

    @game_initialized_only
    def handle_attack(self, attacker):
        deal_damage(self, attacker)
        self.game.update()
