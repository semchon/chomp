import random

import pygame

import os

import sys

from fish import Fish, fishes  # importing the Fish class and fishes group

clock =pygame.time.Clock() #enables tickrate

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

def draw_background(surf):
    #loading tiles from files. The .convert loads the image
    water = pygame.image.load("../pygame_intro/assets/sprites/water.png").convert()
    sand = pygame.image.load("../pygame_intro/assets/sprites/sand_top.png").convert()
    seagrass = pygame.image.load("../pygame_intro/assets/sprites/seagrass.png").convert()

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
    # load game , designating ttf file and font size
    custom_font = pygame.font.Font("../pygame_intro/assets/fonts/Dried_Leaves.otf", size=128)
    text = custom_font.render("Chomp", True, (255, 29, 0))
    surf.blit(text, (screen_width/2-text.get_width()/2, screen_height/2-300))



#Main Loop
running = True
background = screen.copy()
draw_background(background)

#draw ze feesh

for i in range(10):
    x = random.randint(screen_width, screen_width*2)
    y = random.randint(100, screen_height - (2 * tile_size))
    fishes.add(Fish(x,y))

while running:
    for event in pygame.event.get():
        #print(event)
        if event.type ==pygame.QUIT:
            running=False

    screen.blit(background,(0,0))

    fishes.update()

    #check if fish have left the screen
    for fish in fishes: #loop through our feeshys
        if fish.rect.x < -fish.rect.width:
            fishes.remove(fish)
            fishes.add(Fish(random.randint(screen_width, screen_width +50), random.randint(tile_size, screen_height-tile_size)))

    fishes.draw(screen)

    #update disply
    pygame.display.flip()

    clock.tick(50)
pygame.quit()
