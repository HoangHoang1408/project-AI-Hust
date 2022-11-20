import random

import chess
import numpy as np

# points of chess pieces
PIECE_SCORES = {
    "K": 0,
    "Q": 9,
    "R": 5,
    "B": 3,
    "N": 3,
    "P": 1,
    "k": 0,
    "q": -9,
    "r": -5,
    "b": -3,
    "n": -3,
    "p": -1,
}
CHECK_MATE = 1000
DRAW = 0
CHESS_INDICES = np.array(tuple(chess.SQUARES))


def board_index_to_score(x, board: chess.Board):
    piece = board.piece_at(x)
    if piece is None:
        return 0
    return PIECE_SCORES[piece.symbol()]


cal_score = np.vectorize(board_index_to_score)

candidate_move = None


class MoveFinder:
    def __init__(self, board: chess.Board, level: int):
        self.level = level
        self.board = board

    def random_move(self):
        return random.choice(list(self.board.legal_moves))

    # minimax algorithm

    ##### old version

    # def minimax_score(
    #     self,
    #     depth: int,
    #     max_depth: int,
    #     candidate_move: list[chess.Move],
    #     alpha: int,
    #     beta: int,
    # ):
    #     if self.board.is_game_over():
    #         if self.board.is_checkmate():
    #             if self.board.turn:
    #                 return CHECK_MATE
    #             else:
    #                 return -CHECK_MATE
    #         else:
    #             return DRAW

    #     if depth == max_depth:
    #         return self.calculate_board_score()

    #     if self.board.turn:
    #         max_evaluation = -9999
    #         for move in self.board.legal_moves:
    #             self.board.push(move)
    #             evaluation = self.minimax_score(
    #                 depth + 1, max_depth, candidate_move, alpha, beta
    #             )
    #             if evaluation > max_evaluation:
    #                 max_evaluation = evaluation
    #                 if depth == 0:
    #                     candidate_move.clear()
    #                     candidate_move.append(move)
    #             elif evaluation == max_evaluation and depth == 0:
    #                 candidate_move.append(move)
    #             alpha = max(alpha, evaluation)
    #             self.board.pop()
    #             if alpha > beta:
    #                 break
    #         return max_evaluation

    #     else:
    #         min_evaluation = 9999
    #         for move in self.board.legal_moves:
    #             self.board.push(move)
    #             evaluation = self.minimax_score(
    #                 depth + 1, max_depth, candidate_move, alpha, beta
    #             )
    #             if evaluation < min_evaluation:
    #                 min_evaluation = evaluation
    #                 if depth == 0:
    #                     candidate_move.clear()
    #                     candidate_move.append(move)
    #             elif evaluation == min_evaluation and depth == 0:
    #                 candidate_move.append(move)
    #             beta = min(beta, evaluation)
    #             self.board.pop()
    #             if alpha > beta:
    #                 break
    #         return min_evaluation
    # def minimax(self, max_depth: int):
    #     candidate_move: list[chess.Move] = []
    #     self.minimax_score(0, max_depth, candidate_move, -9999, 9999)
    #     return random.choice(candidate_move)

    ###  version 2
    def minimax_score2(
        self,
        depth: int,
        max_depth: int,
        alpha: int,
        beta: int,
    ):
        global candidate_move
        if self.board.is_game_over():
            if self.board.is_checkmate():
                if self.board.turn:
                    return CHECK_MATE
                else:
                    return -CHECK_MATE
            else:
                return DRAW

        if depth == max_depth:
            return self.calculate_board_score()

        if self.board.turn:
            max_evaluation = -9999
            search_moves = np.array(tuple(self.board.legal_moves))
            np.random.shuffle(search_moves)
            for move in search_moves:
                self.board.push(move)
                evaluation = self.minimax_score2(depth + 1, max_depth, alpha, beta)
                if evaluation > max_evaluation:
                    max_evaluation = evaluation
                    if depth == 0:
                        candidate_move = move
                alpha = max(alpha, max_evaluation)
                self.board.pop()
                if alpha >= beta:
                    break
            return max_evaluation

        else:
            min_evaluation = 9999
            search_moves = np.array(tuple(self.board.legal_moves))
            np.random.shuffle(search_moves)
            for move in search_moves:
                self.board.push(move)
                evaluation = self.minimax_score2(depth + 1, max_depth, alpha, beta)
                if evaluation < min_evaluation:
                    min_evaluation = evaluation
                    if depth == 0:
                        candidate_move = move
                beta = min(beta, min_evaluation)
                self.board.pop()
                if alpha >= beta:
                    break
            return min_evaluation

    def minimax2(self, max_depth: int):
        self.minimax_score2(0, max_depth, -9999, 9999)
        return candidate_move

    def calculate_board_score(self):
        return cal_score(CHESS_INDICES, self.board).sum()

    def get_move(self):
        switcher = {
            0: self.random_move,
            1: lambda: self.minimax2(1),
            2: lambda: self.minimax2(2),
            3: lambda: self.minimax2(3),
            4: lambda: self.minimax2(4),
            5: lambda: self.minimax2(5),  # còn chậm chưa ổn định
        }
        return switcher.get(self.level, self.random_move)()
