import pygame
import sys

#now we need to initialize pygame
pygame.init()

#screen dimensions
screen_width = 800
screen_height = 600

#colors for screen
BLUE = (0, 0, 225)
BROWN = (255, 235, 153)

#create the screen. passed in as a tuple
screen = pygame.display.set_mode(size=(screen_width, screen_height))
pygame.display.set_caption("Beach scene")

#The main loop
running = True #set flag to true
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #now fill the screen with blue
    screen.fill(BLUE)

    #adding sandy bottom
    rectangle_height = 100
    pygame.draw.rect(screen, BROWN, (0, screen_height-rectangle_height, screen_width, rectangle_height))

    #update display
    pygame.display.flip()           #by default pygame draws on the "back" of the surface
pygame.quit