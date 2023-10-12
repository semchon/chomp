import pygame
import sys
import random
#now we need to initialize pygame
pygame.init()

#screen dimensions
screen_width = 800
screen_height = 600

#adding tile dimensions
tile_size = 64

#create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Using blit to draw tiles")

#drawing background
def draw_background(screen):
    #loading tiles from files. The .convert loads the image
    water = pygame.image.load("assets/sprites/water.png").convert()
    sand = pygame.image.load("assets/sprites/sand_top.png").convert()
    seagrass = pygame.image.load("assets/sprites/seagrass.png").convert()

    #make PNGs transparent
    water.set_colorkey((0,0,0))
    sand.set_colorkey((0, 0, 0))
    seagrass.set_colorkey((0, 0, 0))

    #fill screen with water
    for x in range(0, screen_width, tile_size):
        for y in range(0, screen_height, tile_size):
            screen.blit(water, (x,y))

    #draw sandy bottom
    for x in range(0, screen_width, tile_size):
        screen.blit(sand, (x, screen_height - tile_size))

    #place seagrass
    for _ in range(10):
        x = random.randint(0,screen_width)
        screen.blit(seagrass, (x, 480))


#main loop
running = True
background = screen.copy()
draw_background(background)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.blit(background, (0,0))
    pygame.display.flip()
pygame.quit()

