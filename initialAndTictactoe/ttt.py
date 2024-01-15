import numpy as np
import pygame
import math

ROWS = 3
COLUMNS = 3
Board = np.zeros((ROWS, COLUMNS))
WIDTH = 600
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)
BG_COLOR = (110, 110, 205)
BLACK = (0, 0, 0)

RED = (255, 0, 0)
BLUE = (0, 0, 255)

CIRCLE = pygame.image.load("circle.png")
CROSS = pygame.image.load("x.png")

def mark(x,y,player):
    Board[x][y] =  player

def is_valid_mark(x,y):
    return Board[x][y] == 0

def is_Board_full():
    for x in range(ROWS):
        for y in range(COLUMNS):
            if Board[x][y] == 0:
                return False
    return True

def draw_lines():
    pygame.draw.line(window, BLACK, (200, 0), (200, 600), 10)
    pygame.draw.line(window, BLACK, (400, 0), (400, 600), 10)
    pygame.draw.line(window, BLACK, (0, 200), (600, 200), 10)
    pygame.draw.line(window, BLACK, (0, 400), (600, 400), 10)

def draw_board():
    for r in range(ROWS):
        for c in range(COLUMNS):
            if Board[r][c] == 1:
                window.blit(CIRCLE, ((c*200)+50, (r*200)+50))
            elif Board[r][c] == 2:
                window.blit(CROSS, ((c * 200) + 50, (r * 200) + 50))
    pygame.display.update()

def is_winning_move(player):
    announcement = ""
    if player == 1:
        announcement = BLUE
    else:
        announcement = RED
    # horizontal
    for r in range(ROWS):
        if Board[r][0] == player and Board[r][1] == player and Board[r][2] == player:
            pygame.draw.line(window, announcement, (10, (r*200) + 100), (WIDTH-10, (r*200) + 100), 10)
            return True
    # vertical
    for c in range(COLUMNS):
        if Board[0][c] == player and Board[1][c] == player and Board[2][c] == player:
            pygame.draw.line(window, announcement, ((c*200) + 100, 10), ((c*200)+100, HEIGHT-10), 10)
            return True
    # diagonal top left - bottom right
    if Board[0][0] == player and Board[1][1] == player and Board[2][2] == player:
        pygame.draw.line(window, announcement, (10,10), (590,590), 10)
        return True
    # diagonal top right - bottom left
    if Board[0][2] == player and Board[1][1] == player and Board[2][0] == player:
        pygame.draw.line(window, announcement, (500,10), (10,500), 10)
        return True

game_over = False

Turn = 0

# OPEN A NEW GAME
pygame.init()
# SET WINDOW SIZE
window = pygame.display.set_mode(SIZE)
# SET WINDOW HEADER
pygame.display.set_caption("Tic Tac Toe!")
# SET BACKGROUND COLOR
window.fill(BG_COLOR)
draw_lines()
# UPDATE WINDOW
pygame.display.update()

# # DO NOT CLOSE WINDOW UNLESS USER CLOSED IT
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
# pygame.quit()

# # 2 player, player 1, player 2
while not game_over:
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
             pygame.quit()
         if event.type == pygame.MOUSEBUTTONDOWN:
             print(event.pos)
             if Turn % 2 == 0:
                 # player 1
                 x = math.floor(event.pos[1]/200)
                 y = math.floor(event.pos[0]/200)
                 if is_valid_mark(x,y):
                     mark(x,y, 1)
                     if is_winning_move(1):
                         game_over = True
                     Turn = Turn + 1
             else:
                 # player 2
                 x = math.floor(event.pos[1] / 200)
                 y = math.floor(event.pos[0] / 200)
                 if is_valid_mark(x, y):
                     mark(x, y, 2)
                     if is_winning_move(2):
                         game_over = True
                     Turn = Turn + 1

             print(Board)
             draw_board()
             if game_over == True:
                 print("GAME OVER")
                 # start a new game
                 pygame.time.wait(2000)
                 Board.fill(0)
                 window.fill(BG_COLOR)
                 draw_lines()
                 draw_board()
                 game_over = False
                 pygame.display.update()
