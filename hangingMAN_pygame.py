
'''
# 0
print("_________")
print("|       |")
print("|")
print("|")
print("|")
print("|")
print("|")
#1
print("_________")
print("|       |")
print("|       0")
print("|           ")
print("|")
print("|")
print("|")
#2
print("_________")
print("|       |")
print("|       0")
print("|       |   ")
print("|")
print("|")
print("|")
#3
print("_________")
print("|       |")
print("|       0")
print("|       | \ ")
print("|")
print("|")
print("|")
#4
print("_________")
print("|       |")
print("|       0")
print("|     / | \ ")
print("|")
print("|")
print("|")
#5
print("_________")
print("|       |")
print("|       0")
print("|     / | \ ")
print("|        \ ")
print("|")
print("|")
#6 game over!!
print("_________")
print("|       |")
print("|       0")
print("|     / | \ ")
print("|      / \ ")
print("|")
print("|")

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
myfont = pygame.font.SysFont("monospace", 16)

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hanging Man Game")
#intializing the clock
clock = pygame.time.Clock()
# adding an image as background
#img_background = pygame.image.load(os.path.join(img_folder, 'the image name.jpg')).convert()
#screen.blit(img_background, (0, 0)) # loading the image to coordinates (0,0)

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
    hangingManDraw_0 = myfont.render("_________\n|       |\n|\n|\n|\n|\n|\n", 1, (0, 0, 0))
    screen.blit(hangingManDraw_0, (5, 10))
    # life score bord
   # lifetext = myfont.render("life {0}".format(life_score), 1, (0, 0, 0))
    #creen.blit(lifetext, (5, 30))
    pygame.display.flip()

pygame.quit()