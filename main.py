import pygame
import time
pygame.init() #Init of all imported pygame modules

Game_Height = 600
Game_Width = 800

dis = pygame.display.set_mode((Game_Width,Game_Height)) #size of the snake game window

pygame.display.set_caption('GAME: Snake')
game_over = False

background = (200,200,200)
blue = (0,0,255)
red = (255,0,0)

LEFT_Direction = False
RIGHT_Direction = False
UP_Direction = False
DOWN_Direction = False

x1 = Game_Width / 2
y1 = Game_Height / 2

x1_Changed = 0
y1_Changed = 0

clock = pygame.time.Clock()

font_style = pygame.font.SysFont(None, 50)

def message (msg,color): # Message created when we hit the end of the map
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg,[Game_Width/2,Game_Height/2])

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Closing the snake game
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and RIGHT_Direction == False:
                x1_Changed = -10
                y1_Changed = 0
                LEFT_Direction = True
                RIGHT_Direction = False
                UP_Direction = False
                DOWN_Direction = False
            elif event.key == pygame.K_RIGHT and LEFT_Direction == False:
                x1_Changed = 10
                y1_Changed = 0
                LEFT_Direction = False
                RIGHT_Direction = True
                UP_Direction = False
                DOWN_Direction = False
            elif event.key == pygame.K_UP and DOWN_Direction == False:
                x1_Changed = 0
                y1_Changed = -10
                LEFT_Direction = False
                RIGHT_Direction = False
                UP_Direction = True
                DOWN_Direction = False
            elif event.key == pygame.K_DOWN and UP_Direction == False:
                x1_Changed = 0
                y1_Changed = 10
                LEFT_Direction = False
                RIGHT_Direction = False
                UP_Direction = False
                DOWN_Direction = True

    if x1 > Game_Width or x1 < 0 or y1 > Game_Height or y1 < 0:
        game_over = True

    x1 = x1 + x1_Changed
    y1 = y1 + y1_Changed

    dis.fill(background)

    pygame.draw.rect(dis,blue,[x1,y1,10,10]) # drawing snake (position and size)
    pygame.display.update()  # Updates the screen

    clock.tick(20)

if game_over == True:
    message("You lost", red)
    pygame.display.update()
    time.sleep(2)

    pygame.quit()
    quit()
