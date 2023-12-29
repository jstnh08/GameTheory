import random
from choices import Choice

class Strategy:
    def __init__(self):
        self.opp_move: Choice = None
        self.points: int = 0

    def make_move(self):
        return Choice.cooperate()

    @property
    def name(self):
        return self.__class__.__name__

class Friedman(Strategy):
    def __init__(self):
        super().__init__()
        self.retaliate = False

    def make_move(self):
        if self.opp_move and not self.opp_move.cooperated:
            self.retaliate = True

        return Choice.defer() if self.retaliate else Choice.cooperate()

class TitForTat(Strategy):
    def __init__(self):
        super().__init__()

    def make_move(self):
        return self.opp_move or Choice.cooperate()

class Joss(Strategy):
    def __init__(self):
        super().__init__()

    def make_move(self):
        if not self.opp_move:
            return Choice.cooperate()

        move = self.opp_move
        if move.cooperated and random.random() < 0.25:
            move = Choice.defer()

        return move