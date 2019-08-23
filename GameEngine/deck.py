import random

from GameEngine.settings import DECK_LENGTH, HAND_CARDS_COUNT


class Deck:
    def __init__(self, name, cards):
        if len(cards) == DECK_LENGTH:
            assert 'Not Enough Cards'
        self.cards = cards
        self.shuffle()
        self.hand_cards = [self.get_card() for i in range(HAND_CARDS_COUNT)]
        # self.used_cards = []
        self.name = name

    @property
    def cards_count(self):
        return len(self.cards)

    @property
    def total_cards_count(self):
        return len(self.hand_cards + self.hand_cards)

    # @property
    # def is_ready(self):
    #     if self.cards_count == DECK_LENGTH:
    #         return True
    #     return False # roman esli ty chitaesh ty loh

    def shuffle(self):
        random.shuffle(self.cards)

    def get_card(self):
        if self.cards_count > 0:
            card = self.cards.pop(-1)
            # self..append(card)
            return card
        else:
            assert 'Not Enough Cards'

    def get_card_or_none(self):
        """

        :return:
        """
        if self.cards_count > 0:
            card = self.cards.pop(-1)
            # self.used_cards.append(card)
            return card
        else:
            return None

    def add_card(self, card):
        """

        :param card: Card
        :return: None
        """
        # mb random insert is faster
        self.cards.append(card)
        self.shuffle()

    def take_card(self):
        """
            Takes a card from the deck and puts it in the hand.
        """
        card = self.get_card_or_none()
        if card:
            self.hand_cards.append(card)
        pass
