import pygame,sys
import numpy as np

pygame.__init__
WIDTH=600
HEIGHT=600
bg_colour=(135, 5, 179)
LINE=(0,0,0)
win=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Tic, Tac, Toe")
win.fill(bg_colour)
grid=np.zeros((3,3))

class Player:
    def __init__(self,type):
        self.type=type
def draw_grid():
    pygame.draw.line(win,LINE,(150,250),(450,250),10) # HZ 1
    pygame.draw.line(win,LINE,(150,350),(450,350),10) # HZ 2
    pygame.draw.line(win,LINE,(250,150),(250,450),10) # VT 1
    pygame.draw.line(win,LINE,(350,150),(350,450),10)
def check_availability(row,col):
    if grid[row][col]==0:
        return True
    else:
        return False
def circle_pos(row,col):
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
def turn(row,col,player):
    grid[row][col]=player
    x,y=circle_pos(row,col)
    if player==1:
        pygame.draw.line(win,LINE,(x,y),(x+40,y-40),10) # up and right
        pygame.draw.line(win,LINE,(x,y),(x-40,y-40),10) # up and left
        pygame.draw.line(win,LINE,(x,y),(x+40,y+40),10) # down and right
        pygame.draw.line(win,LINE,(x,y),(x-40,y+40),10) # down and left
    elif player==2:
        pygame.draw.circle(win,LINE,(x,y),20,10)
    pygame.display.update()    
def grid_complete():
    for row in range(3):
        for col in range(3):
            if grid[row][col]=0:
                return False
    return True
def winner():
    pass
    
def valid_click(x,y):
    if (x>152 and x<248) and (y>152 and y<248):
        return 0,0
    elif (x>252 and x<348) and (y>152 and y<248):
        return 0,1
    elif (x>352 and x<448) and (y>152 and y<248):
        return 0,2
    elif (x>152 and x<248) and (y>252 and y<348):
        return 1,0
    elif (x>252 and x<348) and (y>252 and y<348):
        return 1,1
    elif (x>352 and x<448) and (y>252 and y<348):
        return 1,2
    elif (x>152 and x<248) and (y>352 and y<448):
        return 2,0
    elif (x>252 and x<348) and (y>352 and y<448):
        return 2,1
    elif (x>352 and x<448) and (y>352 and y<448):
        return 2,2
    else:
        return None, None
def game(row,col,ply):
    if check_availability(row,col):
        if ply==1:
            turn(row,col,ply)
            ply+=1
        elif ply==2:
            turn(row,col,ply)
            ply-=1


draw_grid()

loop=True
global ply
ply=1
while loop:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            x=event.pos[0]
            y=event.pos[1]
            row,col=valid_click(x,y)
            if row != None:
                game(row,col,ply)
    
    pygame.display.update()