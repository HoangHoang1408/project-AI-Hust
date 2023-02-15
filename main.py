import pygame

from ChessGame2 import ChessGame2

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Set font


# def func():

def start_game():
    pygame.init()

    # Set screen size
    size = (720, 720)
    screen = pygame.display.set_mode(size)

    # Set title
    pygame.display.set_caption("Chess Game")

    # set background image
    background_image = pygame.image.load("bgchess.jpg").convert()
    screen.blit(background_image, [0, 0])

    # Set colors

    mode = None
    while mode is None:
        mode = select_mode(screen)

    if mode == "Human vs Machine":
        side = select_side(screen)
        depth = select_depth(screen)
        human_machine_match(screen=screen, depth=depth, side=side)
    elif mode == "Machine vs Machine":
        depth_machine_1, depth_machine_2 = select_depth_two_machine(screen)
        machine_match(
            screen=screen,
            depth_machine_1=depth_machine_1,
            depth_machine_2=depth_machine_2,
        )
    else:
        human_match(screen)


def select_mode(screen):
    man_man_color = white
    man_machine_color = white
    machine_machine_color = white
    selected_mode = None
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if buttons were clicked
                if man_man.collidepoint(event.pos):
                    selected_mode = "Human vs Human"
                    man_man_color = red
                    man_machine_color = white
                    machine_machine_color = white
                elif man_machine.collidepoint(event.pos):
                    selected_mode = "Human vs Machine"
                    man_man_color = white
                    man_machine_color = red
                    machine_machine_color = white
                elif machine_machine.collidepoint(event.pos):
                    selected_mode = "Machine vs Machine"
                    man_man_color = white
                    man_machine_color = white
                    machine_machine_color = red
                elif next.collidepoint(event.pos):
                    if selected_mode is not None:
                        return selected_mode
        # Draw mode selection interface here
        font = pygame.font.Font(None, 25)
        mode_text = font.render("Select game mode:", True, white)
        mode_modul = pygame.Rect(360, 50, 200, 50)
        mode_modul_color = white

        # node to next
        font_big = pygame.font.Font(None, 40)
        next = pygame.Rect(360, 600, 200, 50)
        next_text = font_big.render("Next", True, white)
        pygame.draw.rect(screen, white, next, 3, 6)
        screen.blit(next_text, (next.x + 10, next.y + 10))

        # position of text
        man_man = pygame.Rect(400, 120, 200, 50)
        man_machine = pygame.Rect(400, 190, 200, 50)
        machine_machine = pygame.Rect(400, 260, 200, 50)

        # color of text

        # text
        man_man_text = font.render("Human vs Human", True, white)
        man_machine_text = font.render("Human vs Machine", True, white)
        machine_machine_text = font.render("Machine vs Machine", True, white)

        pygame.draw.rect(screen, mode_modul_color, mode_modul, 3, 6)
        pygame.draw.rect(screen, man_man_color, man_man, 3, 6)
        pygame.draw.rect(screen, man_machine_color, man_machine, 3, 6)
        pygame.draw.rect(screen, machine_machine_color, machine_machine, 3, 6)

        screen.blit(mode_text, (mode_modul.x + 10, mode_modul.y + 10))
        screen.blit(man_man_text, (man_man.x + 10, man_man.y + 10))
        screen.blit(man_machine_text, (man_machine.x + 10, man_machine.y + 10))
        screen.blit(
            machine_machine_text, (machine_machine.x +
                                   10, machine_machine.y + 10)
        )

        pygame.display.update()


