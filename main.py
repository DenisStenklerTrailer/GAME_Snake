import pygame
import time
import random

pygame.init() #Init of all imported pygame modules

Game_Height = 600
Game_Width = 800

dis = pygame.display.set_mode((Game_Width,Game_Height)) #size of the snake game window

pygame.display.set_caption('GAME: Snake')

background = (200,200,200)
blue = (0,0,255)
red = (255,0,0)
white = (0,0,0)

snake_block = 10

clock = pygame.time.Clock()

font_style = pygame.font.SysFont(None, 20)

def message (msg,color): # Message created when we hit the end of the map
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg,[Game_Width/2,Game_Height/2])

def gameLoop():
    game_over = False
    game_close = False

    x1 = Game_Width / 2
    y1 = Game_Height / 2

    x1_Changed = 0
    y1_Changed = 0

    LEFT_Direction = False
    RIGHT_Direction = False
    UP_Direction = False
    DOWN_Direction = False

    foodx = round(random.randrange(0, Game_Width - snake_block) / 10) * 10
    foody = round(random.randrange(0, Game_Width - snake_block) / 10) * 10

    while not game_over:

        while game_close == True:
            dis.fill(white)
            message("You lost! Press Q-Quit or O-Play Again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_o:
                        gameLoop()

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
            game_close = True

        x1 = x1 + x1_Changed
        y1 = y1 + y1_Changed

        dis.fill(background)

        pygame.draw.rect(dis, blue,[foodx,foody, 10, 10])
        pygame.draw.rect(dis,blue,[x1,y1,10,10]) # drawing snake (position and size)
        pygame.display.update()  # Updates the screen

        if x1 == foodx and y1 == foody:
            print("WE EATED THE FOOD")

        clock.tick(20)

    message("You lost", red)
    pygame.display.update()
    time.sleep(2)

    pygame.quit()
    quit()

gameLoop()