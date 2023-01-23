import pygame
pygame.init() #Init of all imported pygame modules
dis = pygame.display.set_mode((400,300)) #size of the snake game window
pygame.display.update() #Updates the screen
pygame.display.set_caption('GAME: Snake')
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Closing the snake game
            game_over = True

pygame.quit()
quit()
