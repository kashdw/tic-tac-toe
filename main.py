import pygame, math, sys
import numpy as np

pygame.init()  # initializes pygame

# constants
WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 13
BACK_COLOR = (229, 204, 255)
LINE_COLOR = (0, 0, 0)
ROWS = 3
COLS = 3
CIRCLE_COLOR = (204, 102, 0)
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
X_COLOR = (0, 102, 102)
X_WIDTH = 25
X_SPACE = 55  # space between lines and corners

# screen window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(BACK_COLOR)
pygame.display.set_caption('Tic Tac Toe')

# console board
board = np.zeros((ROWS, COLS))

def draw_lines():
    pygame.draw.line(screen, LINE_COLOR, (WIDTH / 3, 0), (WIDTH / 3, HEIGHT),
                     LINE_WIDTH)  # surface, color, start pos, end pos, line width
    pygame.draw.line(screen, LINE_COLOR, ((WIDTH / 3) * 2, 0), ((WIDTH / 3) * 2, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, HEIGHT/3), (WIDTH, HEIGHT/3), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, (HEIGHT / 3)*2), (WIDTH, (HEIGHT / 3)*2), LINE_WIDTH)

def draw_letters():
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == 1: # if player 1 has marked the square
                pygame.draw.line(screen, X_COLOR, (col * WIDTH / 3 + X_SPACE, row * HEIGHT / 3 + HEIGHT / 3 - X_SPACE),
                                 (col * WIDTH / 3 + WIDTH / 3 - X_SPACE, row * HEIGHT / 3 + X_SPACE), X_WIDTH)
                pygame.draw.line(screen, X_COLOR, (col * WIDTH / 3 + X_SPACE, row * HEIGHT / 3 + X_SPACE),
                                 (col * WIDTH / 3 + WIDTH / 3 - X_SPACE, row * HEIGHT / 3 + HEIGHT / 3 - X_SPACE),
                                 X_WIDTH)
            elif board[row][col] ==2:
                pygame.draw.circle(screen, CIRCLE_COLOR,
                                   (int(col * WIDTH / 3 + WIDTH / 6), int(row * HEIGHT / 3 + HEIGHT / 6)),
                                   CIRCLE_RADIUS, CIRCLE_WIDTH)

def mark_square(row, col, player):
    board[row][col] = player

def available_square(row, col):
    if board[row][col] == 0:
        return True  # 0 represents an empty square
    else:
        return False

def is_board_full():
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == 0:
                return False
    return True

def check_win(player):
    # vertical win check
    for col in range(COLS):
        if board[0][col] == player and board[1][col]== player and board[2][col]==player:
            draw_vertical_line(col, player)
            return True  # breaks the function, doesn't check for other possible wins
    # horizontal win check
    for row in range(ROWS):
        if board[row][0] == player and board[row][1]== player and board[row][2]==player:
            draw_horizontal_line(row, player)
            return True
    # ascending diagonal win check
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_asc_diagonal_(player)
        return True
    # descending diagonal win check
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_desc_diagonal_(player)
        return True
    return False  # if function reaches here, there is no win yet
def draw_vertical_line(col, player):
    posX = col*(WIDTH/3) + WIDTH/6

    if player == 1:
        color = X_COLOR
    elif player == 2:
        color = CIRCLE_COLOR

    pygame.draw.line(screen, color, (posX, 15), (posX, HEIGHT-15), LINE_WIDTH)

def draw_horizontal_line(row, player):
    posY = row*(HEIGHT/3)+HEIGHT/6

    if player == 1:
        color = X_COLOR
    elif player == 2:
        color = CIRCLE_COLOR

    pygame.draw.line(screen, color, (15, posY), (WIDTH-15, posY), LINE_WIDTH)
def draw_asc_diagonal_(player):
    if player == 1:
        color = X_COLOR
    elif player == 2:
        color = CIRCLE_COLOR
    pygame.draw.line(screen, color, (15, HEIGHT-15), (WIDTH-15, 15), LINE_WIDTH)
def draw_desc_diagonal(player):
    if player == 1:
        color = X_COLOR
    elif player == 2:
        color = CIRCLE_COLOR
    pygame.draw.line(screen, color, (15, 15), (WIDTH-15, HEIGHT-15), LINE_WIDTH)
def restart():
    screen.fill(BACK_COLOR)
    draw_lines()
    player = 1
    for row in range(ROWS):
        for col in range(COLS):
            board[row][col] = 0

draw_lines()  # executes code in draw_lines function

player = 1
game_over = False

# main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()  # will cause program to terminate

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]  # x coordinate of click
            mouseY = event.pos[1]  # y coordinate of click

            clicked_row = int(mouseY // 200)  # returns row that mouse has clicked on
            clicked_col = int(mouseX // 200)  # returns column mouse has clicked on

            if available_square(clicked_row, clicked_col):
                if player == 1:
                    mark_square(clicked_row, clicked_col, 1)
                    if check_win(player):
                        game_over = True  # will end game
                    player = 2
                elif player == 2:
                    mark_square(clicked_row, clicked_col, 2)  # denote the clicked square as being clicked by player 2
                    if check_win(player):
                        game_over = True
                    player = 1  # will let us change the player variable

                draw_letters()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                restart()


    pygame.display.update()  # updates screen each time loop is executed
