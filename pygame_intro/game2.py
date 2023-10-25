import pygame
import sys
import random
import os
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

#load game , designating ttf file and font size
custom_font = pygame.font.Font("assets/fonts/Dried_Leaves.otf", size=128)


#drawing background
def draw_background(surf):
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
            surf.blit(water, (x,y))

    #draw sandy bottom
    for x in range(0, screen_width, tile_size):
        surf.blit(sand, (x, screen_height - tile_size))

    #place seagrass
    for _ in range(10):
        x = random.randint(0,screen_width)
        surf.blit(seagrass, (x, 480))

    #drawing text with imported ttf fonts
    text = custom_font.render("Chomp", True, (255, 29, 0))
    surf.blit(text, (screen_width/2-text.get_width()/2, screen_height/2-300))


def draw_fish(surf):
        #load our fishy tiles
    for i in range(0,5):
        random_fish = random.choice(os.listdir("../game4/fishes"))
        fish_at_hand = pygame.image.load(f"../game4/fishes/{random_fish}").convert()
        fish_at_hand.set_colorkey((0,0,0))
        #^sets transparent color
        x = random.randint(0,800-fish_at_hand.get_width())
        y= random.randint(100, screen_height-(2 * tile_size))
        if i%2 == 0:
            flipped_fishy = pygame.transform.flip(fish_at_hand, flip_x=True,flip_y=False)
            surf.blit(flipped_fishy, (x,y))
        else:
            surf.blit(fish_at_hand, (x,y))

    #randomly distribute our fish


running = True
background = screen.copy()
draw_background(background)
draw_fish(background)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #drawing background
    screen.blit(background, (0,0))

    pygame.display.flip()
pygame.quit()