class Player:
    def __init__(self, deck):
        self.deck = deck
        self.client_id = 1
        self.side = ''

    def set_side(self, side):
        self.side = side
        for c in self.deck.cards:
            c.side = side


