import random

import chess


class MoveFinder:
    def __init__(self, board: chess.Board, level: int):
        self.level = level
        self.board = board

    def random_move(self):
        return random.sample(list(self.board.legal_moves), 1)[0]

    def get_move(self):
        switcher = {
            1: self.random_move,
        }
        return switcher.get(self.level, self.random_move)()
