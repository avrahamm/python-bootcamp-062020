import collections


class Score:
    def __init__(self):
        self.score = collections.defaultdict(int)

    def sign_victory(self, name):
        self.score[name] += 10

    def print(self):
        print(self.score.items())

    def print_player(self, name):
        print(self.score[name])
