# from ChessGame import ChessGame
from ChessGame2 import ChessGame2

# game modes
# 0: human vs human
# 1: human vs ai
# 2: ai vs ai

# mode 0 => ko truyền vào gì
# mode 1 => truyền vào ai_side (True or False) là phía của AI, ai_1_level là level của AI
# mode 2 => truyền vào ai_1_level và ai_2_level là level của 2 AI

if __name__ == "__main__":
# mode = 0
    # game = ChessGame2()
# mode = 1
    # ai is WHITE
    # game = ChessGame2(ai_side=True, ai_1_level=3)
    # ai is BLACK
    # game = ChessGame2(ai_side=False, ai_1_level=3)
# mode = 2
    game = ChessGame2(ai_1_level=3, ai_2_level=3)
    game.start()
