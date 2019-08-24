from GameEngine.func import deal_damage, game_initialized_only

# TODO: end_act
# TODO: timer decorator


class Player:
    def __init__(self, deck):
        self.game = None
        self.deck = deck
        self.client_id = 1
        self.side = ''
        self.hp = 30
        self.armor = 0
        self.mana = 0

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

    # @game_initialized_only
    # def make_move(self):
    #     pass

    @game_initialized_only
    def attack_with_card(self, card, target):
        # mb create a decorator
        if self.game.current_player is self:
            card.attack(target)
        else:
            # mb assert
            print('Not your turn')

    @game_initialized_only
    def end_act(self):
        self.game.end_act()
        pass
