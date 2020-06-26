class BasePlayer:
    def __init__(self, score_keeper, value, name):
        self.score = score_keeper
        self.value = value
        self.name = name

    def game_over(self, win):
        self.score.game_over(win, self.name)

    def sign_victory(self):
        self.score.sign_victory(self.name)
