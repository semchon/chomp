#create a pygame sprite class for a fish

import pygame
class Fish(pygame.sprite.Sprite):
    def __init__(self, x,y):
        super().__init__()
        self.image = pygame.image.load("fishes/fishTile_072.png").convert()
        self.image.set_colorkey((0,0,0))
        self.image = pygame.transform.flip(self.image, flip_x = True, flip_y = False)
        # below shifts the center of the image to its actual center (rectangular parameters)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (x,y)

    def draw_fish(self, surf):
        surf.blit(self.image, self.rect)

fishes = pygame.sprite.Group()
#created group called fishes. As we make fish, we will add it to the group fishes