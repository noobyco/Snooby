from pygame.locals import *
from pygame import mixer
import pygame
import random





#Initialize..

pygame.init()
Win_Size = [800,500]
iconPath = 'images/icon.png'
icon = pygame.image.load(iconPath)
Display = pygame.display.set_mode(Win_Size)
pygame.display.set_caption("Snooby")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()



##Images...

startScreenPath = 'images/start.png'
ApplePath = 'images/Apple.png'
pausedPath = 'images/pause.png'

startScreen = pygame.image.load(startScreenPath)
Apple = pygame.image.load(ApplePath)
paused = pygame.image.load(pausedPath)




##Colors..

red = [254,5,0]
green = [192,255,24]
blue = [17,29,94]
black = [0,0,0]
white = [255,255,255]
orange = [243,113,33]


## Sounds...

mixer.pre_init(44100, -16, 2, 512)

gameMusicPath = 'sounds/GameMusic.mp3'
gameOverPath = 'sounds/GameOver.mp3'

mixer.music.load(gameMusicPath)
gameover_sound = mixer.Sound(gameOverPath)

    
##Highest Score...
        
HS = 0


##Font Object...

font = pygame.font.SysFont("comicsansms", 30)

def snake(block_width,block_height,SnakeList):
    for XnY in SnakeList:
        Block = pygame.draw.rect(Display,green,(XnY[0],XnY[1],block_width,block_height))

def text_object(text,color):
    text_area = font.render(text, True, color)
    return text_area , text_area.get_rect()

def text(msg,color):
    surface , textRect = text_object(msg, color)
    textRect.center = (Win_Size[0]/2),(Win_Size[1]/2)
    Display.blit(surface, textRect)


##Pause function...
    
def Pause_Screen():
    Pause = True
    mixer.music.fadeout(1000)
    while Pause:

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_c:
                    mixer.music.play(-1)
                    Pause = False

                if event.key == K_q:
                    pygame.quit()
                    quit()
                    
        
        Display.blit(paused,[0,0])
        pygame.display.update()
        clock.tick(5)
               
def Start_Screen():
    StartLoop = True
    
    while StartLoop == True:
        Display.fill(white)
        Display.blit(startScreen, [0,0])
 
        
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()

            if event.type == KEYDOWN:
                if event.key == K_c:
                    StartLoop = False

                if event.key == K_q:
                    pygame.quit()
                    quit()
        
def Game_Loop():

    
    ##Snake_Object
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
    Game_Update = True
    Fps = 20
    
    mixer.music.play(-1)
    mixer.music.set_volume(0.4)


    while not Game_Exit:
        global HS
        score = (SnakeLength-3)
        
        if score > HS:
            HS = score
            
        while Game_Over == True:
            Display.fill(black)
            gameover_sound.set_volume(0.1)
            gameover_sound.play()
                        
            text("HIGHEST SCORE : {}".format(str(HS)), white)
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    Game_Exit = True
                    Game_Over = False
                if event.type == KEYDOWN:
                    if event.key == K_c:
                        mixer.music.play(-1)
                        gameover_sound.fadeout(100)
                        Game_Loop()
                    if event.key == K_q:
                        Game_Exit = True
                        Game_Over = False
                  
            
             
            

        for event in pygame.event.get():
            if event.type == QUIT:
                mixer.music.fadeout(100)
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
                    
                if event.key == K_p:
                    Pause_Screen()
                    
        ## Wall collision...
        if pos_x < 0 or pos_x > Win_Size[0] or pos_y < 0 or pos_y > Win_Size[1]:
            mixer.music.fadeout(1000)
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
        
        Display.blit(Apple,[randApple_x,randApple_y])
        SnakeHead = []
        SnakeHead.append(pos_x)
        SnakeHead.append(pos_y)
        SnakeList.append(SnakeHead)

        
        
        if len(SnakeList) > SnakeLength:
            del SnakeList[0]

        ## Self collision...
        for eachSegment in SnakeList[:-3]:
            if eachSegment == SnakeHead:
                mixer.music.fadeout(1000)
                Game_Over = True
                
                
        ## Snake Object...    
        snake(snake_width,snake_height,SnakeList)
        
        ## Score Board...
        if (SnakeLength-3) > 0:
            text(str(SnakeLength-3),white)

        

        pygame.display.update()
        clock.tick(Fps)

    
    pygame.quit()
    quit()
    
## Game call...
    
Start_Screen()



Game_Loop()
