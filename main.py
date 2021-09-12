import pygame
import os
import time
from board import Board



pygame.display.set_caption("Queen´s solver")
pygame.font.init()
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
FPS=60
QUEEEN_IMAGE = pygame.image.load(os.path.join('Assets/queen.png'))
ADD_IMAGE = pygame.image.load(os.path.join('Assets/add.png'))
SUBTRACT_IMAGE= pygame.image.load(os.path.join('Assets/subtract.png'))
ADD = pygame.transform.scale(ADD_IMAGE,(35, 35))
SUBTRACT = pygame.transform.scale(SUBTRACT_IMAGE,(35, 35))
BUTTONS_FONT = pygame.font.SysFont('lucidasans', 18, bold=True)
TITLE_FONT = pygame.font.SysFont('Palatino Linotype', 32, bold=True, italic=True)

def draw_screen(board, start_button, more_queens_button, less_queens_button):
    SCREEN.fill(('#E8E6E0'))
    board.draw_board(SCREEN, QUEEEN_IMAGE)
    pygame.draw.rect(SCREEN, ('#FFFFFF'), start_button, border_radius=10)
    pygame.draw.rect(SCREEN, ('#FFFFFF'), more_queens_button, border_radius=100)
    pygame.draw.rect(SCREEN, ('#FFFFFF'), less_queens_button, border_radius=100)
    SCREEN.blit(ADD, (more_queens_button.x +7.5, more_queens_button.y +7.5))
    SCREEN.blit(SUBTRACT, (less_queens_button.x +7.5, less_queens_button.y +7.5))
    SCREEN.blit(BUTTONS_FONT.render('Solve', 1,(0,0,0)),(start_button.x+10, start_button.y+15))
    SCREEN.blit(TITLE_FONT.render('Queens Alive', 1, (0,0,0)), (300,25))

    pygame.display.update()

def main():

    pygame.init()
    running = True
    clock = pygame.time.Clock()

    solve_button= pygame.Rect(50,100,70,50)
    more_queens_button= pygame.Rect(50, 170, 50 ,50)
    less_queens_button= pygame.Rect(50, 230, 50, 50)

    board = Board(4)

    while running:
        clock.tick(FPS)
    
        for event in pygame.event.get():
            mouse_pos= pygame.mouse.get_pos()
            if event.type==pygame.QUIT:
                running=False
                pygame.quit()
            if event.type==pygame.MOUSEBUTTONDOWN and solve_button.collidepoint(mouse_pos):
                start_time = time.time()
                board.solve(0)
                print(time.time() - start_time, "seconds")
                print(board.matrix)
            if event.type==pygame.MOUSEBUTTONDOWN and more_queens_button.collidepoint(mouse_pos) and board.N+1<20:
                board.reset_board(1)
            if event.type==pygame.MOUSEBUTTONDOWN and less_queens_button.collidepoint(mouse_pos) and board.N-1>0:
                board.reset_board(-1)

        draw_screen(board, solve_button, more_queens_button, less_queens_button)
    main()

if __name__ == '__main__':
    main()