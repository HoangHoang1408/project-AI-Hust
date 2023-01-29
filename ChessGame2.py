from multiprocessing import Process, Queue

import chess
import pygame as pg

from MoveFinder import MoveFinder


class ChessGame2:
    def __init__(
        self,
        ai_side: bool = None,
        ai_1_level: int = None,
        ai_2_level: int = None,
        game_speed: int = 2,
        screen: pg.Surface = None,
    ) -> None:
        self.WIDTH = self.HEIGHT = 720
        self.DIMENSION = 8
        self.PIECE_SIZE = self.HEIGHT // self.DIMENSION
        self.MAX_FPS = 15
        self.IMAGES = {}
        self.game_speed = game_speed
        self.MAX_WAIT_TIME = 500  # ms

        self.screen = screen or pg.display.set_mode((self.WIDTH, self.HEIGHT))
        self.colors = [pg.Color("white"), pg.Color("gray")]
        self.board = chess.Board()
        self.clock = pg.time.Clock()

        self.ai_side = ai_side
        self.ai_1_level = ai_1_level
        self.ai_2_level = ai_2_level

        if ai_1_level is not None:
            self.move_finder1 = MoveFinder(
                self.board,
                ai_1_level,
            )
        if ai_2_level is not None:
            self.move_finder2 = MoveFinder(
                self.board,
                ai_2_level,
            )

        self.player1_is_human = (
            self.ai_side is None and self.ai_2_level is None
        ) or self.ai_side == False
        self.player2_is_human = (
            self.ai_side is None and self.ai_2_level is None
        ) or self.ai_side == True

        self.running = True
        self.pausing = False
        self.current_square = None  # (col, row) tuple
        self.two_squares = []

    def start(self):
        self.init_game()
        self.main_loop()

    def init_game(self):
        # pg.init()
        self.load_images()
        self.screen.fill(pg.Color("white"))

    def main_loop(self):
        while self.running:
            humen_turn = (self.board.turn and self.player1_is_human) or (
                not self.board.turn and self.player2_is_human
            )
            for e in pg.event.get():
                if e.type == pg.QUIT:
                    self.handle_quit()
                elif e.type == pg.MOUSEBUTTONDOWN and humen_turn and not self.pausing:
                    self.human_move()
                elif e.type == pg.KEYDOWN:
                    self.handle_key_down(e.key)
            if not humen_turn and not self.pausing:
                self.ai_move()
            self.draw()
            pg.time.wait(self.MAX_WAIT_TIME // self.game_speed)

    # handle methods
    def handle_quit(self):
        self.running = False
        pg.quit()

    def ai_move(self):
        if self.board.is_game_over():
            return
        two_ai = self.player1_is_human == self.player2_is_human
        if two_ai:
            if self.board.turn:
                move = self.move_finder2.get_move()
            else:
                move = self.move_finder1.get_move()
        else:
            move = self.move_finder1.get_move()
        self.board.push(move)

    def human_move(self):
        if self.board.is_game_over():
            return

        x, y = pg.mouse.get_pos()
        row, col = y // self.PIECE_SIZE, x // self.PIECE_SIZE

        if self.current_square == (col, row):
            self.two_squares = [self.current_square]
        else:
            self.current_square = (col, row)
            self.two_squares.append(self.current_square)

        if len(self.two_squares) == 2:
            move_uci = self.get_uci_move_from_row_col(
                *self.two_squares[0],
                *self.two_squares[1],
            )
            move = chess.Move.from_uci(move_uci)

            if self.board.is_legal(move):
                self.board.push(move)
                self.current_square = None
                self.two_squares = []
            elif self.board.is_legal(chess.Move.from_uci(move_uci + "q")):
                self.board.push(chess.Move.from_uci(move_uci + "q"))
                self.current_square = None
                self.two_squares = []
            else:
                self.two_squares = [self.current_square]

    def handle_key_down(self, key: int):
        def reset():
            self.board.reset()
            self.current_square = None
            self.two_squares = []

        def undo():
            if len(self.board.move_stack) > 0 and not self.board.is_game_over():
                self.board.pop()
                if (
                    self.player1_is_human
                    and not self.player2_is_human
                    or self.player2_is_human
                    and not self.player1_is_human
                ):
                    self.board.pop()

        def toggle_pause():
            self.pausing = not self.pausing

        if key == pg.K_b:
            undo()

        if key == pg.K_r:
            reset()

        if key == pg.K_p:
            toggle_pause()

    # draw methods
    def draw(self):
        self.draw_board()
        self.draw_pieces()
        self.draw_highlight_squares()
        self.draw_game_over_text()
        self.draw_pause_text()
        self.clock.tick(self.MAX_FPS)
        pg.display.flip()

    def draw_board(self):
        for r in range(self.DIMENSION):
            for c in range(self.DIMENSION):
                pg.draw.rect(
                    self.screen,
                    self.colors[(r + c) % 2],
                    pg.Rect(
                        c * self.PIECE_SIZE,
                        (r) * self.PIECE_SIZE,
                        self.PIECE_SIZE,
                        self.PIECE_SIZE,
                    ),
                )

    def draw_pieces(self):
        for r in range(self.DIMENSION):
            for c in range(self.DIMENSION):
                piece = self.board.piece_at(chess.square(c, r))
                if piece != None:
                    self.screen.blit(
                        self.IMAGES[str(piece)],
                        pg.Rect(
                            c * self.PIECE_SIZE,
                            r * self.PIECE_SIZE,
                            self.PIECE_SIZE,
                            self.PIECE_SIZE,
                        ),
                    )

    def draw_game_over_text(self):
        if not self.board.is_game_over():
            return

        if self.board.is_checkmate():
            text = (
                "Black wins by checkmate"
                if self.board.turn
                else "White wins by checkmate"
            )
        elif self.board.is_stalemate():
            text = "Stalemate"
        elif self.board.is_insufficient_material():
            text = "Draw by insufficient material"
        elif self.board.is_seventyfive_moves():
            text = "Draw by 75 moves rule"
        elif self.board.is_fivefold_repetition():
            text = "Draw by fivefold repetition"
        self.draw_text_in_the_middle(text)

    def draw_pause_text(self):
        if not self.pausing:
            return
        self.draw_text_in_the_middle("Pausing")

    def draw_text_in_the_middle(self, text):
        font = pg.font.SysFont("Rboto", 45, True, False)
        text_object = font.render(text, 0, pg.Color("Black"))
        text_location = pg.Rect(0, 0, self.WIDTH, self.HEIGHT).move(
            self.WIDTH / 2 - text_object.get_width() / 2,
            self.HEIGHT / 2 - text_object.get_height() / 2,
        )
        self.screen.blit(text_object, text_location)

    def draw_highlight_squares(self):
        if self.current_square is None:
            return

        col, row = self.current_square
        s = pg.Surface((self.PIECE_SIZE, self.PIECE_SIZE))
        s.set_alpha(100)
        s.fill(pg.Color("blue"))
        self.screen.blit(s, ((col) * self.PIECE_SIZE, row * self.PIECE_SIZE))
        s.fill(pg.Color("yellow"))
        for move in self.board.legal_moves:
            if move.from_square == chess.square(col, row):
                self.screen.blit(
                    s,
                    (
                        chess.square_file(move.to_square) * self.PIECE_SIZE,
                        chess.square_rank(move.to_square) * self.PIECE_SIZE,
                    ),
                )

    # init methods
    def load_images(self):
        white_piece_names = ["B", "K", "N", "P", "Q", "R"]
        black_piece_names = ["b", "k", "n", "p", "q", "r"]
        for piece in white_piece_names:
            self.IMAGES[piece] = pg.image.load(f"./images/w{piece}_new.png")
        for piece in black_piece_names:
            self.IMAGES[piece] = pg.image.load(
                f"./images/b{piece.capitalize()}_new.png"
            )

    # util methods
    def get_uci_move_from_row_col(
        self, from_row: int, from_col: int, to_row: int, to_col: int
    ) -> str:
        from_uci = chess.square_name(chess.square(from_row, from_col))
        to_uci = chess.square_name(chess.square(to_row, to_col))
        return from_uci + to_uci
