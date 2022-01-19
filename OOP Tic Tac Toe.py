import math
import numpy as np
import random
import pygame

pygame.__init__
win=pygame.display.set_mode((600,600))
bg_colour=(135, 5, 179)
win.fill(bg_colour)
pygame.display.set_caption("Tic, Tac, Toe")
pygame.display.update()

class TicTacToe:
    turn_number=1
    current_winner=None
    game_over=False
    def __init__(self):
        self.create_board_array()
        self.draw_board()
        self.pygame_run()
    def create_board_array(self):
        self.grid=np.zeros((3,3))  
    def pygame_run(self):
        loop=True
        while loop:
            pygame.time.delay(100)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type==pygame.MOUSEBUTTONDOWN and self.game_over==False:
                    x=event.pos[0]
                    y=event.pos[1]
                    if self.turn_number==1:
                        row,col,player_number=x_player.get_click(x,y)
                    elif self.turn_number==2:
                        row,col,player_number=o_player.get_click(x,y)
                    if self.check_availability(row,col):
                        self.turn(row,col,player_number)
                        self.isWinner()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and self.game_over:
                        self.reset_pygame()
    def reset_pygame(self):
        
    def draw_board(self):
        pygame.draw.line(win,(0,0,0),(150,250),(450,250),10) # HZ 1
        pygame.draw.line(win,(0,0,0),(150,350),(450,350),10) # HZ 2
        pygame.draw.line(win,(0,0,0),(250,150),(250,450),10) # VT 1
        pygame.draw.line(win,(0,0,0),(350,150),(350,450),10) # VT 2
        pygame.display.update()
    def isWinner(self):
        if self.game_over==False:
            for ply in range(1,3):
                for r in range(3):
                    if self.grid[r][0]==self.grid[r][1]==self.grid[r][2]==ply:
                        self.current_winner=ply
                        self.game_over=True
                for c in range(3):
                    if self.grid[0][c]==self.grid[1][c]==self.grid[2][c]==ply:
                        self.current_winner=ply
                        self.game_over=True
                if self.grid[0][0]==self.grid[1][1]==self.grid[2][2]==ply:
                    self.current_winner=ply
                    self.game_over=True
                if self.grid[0][2]==self.grid[1][1]==self.grid[2][0]==ply:
                    self.current_winner=ply
                    self.game_over=True
                if (self.grid!=0).all():
                    self.current_winner="Tie"
                    self.game_over=True     
    def check_availability(self,row,col):
        if self.grid[row][col]==0:
            return True
        else:
            return False
    def circle_pos(self,row,col):
        if row==0 and col==0:
            pos=200,200
        elif row==0 and col==1:
            pos=300,200
        elif row==0 and col==2:
            pos=400,200
        elif row==1 and col==0:
            pos=200,300
        elif row==1 and col==1:
            pos=300,300
        elif row==1 and col==2:
            pos=400,300
        elif row==2 and col==0:
            pos=200,400
        elif row==2 and col==1:
            pos=300,400
        elif row==2 and col==2:
            pos=400,400
        return pos
    def turn(self,row,col,player):
        self.grid[row][col]=player
        x,y=self.circle_pos(row,col)
        if player==1:
            pygame.draw.line(win,(0,0,0),(x,y),(x+40,y-40),10) # up and right
            pygame.draw.line(win,(0,0,0),(x,y),(x-40,y-40),10) # up and left
            pygame.draw.line(win,(0,0,0),(x,y),(x+40,y+40),10) # down and right
            pygame.draw.line(win,(0,0,0),(x,y),(x-40,y+40),10) # down and left
            self.turn_number=2
        elif player==2:
            pygame.draw.circle(win,(0,0,0),(x,y),40,10)
            self.turn_number=1
        pygame.display.update()

class HumanPlayer:
    def __init__(self,letter):
        self.letter=letter
        if self.letter=="X":
            self.player_number=1
        elif self.letter=="O":
            self.player_number=2
    
    def get_click(self,x,y):
        if (x>152 and x<248) and (y>152 and y<248):
            return 0,0,self.player_number
        elif (x>252 and x<348) and (y>152 and y<248):
            return 0,1,self.player_number
        elif (x>352 and x<448) and (y>152 and y<248):
            return 0,2,self.player_number
        elif (x>152 and x<248) and (y>252 and y<348):
            return 1,0,self.player_number
        elif (x>252 and x<348) and (y>252 and y<348):
            return 1,1,self.player_number
        elif (x>352 and x<448) and (y>252 and y<348):
            return 1,2,self.player_number
        elif (x>152 and x<248) and (y>352 and y<448):
            return 2,0,self.player_number
        elif (x>252 and x<348) and (y>352 and y<448):
            return 2,1,self.player_number
        elif (x>352 and x<448) and (y>352 and y<448):
            return 2,2,self.player_number
        else:
            return None, None,self.player_number

def play_game(game,x_ply,o_ply):
    pass

if __name__ == '__main__':
    x_player=HumanPlayer("X")
    o_player=HumanPlayer("O")
    t=TicTacToe()
    play_game(t,x_player,o_player)
