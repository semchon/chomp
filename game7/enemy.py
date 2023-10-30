#create a pygame sprite class for a fish
import os
import pygame
import random
from game_parameters import *


class Enemy(pygame.sprite.Sprite):

    def __init__(self, x,y):
        super().__init__()
        self.image = pygame.image.load("enemy.png").convert()
        self.image2 = pygame.image.load("enemy.png").convert()
        self.image.set_colorkey((255,255,255))
        self.image = pygame.transform.flip(self.image, flip_x = False, flip_y = False)
        # below shifts the center of the image to its actual center (rectangular parameters)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.speed = random.uniform(MIN_SPEED,MAX_SPEED)
        self.rect.center = (x,y)

    def update(self):
        #update the x position of the fish
        self.x -= self.speed
        self.rect.x = self.x


    def draw_fish(self, surf):
        surf.blit(self.image, self.rect)

enemies = pygame.sprite.Group()
#created group called fishes. As we make fish, we will add it to the group fishes