import pygame
from game_parameters import *
import random
from fish import Fish, fishes
from enemy import Enemy, enemies
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
    custom_font = pygame.font.Font("../pygame_intro/assets/fonts/Dried_Leaves.otf", size=100)
    custom_font_small = pygame.font.Font("../pygame_intro/assets/fonts/Dried_Leaves.otf", size=50)
    text = custom_font.render("Catch the fish", True, (255, 29, 0))
    text2 = custom_font_small.render("Use Arrows to move", True, (255, 29, 0))
    surf.blit(text, (screen_width/2-text.get_width()/2, screen_height/2-300))
    surf.blit(text2, (screen_width/2-text2.get_width()/2, screen_height/2-200))

def add_fish(num_fish):
    for i in range(num_fish):
        x = random.randint(screen_width, screen_width * 2)
        y = random.randint(100, screen_height - (2 * tile_size))
        fishes.add(Fish(x, y))

def add_enemy(num_enemies):
    for i in range(num_enemies):
        x = random.randint(screen_width, screen_width * 2)
        y = random.randint(100, screen_height - (2 * tile_size))
        enemies.add(Enemy(x, y))