class Table:
    def __init__(self):
        self.radiant = []
        self.dire = []

    @property
    def all_cards(self):
        return self.radiant + self.dire

    @property
    def all_cards_count(self):
        return len(self.all_cards)

    def update(self):
        self.radiant = filter(lambda card: card.is_alive,
                              self.radiant)

        self.dire = filter(lambda card: card.is_alive,
                           self.dire)
