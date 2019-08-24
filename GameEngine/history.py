class History:
    def __init__(self):
        self.acts = [Act()]

    @property
    def acts_count(self):
        return len(self.acts)

    @property
    def ended_acts_count(self):
        return len(self.acts) - 1

    @property
    def current_act(self):
        return self.acts[-1]

    def end_act(self):
        self.current_act.end()
        self.acts.append(Act())


class Move:
    pass


class Act:
    pass

    def end(self):
        pass


class Result:
    pass

