import pygame
import sys
import random

from fish import Fish, fishes
from background import draw_background
from game_parameters import *
from player import Player

#initialize pygame
pygame.init()

#create screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Fish Game")

#clock
clock = pygame.time.Clock()


#Main loop
running = True
background = screen.copy()
draw_background(background)

#draw fish
for i in range(7):
    x = random.randint(screen_width, screen_width*2)
    y = random.randint(100, screen_height - (2 * tile_size))
    fishes.add(Fish(x,y))

#draw player fish
player = Player(screen_width/2, screen_height/2)


while running:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            running = False
            #controlling player fish vvv
        player.stop() #ensures it stops every time you release input
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print('You pressed W')
                player.move_up()
            if event.key == pygame.K_LEFT:
                player.move_left()
            if event.key == pygame.K_DOWN:
                player.move_down()
            if event.key == pygame.K_RIGHT:
                player.move_right()


    screen.blit(background,(0,0))

    #updating
    fishes.update()
    player.update()

   #check if fish have left the screen
    for fish in fishes: #loop through our feeshys
        if fish.rect.x < -fish.rect.width:
            fishes.remove(fish)
            fishes.add(Fish(random.randint(screen_width, screen_width +50), random.randint(tile_size, screen_height-tile_size)))

    #drawing the feesh
    fishes.draw(screen)
    player.draw(screen)

    #update display
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
