#a pygame sprite class for a player fish

import pygame

from game_parameters import *

class Player(pygame.sprite.Sprite):
    def __init__(self,x,  y):
        #TURN FISH IN OPP DIRECTION
        super().__init__()
        self.image = pygame.image.load("player.png").convert()
        self.forward_image = pygame.image.load("player.png").convert()
        self.reverse_image = pygame.transform.flip(self.image, flip_x=True, flip_y=False)
        self.image.set_colorkey((255, 255, 255))
        self.forward_image.set_colorkey((255, 255, 255))
        self.reverse_image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.x = x
        self.y = y
        self.x_speed = 0
        self.y_speed = 0


    def move_up(self):
        self.y_speed = -1 * PLAYER_SPEED
        print('you moved up')
        print(self.y_speed)

    def move_down(self):
        self.y_speed = PLAYER_SPEED

    def move_left(self):
        self.x_speed = -1 * PLAYER_SPEED
        self.image = self.reverse_image
    def move_right(self):
        self.x_speed = PLAYER_SPEED
        self.image = self.forward_image
    def stop(self):
        self.x_speed = 0
        self.y_speed = 0

    def update(self):
        self.x += self.x_speed
        self.y += self.y_speed
        if self.x > screen_width:
            self.x = screen_width
        if self.x < 0:
            self.x = 0
        if self.y < 0:
            self.y = 0
        if self.y > screen_height:
            self.y = screen_height
        self.rect.x = self.x
        self.rect.y = self.y



    def draw(self,surf):
        surf.blit(self.image, self.rect)
