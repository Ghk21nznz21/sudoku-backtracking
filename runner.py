import time

import numpy
import pygame

from classes import *
from solver_functions import *
from var_handlers import *
from visuals import *

pygame.font.init()  


def main():
    window = pygame.display.set_mode((540,600))
    pygame.display.set_caption("Sudoku")
    board = Grid(9, 9, 540, 540)            #board is now a instance of grid class
    solved_board_var =solved_board(board.board_ini)
    run = True
    key=None
    strikes=0
    end=False
    start=time.time()
    while run:
        play_time=round( time.time()-start )
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    key = 1
                if event.key == pygame.K_2:
                    key = 2
                if event.key == pygame.K_3:
                    key = 3
                if event.key == pygame.K_4:
                    key = 4
                if event.key == pygame.K_5:
                    key = 5
                if event.key == pygame.K_6:
                    key = 6
                if event.key == pygame.K_7:
                    key = 7
                if event.key == pygame.K_8:
                    key = 8
                if event.key == pygame.K_9:
                    key = 9
                if event.key == pygame.K_SPACE :
                    i,j=board.tip()
                    board.cubes[i][j].set_val(solved_board_var[i][j])
                    if not(board.finished() ):
                        text='now try without tips!'
                        end=True
                        run=False
                        
                if event.key == pygame.K_DELETE or event.key==pygame.K_BACKSPACE :
                    board.clear()   
                    key = None
                if event.key == pygame.K_RETURN:
                    i,j=board.selected
                    if board.cubes[i][j].value ==0 and board.cubes[i][j].temp!=0:
                        if not (board.convert_to_value(board.cubes[i][j].temp,solved_board_var[i][j]) ): #corret val. runs the solver for the new board
                            strikes +=1
                            if strikes>=3:
                                text='Game Over you Lost'
                                end=True
                                run= False

                    if not(board.finished() ):
                        text='Game Over you Won'
                        end=True
                        run=False
                    key=None

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                mouse_pos_x_y= board.mouse_clicked_pos(pos) #return (i,j) cube 
                if mouse_pos_x_y: 
                    board.mouse_clicked(mouse_pos_x_y[0], mouse_pos_x_y[1])

        if key != None and board.selected : #mouse clicked
            board.sketch(key)
            key=None

        window_draw(window,board,play_time,strikes)
        pygame.display.update()
        if end:
            if draw_end(window,text):
                run,key,strikes,end,start=restart_vars()
                board=Grid(9, 9, 540, 540)
                
main()
pygame.quit()
