from GameEngine.table import Table
from GameEngine.history import History

# TODO: Use Result
# TODO: end_act


class Game:
    def __init__(self, radiant, dire):
        self.radiant = radiant # first move
        self.radiant.init_game(self)
        self.radiant.set_side('radiant')

        self.dire = dire
        self.radiant.init_game(self)
        self.dire.set_side('dire')

        self.players = [self.radiant, self.dire]
        self.history = History()
        self.winner = None

        self.table = Table()

    @property
    def current_player(self):
        return self.players[self.history.ended_acts_count % 2]

    @property
    def next_player(self):
        return self.players[self.history.ended_acts_count % 2 - 1]

    def update(self):
        self.table.update()
        if self.radiant.hp == 0:
            self.winner = self.dire
        elif self.dire.hp == 0:
            self.winner = self.radiant

        if self.winner:
            self.end_game()

    def end_act(self):
        self.history.end_act()
        pass

    def end_game(self):
        pass


