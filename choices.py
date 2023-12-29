class Choice:
    def __init__(self, cooperate: bool):
        self.cooperated: bool = cooperate

    @classmethod
    def cooperate(cls):
        return cls(True)

    @classmethod
    def defer(cls):
        return cls(False)

    def __repr__(self):
        return "Cooperated" if self.cooperated else "Deferred"