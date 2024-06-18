import pygame
import sys
from const import *
import numpy as np

pygame.init()

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("TIC TAC TOE")
screen.fill(BG_COLLOR)

# board 
board = np.zeros((BOARD_ROWS,BOARD_COLS))

print(board)

## Coordinates for the board 
'''
(0,0),(1,0)
(1,1), ..., (xn,yn)


        (600,600)
'''

#pygame.draw.line(screen,GREEN ,(10,10),(300,300),10)

def draw_lines():
    # First horisontal line
    pygame.draw.line(screen,LINE_COLOR,(0,200),(600,200),LINE_WIDHT)
    # Second horisontal line 
    pygame.draw.line(screen,LINE_COLOR,(0,400),(600,400),LINE_WIDHT)
    
    # 1.Verical line 
    pygame.draw.line(screen,LINE_COLOR,(200,0),(200,600),LINE_WIDHT)
    
    # 2. Veritcal Line
    pygame.draw.line(screen,LINE_COLOR,(400,0),(400,600),LINE_WIDHT)


# Draw figures on screen 
def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS): 
            if board[row][col] == 1: 
                pygame.draw.circle(screen,GREEN,(int(col * 200 + 200 /2),int (row * 200 + 200 / 2)),CIRCLE_RADIUS,CIRCLE_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.line(screen,BLUE,(col * 200 + SPACE ,row * 200 + 200 - SPACE),(col * 200 + 200 -SPACE, row * 200 + SPACE),LINE_WIDHT_CROSS)
                pygame.draw.line(screen,BLUE,(col * 200 + SPACE ,row * 200 + SPACE),(col * 200 + 200 -SPACE, row * 200 + 200 - SPACE),LINE_WIDHT_CROSS)

'''
def draw_line(): 
    for row in range(BOARD_ROWS): 
        for col in range(BOARD_COLS): 
            if board[row][col] == 2: 
                pygame.draw.line(screen,BLUE,int(row%2),int(col%2),10)
'''

## Mark a square with a 1
def mark_square(row,col,player): 
    board[row][col]  = player
    
## Check if the square is empty or not
def avilable_square(row,col): 
    if board[row][col] == 0: 
        return True
    else: 
        return False


## check if there is an empty square left
def board_full(): 
    for row in range(BOARD_ROWS): 
        for col in range(BOARD_COLS): 
            if board[row][col] == 0:
                return False
    return True
            

mark_square(0,0,1)
print(board)

## Check if the square is avilable or not 
print(avilable_square(0,0))


print("Is the board full:",board_full())

draw_lines()

player =1
## Main loop
while True:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX = event.pos[0] # x-coordinate
            mouseY = event.pos[1] # y-coodinate
        
            cicked_row = int(mouseY // 200) 
            clicked_col = int(mouseX // 200)   
    
            if avilable_square(cicked_row,clicked_col):
                if player == 1: 
                    mark_square(cicked_row,clicked_col,1)
                    player = 2
                    
                elif player == 2:
                    mark_square(cicked_row,clicked_col,2)
                    player = 1
                draw_figures()    
            
    pygame.display.update()