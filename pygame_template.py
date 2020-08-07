# Pygame template - skeleton for a new pygame project
'''
pygame template for my Atid Pluse students!
I took it from this amazing youtuber ,
the link is: https://github.com/kidscancode/pygame_tutorials/blob/master/pygame%20template.py

I did some changes so it can fit perfectly to my students and posted it on my github for a more comftrable access to all the material
'''
import pygame
import random

WIDTH = 360
HEIGHT = 480
FPS = 30

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
#intializing the clock
clock = pygame.time.Clock()
# adding an image as background
img_background = pygame.image.load(os.path.join(img_folder, 'the image name.jpg')).convert()
screen.blit(img_background, (0, 0)) # loading the image to coordinates (0,0)

# in order to update all the sprites we have in the game it is important to put them all in a list
all_sprites = pygame.sprite.Group()
# Game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()

    # Draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()