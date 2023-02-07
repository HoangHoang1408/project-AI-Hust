import random

# add the evals folder to the path
import sys
from time import time

import chess

sys.path.append("evals")
from evals.Eval import Eval
from evals.Eval2 import Eval2

# constants
CHECK_MATE = 1000000
DRAW = 0
UPPER_BOUND = 99999

candidate_move = None

KING_WHITE = "K"
KING_BLACK = "k"
QUEEN_WHITE = "Q"
QUEEN_BLACK = "q"
ROOK_WHITE = "R"
ROOK_BLACK = "r"
BISHOP_WHITE = "B"
BISHOP_BLACK = "b"
KNIGHT_WHITE = "N"
KNIGHT_BLACK = "n"
PAWN_WHITE = "P"
PAWN_BLACK = "p"


class MoveFinder:
    def __init__(self, board: chess.Board, level: int, ev: int = 0):
        self.level = level
        self.board = board
        self.evals = [Eval(self.board), Eval2(self.board)]
        self.eval = self.evals[ev]

    def random_move(self):
        return random.choice(tuple(self.board.legal_moves))

    def minimax_score(
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
                    return -CHECK_MATE
                else:
                    return CHECK_MATE
            else:
                return DRAW

        if depth == max_depth:
            return self.eval.evaluate()

        if self.board.turn:
            max_evaluation = -UPPER_BOUND
            moves = list(self.board.legal_moves)
            random.shuffle(moves)
            for move in moves:
                # for move in self.board.legal_moves:
                self.board.push(move)
                evaluation = self.minimax_score(depth + 1, max_depth, alpha, beta)
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
            min_evaluation = UPPER_BOUND
            moves = list(self.board.legal_moves)
            random.shuffle(moves)
            for move in moves:
                # for move in self.board.legal_moves:
                self.board.push(move)
                evaluation = self.minimax_score(depth + 1, max_depth, alpha, beta)
                if evaluation < min_evaluation:
                    min_evaluation = evaluation
                    if depth == 0:
                        candidate_move = move
                beta = min(beta, min_evaluation)
                self.board.pop()
                if alpha >= beta:
                    break
            return min_evaluation

    def get_move(self):
        global candidate_move
        candidate_move = None
        self.minimax_score(0, self.level, -UPPER_BOUND, UPPER_BOUND)
        if candidate_move is None:
            return self.random_move()
        return candidate_move

    def get_move2(self):
        global candidate_move
        candidate_move = None

        total_moves = len(list(self.board.legal_moves))
        pc = {
            KING_WHITE: 0,
            QUEEN_WHITE: 0,
            ROOK_WHITE: 0,
            BISHOP_WHITE: 0,
            KNIGHT_WHITE: 0,
            PAWN_WHITE: 0,
            KING_BLACK: 0,
            QUEEN_BLACK: 0,
            ROOK_BLACK: 0,
            BISHOP_BLACK: 0,
            KNIGHT_BLACK: 0,
            PAWN_BLACK: 0,
        }
        for piece in self.board.piece_map().values():
            symbol = piece.symbol()
            pc[symbol] += 1
        phase = (
            pc[KNIGHT_WHITE]
            + pc[BISHOP_WHITE]
            + 2 * pc[ROOK_WHITE]
            + 4 * pc[QUEEN_WHITE]
            + pc[KNIGHT_BLACK]
            + pc[BISHOP_BLACK]
            + 2 * pc[ROOK_BLACK]
            + 4 * pc[QUEEN_BLACK]
        )

        time_start = time()
        if phase in set([1, 2, 3, 5, 6]) or total_moves in set([1, 2, 3, 6, 7, 8, 9]):
            self.minimax_score(0, 5, -UPPER_BOUND, UPPER_BOUND)
        elif (
            phase in set([16, 20, 22, 24])
            or total_moves in set([30, 34, 35, 37])
            or (total_moves > 40 and total_moves < 48)
        ):
            self.minimax_score(0, 3, -UPPER_BOUND, UPPER_BOUND)
        else:
            self.minimax_score(0, 4, -UPPER_BOUND, UPPER_BOUND)

        time_end = time()

        if candidate_move is None:
            return self.random_move()

        with open("./metrics/move_time2.csv", "a") as f:
            f.write(f"{total_moves},{phase},{time_end - time_start}\n")
        return candidate_move
