import pygame
pygame.init() #Init of all imported pygame modules
dis = pygame.display.set_mode((800,600)) #size of the snake game window

pygame.display.set_caption('GAME: Snake')
game_over = False

background = (200,200,200)
blue = (0,0,255)
red = (255,0,0)

x1 = 300
y1 = 300

x1_Changed = 0
y1_Changed = 0

clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Closing the snake game
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_Changed = -10
                y1_Changed = 0
            elif event.key == pygame.K_RIGHT:
                x1_Changed = 10
                y1_Changed = 0
            elif event.key == pygame.K_UP:
                x1_Changed = 0
                y1_Changed = -10
            elif event.key == pygame.K_DOWN:
                x1_Changed = 0
                y1_Changed = 10

    x1 = x1 + x1_Changed
    y1 = y1 + y1_Changed
    dis.fill(background)
    pygame.draw.rect(dis,blue,[x1,y1,10,10]) # drawing snake (position and size)
    pygame.display.update()  # Updates the screen

    clock.tick(20)

pygame.quit()
quit()
