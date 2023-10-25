#create a pygame sprite class for a fish
import os
import pygame
import random
MIN_SPEED = 2
MAX_SPEED = 5


class Fish(pygame.sprite.Sprite):

    def __init__(self, x,y):
        super().__init__()
        random_fish = random.choice(os.listdir("fishes"))
        self.image = pygame.image.load(f"fishes/{random_fish}").convert()
        self.image.set_colorkey((0,0,0))
        self.image = pygame.transform.flip(self.image, flip_x = True, flip_y = False)
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

fishes = pygame.sprite.Group()
#created group called fishes. As we make fish, we will add it to the group fishes