import random

from GameEngine.database import CardModel, session
from GameEngine.settings import DECK_LENGTH
from GameEngine.shortcuts import Card, Deck, Player, Game


def create_random_deck(name=f'deck {random.randint(0, 12345)}'):
    rand = [random.randrange(0, session.query(CardModel).count())
            for i in range(DECK_LENGTH)]
    rows = [session.query(CardModel)[r] for r in rand]
    cards = [row.get_card() for row in rows]
    deck = Deck(name, cards)
    return deck


deck1 = create_random_deck('deck1')
player1 = Player(deck1)

deck2 = create_random_deck('deck2')
player2 = Player(deck2)

game = Game(player1, player2)



