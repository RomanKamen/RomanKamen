from engine.table import Table


class Game:
    def __init__(self, radiant, dire):
        self.radiant = radiant
        self.radiant.set_side('radiant')

        self.dire = dire
        self.dire.set_side('dire')

        self.moves_count = 0

        self.table = Table()

    @property
    def current_player(self):
        if self.moves_count % 2:
            return self.radiant
        else:
            return self.dire

    @property
    def next_player(self):
        if not self.moves_count % 2:
            return self.radiant
        else:
            return self.dire

