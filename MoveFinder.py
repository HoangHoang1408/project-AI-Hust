import random

import chess


class MoveFinder:
    def __init__(self, board: chess.Board, level: int):
        self.level = level
        self.board = board

    def random_move(self):
        return random.sample(list(self.board.legal_moves), 1)[0]

    def sample_algorithm(self):
        # lấy tất cả các nước đi hợp lệ từ board.legal_moves
        # => dùng các nước đi đó để xây dựng thuật toán
        pass

    def get_move(self):
        switcher = {
            1: self.random_move,
            2: self.sample_algorithm,  # thêm thuật toán vào đây tương ứng với level của AI
        }
        return switcher.get(self.level, self.random_move)()
