import random

# add the evals folder to the path
import sys

import chess

sys.path.append("evals")
from evals.Eval import Eval
from evals.Eval2 import Eval2

# constants
CHECK_MATE = 1000000
DRAW = 0
UPPER_BOUND = 99999

candidate_move = None


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

