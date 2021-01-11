import pygame
import time
import random
from pygame.locals import *


#Initialize..
pygame.init()
Win_Size = [800,500]

Display = pygame.display.set_mode(Win_Size)
pygame.display.set_caption("Snake.io")
clock = pygame.time.Clock()




##Colors..
red = [225,0,0]
blue = [0,0,255]
black = [0,0,0]
white = [255,255,255]

##Font Object..
font = pygame.font.SysFont(None, 20)

def snake(block_width,block_height,SnakeList):
    for XnY in SnakeList:
        Block = pygame.draw.rect(Display,blue,(XnY[0],XnY[1],block_width,block_height))
def text(msg,color):
    screen_text = font.render(msg, True, color)
    Display.blit(screen_text, [Win_Size[0]/2,Win_Size[1]/2])



def Game_Loop():
##Block_Object
    SnakeList = []
    SnakeLength = 3
    
    pos_x = Win_Size[0]/2
    pos_y = Win_Size[1]/2
    pos_x_change = 0
    pos_y_change = 0
    block_width = 10
    block_height = 10
    velocity = 10

    ##Apple_Object
    randApple_x = round(random.randrange(0,Win_Size[0]-block_width)/10.0)*10.0
    randApple_y = round(random.randrange(0,Win_Size[1]-block_height)/10.0)*10.0
    apple_width = 10
    apple_height = 10
    
    ##Game_setting
    Game_Exit = False
    Game_Over = False
    Fps = 15
        
    while not Game_Exit:

        while Game_Over == True:
            Display.fill(black)
            text("GAME OVER! press c to continue or q to quit.", red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_c:
                        Game_Loop()
                    if event.key == K_q:
                        Game_Exit = True
                        Game_Over = False
                            
            

        for event in pygame.event.get():
            if event.type == QUIT:
                run = True

            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    pos_x_change = -velocity
                    pos_y_change = 0
                if event.key == K_RIGHT:
                    pos_x_change = velocity
                    pos_y_change = 0
                if event.key == K_UP:
                    pos_y_change = -velocity
                    pos_x_change = 0
                if event.key == K_DOWN:
                    pos_y_change = velocity
                    pos_x_change = 0
                    
                    
            """        
            if event.type == KEYUP:
                if event.key == K_LEFT:
                    moving_left = False
                if event.key == K_RIGHT:
                    moving_right = False
                if event.key == K_UP:
                    moving_up = False
                if event.key == K_DOWN:
                    moving_down = False
        """

        if pos_x < 0 or pos_x > Win_Size[0] or pos_y < 0 or pos_y > Win_Size[1]:
            Game_Over = True

        if pos_x == randApple_x and pos_y == randApple_y:
            randApple_x = round(random.randrange(0,Win_Size[0]-block_width)/10.0)*10.0
            randApple_y = round(random.randrange(0,Win_Size[1]-block_height)/10.0)*10.0
            SnakeLength +=1
            #print("um yum yum ")

            
        pos_x += pos_x_change
        pos_y += pos_y_change

        ##Canvas
        
        Display.fill(white)
        Apple = pygame.draw.rect(Display, red,(randApple_x,randApple_y,apple_width,apple_height))
        
        
        SnakeHead = []
        SnakeHead.append(pos_x)
        SnakeHead.append(pos_y)
        SnakeList.append(SnakeHead)

        if len(SnakeList) > SnakeLength:
            del SnakeList[0]
        snake(block_width,block_height,SnakeList)
        
        pygame.display.update()
        clock.tick(Fps)

    
    pygame.quit()
    quit()

Game_Loop()
