class players():
    def __init__(self, name, score):
        self.name: str = name
        self.score: list[int] = score

    def total_score(self):
        total = 0
        for i in self.score:
            total += i
        return total
