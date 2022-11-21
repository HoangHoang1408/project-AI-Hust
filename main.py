from ChessGame import ChessGame

if __name__ == "__main__":
    game = ChessGame(
        player1_is_human=False, player2_is_human=False, ai_level=5, game_speed=10
    )
    game.start()
