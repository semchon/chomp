import pygame
import sys
import random

from fish import Fish, fishes
from background import draw_background, add_fish, add_enemy
from game_parameters import *
from player import Player
from enemy import Enemy, enemies
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

#draw fish/enemies
add_fish(6)
add_enemy(2)

#draw player fish
player = Player(screen_width/2, screen_height/2)

score = 0
score_font = pygame.font.Font("../pygame_intro/assets/fonts/Dried_Leaves.otf", size=50)

#load bg music
pygame.mixer.music.load("sounds/backgroundmusic.wav")
pygame.mixer.music.play(loops = 100)

#load sound effect
chomp = pygame.mixer.Sound("sounds/chomp.wav")
bad = pygame.mixer.Sound("sounds/bad.wav")
hurt = pygame.mixer.Sound("sounds/hurt.wav")
bubbles = pygame.mixer.Sound("sounds/bubbles.wav")

#add life counter and game over
life_icon = pygame.image.load("life.png").convert()
life_icon.set_colorkey((255,255,255))
lives = 3

while lives>0:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
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
    enemies.update()
    #update score on screen
    text = score_font.render(f"Score: {score}", True, (255, 29, 0))
    screen.blit(text, (text.get_width()/10, screen_height / 2 - 300))

    #lives
    for i in range(lives):
        screen.blit(life_icon, (i*tile_size, screen_height-tile_size))

   #check if fish have left the screen
    for fish in fishes: #loop through our feeshys
        if fish.rect.x < -fish.rect.width:
            fishes.remove(fish)
            fishes.add(Fish(random.randint(screen_width, screen_width +50), random.randint(tile_size, screen_height-tile_size)))
            enemies.add(Enemy(random.randint(screen_width, screen_width + 50), random.randint(tile_size, screen_height - tile_size)))
            enemies.add(Enemy(random.randint(screen_width, screen_width + 50), random.randint(tile_size, screen_height - tile_size)))
    for enemy in enemies:
        if enemy.rect.x < -enemy.rect.width:
            enemies.remove(enemy)

    #drawing the feesh
    fishes.draw(screen)
    enemies.draw(screen)
    player.draw(screen)

    #checking for collisions between player & fishy - use the built in pygame group collision method
    result = pygame.sprite.spritecollide(player, fishes, True)
    if len(result) > 0:
        score += len(result)
        for i in range(len(result)):
            pygame.mixer.Sound.play(chomp)
            add_fish(1)

    enemy_result = pygame.sprite.spritecollide(player, enemies, True)
    if len(enemy_result)>0:
        for i in range(len(enemy_result)):
            pygame.mixer.Sound.play(hurt)
            lives -= len(enemy_result)
            add_enemy(len(enemy_result))

    #game loss condition
    #update display
    pygame.display.flip()

    clock.tick(60)

highscore = -1
with open('highscore.txt','r') as score_file:
    e = score_file.readlines()
    highscore = int(e[0])
    print(highscore)
    if score > highscore:
        with open('highscore.txt','w') as sco_file:
            sco_file.write(f"{score}")
            highscore = score

screen.blit(background, (0,0))
h_score = score_font.render(f"High Score: {highscore}", True, (255, 0, 0))
screen.blit(h_score, (screen_width / 2 - h_score.get_width() / 2, screen_height / 2 + 100))
pygame.display.flip()
message = score_font.render("GAME OVER", True, (255,0,0))
screen.blit(message, (screen_width/2 - message.get_width()/2, screen_height/2-100))

#show score
score_text = score_font.render(f"Score: {score}", True, (255,0,0))
screen.blit(score_text, (screen_width/2 - message.get_width()/2, screen_height/2-score_text.get_height()))
pygame.display.flip()
pygame.mixer.Sound.play(bubbles)



#What does user wanna do next?
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #quit pygame
            pygame.quit()
            sys.exit()
