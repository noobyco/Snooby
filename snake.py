from pygame.locals import *
import pygame
import random
import time



#Initialize..
pygame.init()
Win_Size = [800,500]

Display = pygame.display.set_mode(Win_Size)
pygame.display.set_caption("Snake-game")
clock = pygame.time.Clock()




##Colors..
red = [254,5,0]
green = [192,255,24]
blue = [17,29,94]
black = [0,0,0]
white = [255,255,255]
orange = [243,113,33]
##Font Object..
font = pygame.font.SysFont(None, 25)

def snake(block_width,block_height,SnakeList):
    for XnY in SnakeList:
        Block = pygame.draw.rect(Display,green,(XnY[0],XnY[1],block_width,block_height))
def text(msg,color,x,y):
    screen_text = font.render(msg, True, color)
    Display.blit(screen_text, [x,y])



def Game_Loop():
    ##Block_Object
    SnakeList = []
    SnakeLength = 3
    
    pos_x = Win_Size[0]/2
    pos_y = Win_Size[1]/2
    pos_x_change = 0
    pos_y_change = 0
    snake_width = 10
    snake_height = 10
    
    snake_step = 15

    ##Apple_Object
    
    apple_width = 20
    apple_height = 20
    randApple_x = round(random.randrange(0,Win_Size[0]-apple_width))
    randApple_y = round(random.randrange(0,Win_Size[1]-apple_height))
    
    ##Game_setting
    Game_Exit = False
    Game_Over = False
    Fps = 15
        
    while not Game_Exit:

        while Game_Over == True:
            Display.fill(black)
            text("GAME OVER!", orange,Win_Size[0]/2,Win_Size[1]/2)
            text("Press c to continue.",orange,(Win_Size[0]/2)-20,(Win_Size[1]/2)+15)
            text("Press q to Quit.", orange,(Win_Size[0]/2)-20,(Win_Size[1]/2)+25)
            
            
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    Game_Exit = True
                    Game_Over = False
                if event.type == KEYDOWN:
                    if event.key == K_c:
                        Game_Loop()
                    if event.key == K_q:
                        Game_Exit = True
                        Game_Over = False
                            
            

        for event in pygame.event.get():
            if event.type == QUIT:
                Game_Exit = True

            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    pos_x_change = -snake_step
                    pos_y_change = 0
                if event.key == K_RIGHT:
                    pos_x_change = snake_step
                    pos_y_change = 0
                if event.key == K_UP:
                    pos_y_change = -snake_step
                    pos_x_change = 0
                if event.key == K_DOWN:
                    pos_y_change = snake_step
                    pos_x_change = 0
                    
        ## Wall collision...
        if pos_x < 0 or pos_x > Win_Size[0] or pos_y < 0 or pos_y > Win_Size[1]:
            Game_Over = True

        ## Snake Collision with Apple...     
        if pos_x > randApple_x and pos_x < randApple_x + apple_width or pos_x + snake_width > randApple_x and pos_x + snake_width < randApple_x + apple_width:
            if pos_y > randApple_y and pos_y < randApple_y + apple_height or pos_y + snake_height > randApple_y and pos_y + snake_height < randApple_y + apple_height:
                randApple_x = round(random.randrange(0,Win_Size[0]-apple_width))
                randApple_y = round(random.randrange(0,Win_Size[1]-apple_height))
                SnakeLength +=1
            
            
        pos_x += pos_x_change
        pos_y += pos_y_change

        

        ##Canvas
        
        Display.fill(blue)

        ## Apple Object...
        Apple = pygame.draw.rect(Display, red,(randApple_x,randApple_y,apple_width,apple_height))
        SnakeHead = []
        SnakeHead.append(pos_x)
        SnakeHead.append(pos_y)
        SnakeList.append(SnakeHead)

        
        
        if len(SnakeList) > SnakeLength:
            del SnakeList[0]

        ## Self collision...
        for eachSegment in SnakeList[:-3]:
            if eachSegment == SnakeHead:
                Game_Over = True
                
        ## Snake Object...    
        snake(snake_width,snake_height,SnakeList)
        
        pygame.display.update()
        clock.tick(Fps)

    
    pygame.quit()
    quit()

Game_Loop()