def select_side(screen):
    # reset background
    background_image = pygame.image.load("bgchess.jpg").convert()
    screen.blit(background_image, [0, 0])

    # Set borders color
    white_border_color = white
    black_border_color = white

    side = None
    # select side
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if buttons were clicked
                if white_color.collidepoint(event.pos):
                    white_border_color = red
                    black_border_color = white
                    side = "white"
                elif black_color.collidepoint(event.pos):
                    white_border_color = white
                    black_border_color = red
                    side = "black"
                elif next.collidepoint(event.pos):
                    if side is not None:
                        return side
        # Draw mode selection interface here
        font = pygame.font.Font(None, 25)
        side_text = font.render("Select side for machine:", True, white)
        side_modul = pygame.Rect(360, 50, 250, 50)
        side_modul_color = white

        # node to next
        font_big = pygame.font.Font(None, 40)
        next = pygame.Rect(360, 600, 200, 50)
        next_text = font_big.render("Next", True, white)
        pygame.draw.rect(screen, white, next, 3, 6)
        screen.blit(next_text, (next.x + 10, next.y + 10))

        # position of text
        white_color = pygame.Rect(400, 120, 200, 50)
        black_color = pygame.Rect(400, 190, 200, 50)

        # color of text

        # text
        white_text = font.render("White", True, white)
        black_text = font.render("Black", True, white)

        pygame.draw.rect(screen, side_modul_color, side_modul, 3, 6)
        pygame.draw.rect(screen, white_border_color, white_color, 3, 6)
        pygame.draw.rect(screen, black_border_color, black_color, 3, 6)

        screen.blit(side_text, (side_modul.x + 10, side_modul.y + 10))
        screen.blit(white_text, (white_color.x + 10, white_color.y + 10))
        screen.blit(black_text, (black_color.x + 10, black_color.y + 10))

        pygame.display.update()


def select_depth(screen):
    # reset background
    background_image = pygame.image.load("bgchess.jpg").convert()
    screen.blit(background_image, [0, 0])

    # Set borders color
    depth_one_color = white
    depth_two_color = white
    depth_three_color = white
    depth_four_color = white
    depth_five_color = white

    depth = None
    # select side
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if buttons were clicked
                if depth_one.collidepoint(event.pos):
                    depth_one_color = red
                    depth_two_color = white
                    depth_three_color = white
                    depth_four_color = white
                    depth_five_color = white
                    depth = 1
                elif depth_two.collidepoint(event.pos):
                    depth_one_color = white
                    depth_two_color = red
                    depth_three_color = white
                    depth_four_color = white
                    depth_five_color = white
                    depth = 2
                elif depth_three.collidepoint(event.pos):
                    depth_one_color = white
                    depth_two_color = white
                    depth_three_color = red
                    depth_four_color = white
                    depth_five_color = white
                    depth = 3
                elif depth_four.collidepoint(event.pos):
                    depth_one_color = white
                    depth_two_color = white
                    depth_three_color = white
                    depth_four_color = red
                    depth_five_color = white
                    depth = 4
                elif depth_five.collidepoint(event.pos):
                    depth_one_color = white
                    depth_two_color = white
                    depth_three_color = white
                    depth_four_color = white
                    depth_five_color = red
                    depth = 5
                elif next.collidepoint(event.pos):
                    if depth is not None:
                        return depth
        # Draw mode selection interface here
        font = pygame.font.Font(None, 25)
        depth_text = font.render("Select depth for machine:", True, white)
        depth_modul = pygame.Rect(360, 50, 300, 50)
        depth_modul_color = white

        # node to next
        font_big = pygame.font.Font(None, 40)
        next = pygame.Rect(360, 600, 200, 50)
        next_text = font_big.render("Next", True, white)
        pygame.draw.rect(screen, white, next, 3, 6)
        screen.blit(next_text, (next.x + 10, next.y + 10))

        # position of text
        depth_one = pygame.Rect(400, 120, 100, 50)
        depth_two = pygame.Rect(400, 190, 100, 50)
        depth_three = pygame.Rect(400, 260, 100, 50)
        depth_four = pygame.Rect(400, 330, 100, 50)
        depth_five = pygame.Rect(400, 400, 100, 50)

        # color of text

        # text
        depth_one_text = font.render("Depth 1", True, white)
        depth_two_text = font.render("Depth 2", True, white)
        depth_three_text = font.render("Depth 3", True, white)
        depth_four_text = font.render("Depth 4", True, white)
        depth_five_text = font.render("Depth 5", True, white)

        pygame.draw.rect(screen, depth_modul_color, depth_modul, 3, 6)
        pygame.draw.rect(screen, depth_one_color, depth_one, 3, 6)
        pygame.draw.rect(screen, depth_two_color, depth_two, 3, 6)
        pygame.draw.rect(screen, depth_three_color, depth_three, 3, 6)
        pygame.draw.rect(screen, depth_four_color, depth_four, 3, 6)
        pygame.draw.rect(screen, depth_five_color, depth_five, 3, 6)

        screen.blit(depth_text, (depth_modul.x + 10, depth_modul.y + 10))
        screen.blit(depth_one_text, (depth_one.x + 10, depth_one.y + 10))
        screen.blit(depth_two_text, (depth_two.x + 10, depth_two.y + 10))
        screen.blit(depth_three_text, (depth_three.x + 10, depth_three.y + 10))
        screen.blit(depth_four_text, (depth_four.x + 10, depth_four.y + 10))
        screen.blit(depth_five_text, (depth_five.x + 10, depth_five.y + 10))

        pygame.display.update()


