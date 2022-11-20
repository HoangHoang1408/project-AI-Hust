import random

import chess
import numpy as np

# points of chess pieces
PIECE_SCORES = {
    "K": 0,
    "Q": 900,
    "R": 500,
    "B": 330,
    "N": 320,
    "P": 100,
    "k": -0,
    "q": -900,
    "r": -500,
    "b": -330,
    "n": -320,
    "p": -100,
}
POSITIOIN_SCORES = {
    'p':[
 0,  0,  0,  0,  0,  0,  0,  0,
50, 50, 50, 50, 50, 50, 50, 50,
10, 10, 20, 30, 30, 20, 10, 10,
 5,  5, 10, 25, 25, 10,  5,  5,
 0,  0,  0, 20, 20,  0,  0,  0,
 5, -5,-10,  0,  0,-10, -5,  5,
 5, 10, 10,-20,-20, 10, 10,  5,
 0,  0,  0,  0,  0,  0,  0,  0
    ],
    'n':[
-50,-40,-30,-30,-30,-30,-40,-50,
-40,-20,  0,  0,  0,  0,-20,-40,
-30,  0, 10, 15, 15, 10,  0,-30,
-30,  5, 15, 20, 20, 15,  5,-30,
-30,  0, 15, 20, 20, 15,  0,-30,
-30,  5, 10, 15, 15, 10,  5,-30,
-40,-20,  0,  5,  5,  0,-20,-40,
-50,-40,-30,-30,-30,-30,-40,-50,
    ],
    'b':[
-20,-10,-10,-10,-10,-10,-10,-20,
-10,  0,  0,  0,  0,  0,  0,-10,
-10,  0,  5, 10, 10,  5,  0,-10,
-10,  5,  5, 10, 10,  5,  5,-10,
-10,  0, 10, 10, 10, 10,  0,-10,
-10, 10, 10, 10, 10, 10, 10,-10,
-10,  5,  0,  0,  0,  0,  5,-10,
-20,-10,-10,-10,-10,-10,-10,-20,
    ],
    'r':[
  0,  0,  0,  0,  0,  0,  0,  0,
  5, 10, 10, 10, 10, 10, 10,  5,
 -5,  0,  0,  0,  0,  0,  0, -5,
 -5,  0,  0,  0,  0,  0,  0, -5,
 -5,  0,  0,  0,  0,  0,  0, -5,
 -5,  0,  0,  0,  0,  0,  0, -5,
 -5,  0,  0,  0,  0,  0,  0, -5,
  0,  0,  0,  5,  5,  0,  0,  0
    ],
    'q':[
-20,-10,-10, -5, -5,-10,-10,-20,
-10,  0,  0,  0,  0,  0,  0,-10,
-10,  0,  5,  5,  5,  5,  0,-10,
 -5,  0,  5,  5,  5,  5,  0, -5,
  0,  0,  5,  5,  5,  5,  0, -5,
-10,  5,  5,  5,  5,  5,  0,-10,
-10,  0,  5,  0,  0,  0,  0,-10,
-20,-10,-10, -5, -5,-10,-10,-20
    ],
    'k':[
-30,-40,-40,-50,-50,-40,-40,-30,
-30,-40,-40,-50,-50,-40,-40,-30,
-30,-40,-40,-50,-50,-40,-40,-30,
-30,-40,-40,-50,-50,-40,-40,-30,
-20,-30,-30,-40,-40,-30,-30,-20,
-10,-20,-20,-20,-20,-20,-20,-10,
 20, 20,  0,  0,  0,  0, 20, 20,
 20, 30, 10,  0,  0, 10, 30, 20
    ],
    
    'P':[
  0,  0,  0,  0,  0,  0,  0,  0,
  5, 10, 10,-20,-20, 10, 10,  5,
  5, -5,-10,  0,  0,-10, -5,  5,
  0,  0,  0, 20, 20,  0,  0,  0,
  5,  5, 10, 25, 25, 10,  5,  5,
 10, 10, 20, 30, 30, 20, 10, 10,
 50, 50, 50, 50, 50, 50, 50, 50,
  0,  0,  0,  0,  0,  0,  0,  0,
    ],
    'N':[
-50,-40,-30,-30,-30,-30,-40,-50,
-40,-20,  0,  5,  5,  0,-20,-40,
-30,  5, 10, 15, 15, 10,  5,-30,
-30,  0, 15, 20, 20, 15,  0,-30,
-30,  5, 15, 20, 20, 15,  5,-30,
-30,  0, 10, 15, 15, 10,  0,-30,
-40,-20,  0,  0,  0,  0,-20,-40,
-50,-40,-30,-30,-30,-30,-40,-50,
    ],
    'B':[
-20,-10,-10,-10,-10,-10,-10,-20,
-10,  5,  0,  0,  0,  0,  5,-10,
-10, 10, 10, 10, 10, 10, 10,-10,
-10,  0, 10, 10, 10, 10,  0,-10,
-10,  5,  5, 10, 10,  5,  5,-10,
-10,  0,  5, 10, 10,  5,  0,-10,
-10,  0,  0,  0,  0,  0,  0,-10,
-20,-10,-10,-10,-10,-10,-10,-20,
    ],
    'R':[
  0,  0,  0,  5,  5,  0,  0,  0,
 -5,  0,  0,  0,  0,  0,  0, -5,
 -5,  0,  0,  0,  0,  0,  0, -5,
 -5,  0,  0,  0,  0,  0,  0, -5,
 -5,  0,  0,  0,  0,  0,  0, -5,
 -5,  0,  0,  0,  0,  0,  0, -5,
  5, 10, 10, 10, 10, 10, 10,  5,
  0,  0,  0,  0,  0,  0,  0,  0,
    ],
    'Q':[
-20,-10,-10, -5, -5,-10,-10,-20,
-10,  0,  5,  0,  0,  0,  0,-10,
-10,  5,  5,  5,  5,  5,  0,-10,
  0,  0,  5,  5,  5,  5,  0, -5,
 -5,  0,  5,  5,  5,  5,  0, -5,
-10,  0,  5,  5,  5,  5,  0,-10,
-10,  0,  0,  0,  0,  0,  0,-10,
-20,-10,-10, -5, -5,-10,-10,-20,
    ],
    'K':[
 20, 30, 10,  0,  0, 10, 30, 20,
 20, 20,  0,  0,  0,  0, 20, 20,
-10,-20,-20,-20,-20,-20,-20,-10,
-20,-30,-30,-40,-40,-30,-30,-20,
-30,-40,-40,-50,-50,-40,-40,-30,
-30,-40,-40,-50,-50,-40,-40,-30,
-30,-40,-40,-50,-50,-40,-40,-30,
-30,-40,-40,-50,-50,-40,-40,-30,
    ],
}

CHECK_MATE = 20000
DRAW = 0
CHESS_INDICES = np.array(tuple(chess.SQUARES))


candidate_move = None

i = 0
class MoveFinder:
    def __init__(self, board: chess.Board, level: int):
        self.level = level
        self.board = board

    def random_move(self):
        return random.choice(tuple(self.board.legal_moves))

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
                    return -CHECK_MATE
                else:
                    return CHECK_MATE
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
        global candidate_move
        candidate_move = None
        self.minimax_score2(0, max_depth, -9999, 9999)
        if candidate_move is None:
            return self.random_move()
        return candidate_move

    def cal_piece_score(self,tp:tuple[int,chess.Piece]):
        index, piece = tp
        return POSITIOIN_SCORES[piece.symbol()][index] + PIECE_SCORES[piece.symbol()]

    def calculate_board_score(self):
        return np.sum(np.array(tuple(self.cal_piece_score(x) for x in self.board.piece_map().items())))
        

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
