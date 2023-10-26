import pygame
import sys

from game_parameters import *
from background import draw_background

#initializing pygame
pygame.init()
#create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Fish Game")


#main loop
running = True
background = screen.copy()
draw_background(background)

while running:
    for event in pygame.event.get():
        #print(event.type)
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                print('you pressed W')
            elif event.key == pygame.K_a:
                print('you pressed A')
            elif event.key == pygame.K_s:
                print('you pressed S')
            elif event.key == pygame.K_d:
                print('you pressed D')

    #draw background
    screen.blit(background, (0,0))

    #update the display by flipping
    pygame.display.flip()

pygame.quit()
sys.exit()


