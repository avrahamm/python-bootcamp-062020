import collections


class Score:
    def __init__(self):
        self.score = collections.defaultdict(int)

    def sign_victory(self, name):
        self.score[name] += 10
