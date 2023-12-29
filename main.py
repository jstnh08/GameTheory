from strategies import *

class Game:
    score_table = {
        (True, True): (3, 3),
        (True, False): (0, 5),
        (False, True): (5, 0),
        (False, False): (1, 1)
    }

    def __init__(self, p1: Strategy, p2: Strategy):
        self.p1: Strategy = p1
        self.p2: Strategy = p2

    def play(self, rounds=10, show=True):
        for i in range(rounds):
            p1_move = self.p1.make_move()
            p2_move = self.p2.make_move()

            p1_score, p2_score = self.score_table[(p1_move.cooperated, p2_move.cooperated)]
            self.p1.points += p1_score
            self.p2.points += p2_score

            self.p1.opp_move = p2_move
            self.p2.opp_move = p1_move

            if show:
                print(f"Round {i+1}\n{self.p1.name} {p1_move}, {self.p2.name} {p2_move}\n")

        if self.p1.points == self.p2.points:
            print(f"{self.p1.name} tied with {self.p2.name} for {self.p1.points} a piece")

        else:
            winner, loser = (self.p1, self.p2) if self.p1.points > self.p2.points else (self.p2, self.p1)
            print(f"{winner.name} ({winner.points}) beat {loser.name} ({loser.points})")

Game(Joss(), Friedman()).play()