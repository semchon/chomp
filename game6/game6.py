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
for i in range(15):
    x = random.randint(screen_width, screen_width*2)
    y = random.randint(100, screen_height - (2 * tile_size))
    fishes.add(Fish(x,y))

#draw player fish
player = Player(screen_width/2, screen_height/2)

score = 0
score_font = pygame.font.Font("../pygame_intro/assets/fonts/Dried_Leaves.otf", size=50)

#load bg music
pygame.mixer.music.load("sounds/backgroundmusic.wav")
pygame.mixer.music.play(loops = 100)

#load sound effect
chomp = pygame.mixer.Sound("sounds/chomp.wav")


while running:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            running = False
            #controlling player fish vvv

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player.move_up()
            if event.key == pygame.K_a:
                player.move_left()
            if event.key == pygame.K_s:
                player.move_down()
            if event.key == pygame.K_d:
                player.move_right()
        if event.type == pygame.KEYUP:
            player.stop()


    screen.blit(background,(0,0))

    #updating
    fishes.update()
    player.update()

    #update score on screen
    text = score_font.render(f"Score: {score}", True, (255, 29, 0))
    screen.blit(text, (text.get_width()/10, screen_height / 2 - 300))

   #check if fish have left the screen
    for fish in fishes: #loop through our feeshys
        if fish.rect.x < -fish.rect.width:
            fishes.remove(fish)
            fishes.add(Fish(random.randint(screen_width, screen_width +50), random.randint(tile_size, screen_height-tile_size)))

    #drawing the feesh
    fishes.draw(screen)
    player.draw(screen)

    #checking for collisions between player & fishy - use the built in pygame group collision method
    result = pygame.sprite.spritecollide(player, fishes, True)
    if len(result) > 0:
        score += len(result)
        for i in range(len(result)):
            pygame.mixer.Sound.play(chomp)
            fishes.add(Fish(random.randint(screen_width, screen_width + 50), random.randint(tile_size, screen_height - tile_size)))

    #game loss condition
    #update display
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