def select_depth_two_machine(screen):
    # select depth for tow machine
    # reset background
    background_image = pygame.image.load("bgchess.jpg").convert()
    screen.blit(background_image, [0, 0])

    m1_depth_one_color = white
    m1_depth_two_color = white
    m1_depth_three_color = white
    m1_depth_four_color = white
    m1_depth_five_color = white

    m2_depth_one_color = white
    m2_depth_two_color = white
    m2_depth_three_color = white
    m2_depth_four_color = white
    m2_depth_five_color = white

    depth_machine_1 = None
    depth_machine_2 = None

    # select side
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if buttons were clicked
                if m1_depth_one.collidepoint(event.pos):
                    m1_depth_one_color = red
                    m1_depth_two_color = white
                    m1_depth_three_color = white
                    m1_depth_four_color = white
                    m1_depth_five_color = white
                    depth_machine_1 = 1
                elif m1_depth_two.collidepoint(event.pos):
                    m1_depth_one_color = white
                    m1_depth_two_color = red
                    m1_depth_three_color = white
                    m1_depth_four_color = white
                    m1_depth_five_color = white
                    depth_machine_1 = 2
                elif m1_depth_three.collidepoint(event.pos):
                    m1_depth_one_color = white
                    m1_depth_two_color = white
                    m1_depth_three_color = red
                    m1_depth_four_color = white
                    m1_depth_five_color = white
                    depth_machine_1 = 3
                elif m1_depth_four.collidepoint(event.pos):
                    m1_depth_one_color = white
                    m1_depth_two_color = white
                    m1_depth_three_color = white
                    m1_depth_four_color = red
                    m1_depth_five_color = white
                    depth_machine_1 = 4
                elif m1_depth_five.collidepoint(event.pos):
                    m1_depth_one_color = white
                    m1_depth_two_color = white
                    m1_depth_three_color = white
                    m1_depth_four_color = white
                    m1_depth_five_color = red
                    depth_machine_1 = 5
                elif m2_depth_one.collidepoint(event.pos):
                    m2_depth_one_color = red
                    m2_depth_two_color = white
                    m2_depth_three_color = white
                    m2_depth_four_color = white
                    m2_depth_five_color = white
                    depth_machine_2 = 1
                elif m2_depth_two.collidepoint(event.pos):
                    m2_depth_one_color = white
                    m2_depth_two_color = red
                    m2_depth_three_color = white
                    m2_depth_four_color = white
                    m2_depth_five_color = white
                    depth_machine_2 = 2
                elif m2_depth_three.collidepoint(event.pos):
                    m2_depth_one_color = white
                    m2_depth_two_color = white
                    m2_depth_three_color = red
                    m2_depth_four_color = white
                    m2_depth_five_color = white
                    depth_machine_2 = 3
                elif m2_depth_four.collidepoint(event.pos):
                    m2_depth_one_color = white
                    m2_depth_two_color = white
                    m2_depth_three_color = white
                    m2_depth_four_color = red
                    m2_depth_five_color = white
                    depth_machine_2 = 4
                elif m2_depth_five.collidepoint(event.pos):
                    m2_depth_one_color = white
                    m2_depth_two_color = white
                    m2_depth_three_color = white
                    m2_depth_four_color = white
                    m2_depth_five_color = red
                    depth_machine_2 = 5
                elif next.collidepoint(event.pos):
                    if depth_machine_1 is not None and depth_machine_2 is not None:
                        return depth_machine_1, depth_machine_2
        # Draw mode selection interface here
        font = pygame.font.Font(None, 25)
        depth_text = font.render("Select depth for machine:", True, white)
        depth_modul = pygame.Rect(360, 50, 300, 50)
        depth_modul_color = white

        # node to next
        font_big = pygame.font.Font(None, 40)
        next = pygame.Rect(360, 600, 200, 50)
        next_text = font_big.render("Next", True, white)
        pygame.draw.rect(screen, white, next, 3, 6)
        screen.blit(next_text, (next.x + 10, next.y + 10))

        # position of text
        m1_depth_one = pygame.Rect(400, 120, 100, 50)
        m1_depth_two = pygame.Rect(400, 190, 100, 50)
        m1_depth_three = pygame.Rect(400, 260, 100, 50)
        m1_depth_four = pygame.Rect(400, 330, 100, 50)
        m1_depth_five = pygame.Rect(400, 400, 100, 50)

        m2_depth_one = pygame.Rect(550, 120, 100, 50)
        m2_depth_two = pygame.Rect(550, 190, 100, 50)
        m2_depth_three = pygame.Rect(550, 260, 100, 50)
        m2_depth_four = pygame.Rect(550, 330, 100, 50)
        m2_depth_five = pygame.Rect(550, 400, 100, 50)

        # color of text

        # text
        depth_one_text = font.render("Depth 1", True, white)
        depth_two_text = font.render("Depth 2", True, white)
        depth_three_text = font.render("Depth 3", True, white)
        depth_four_text = font.render("Depth 4", True, white)
        depth_five_text = font.render("Depth 5", True, white)

        pygame.draw.rect(screen, depth_modul_color, depth_modul, 3, 6)
        pygame.draw.rect(screen, m1_depth_one_color, m1_depth_one, 3, 6)
        pygame.draw.rect(screen, m1_depth_two_color, m1_depth_two, 3, 6)
        pygame.draw.rect(screen, m1_depth_three_color, m1_depth_three, 3, 6)
        pygame.draw.rect(screen, m1_depth_four_color, m1_depth_four, 3, 6)
        pygame.draw.rect(screen, m1_depth_five_color, m1_depth_five, 3, 6)

        pygame.draw.rect(screen, m2_depth_one_color, m2_depth_one, 3, 6)
        pygame.draw.rect(screen, m2_depth_two_color, m2_depth_two, 3, 6)
        pygame.draw.rect(screen, m2_depth_three_color, m2_depth_three, 3, 6)
        pygame.draw.rect(screen, m2_depth_four_color, m2_depth_four, 3, 6)
        pygame.draw.rect(screen, m2_depth_five_color, m2_depth_five, 3, 6)

        screen.blit(depth_text, (depth_modul.x + 10, depth_modul.y + 10))
        screen.blit(depth_one_text, (m1_depth_one.x + 10, m1_depth_one.y + 10))
        screen.blit(depth_two_text, (m1_depth_two.x + 10, m1_depth_two.y + 10))
        screen.blit(depth_three_text,
                    (m1_depth_three.x + 10, m1_depth_three.y + 10))
        screen.blit(depth_four_text,
                    (m1_depth_four.x + 10, m1_depth_four.y + 10))
        screen.blit(depth_five_text,
                    (m1_depth_five.x + 10, m1_depth_five.y + 10))

        screen.blit(depth_one_text, (m2_depth_one.x + 10, m2_depth_one.y + 10))
        screen.blit(depth_two_text, (m2_depth_two.x + 10, m2_depth_two.y + 10))
        screen.blit(depth_three_text,
                    (m2_depth_three.x + 10, m2_depth_three.y + 10))
        screen.blit(depth_four_text,
                    (m2_depth_four.x + 10, m2_depth_four.y + 10))
        screen.blit(depth_five_text,
                    (m2_depth_five.x + 10, m2_depth_five.y + 10))

        pygame.display.update()


def human_match(screen):
    game = ChessGame2(screen=screen)
    game.start()


def human_machine_match(screen, depth, side):
    if side == "white":
        game = ChessGame2(screen=screen, ai_1_level=depth, ai_side=True)
        game.start()
    else:
        game = ChessGame2(screen=screen, ai_1_level=depth, ai_side=False)
        game.start()


def machine_match(screen, depth_machine_1, depth_machine_2):
    game = ChessGame2(
        screen=screen, ai_1_level=depth_machine_1, ai_2_level=depth_machine_2
    )
    game.start()


if __name__ == "__main__":
    start_game()
