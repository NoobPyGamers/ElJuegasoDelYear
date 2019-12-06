

"""I am trying to allow resizing for this app, I put the RESIZABLE flag, but when I try to resize, it messes up! Try my code.

It is a grid program, when the window resizes I want the grid to also resize/shrink.
"""
import pygame,math
from pygame.locals import *
# Define some colors
black    = (   0,   0,   0)
white    = ( 255, 255, 255)
green    = (   0, 255,   0)
red      = ( 255,   0,   0)

# This sets the width and height of each grid location
width=1920
height=1080
size=[500,500]
# This sets the margin between each cell
margin=1


# Initialize pygame
pygame.init()

# Set the height and width of the screen

screen=pygame.display.set_mode(size,pygame.VIDEORESIZE)

# Set title of screen
pygame.display.set_caption("Now is our game!")

#Loop until the user clicks the close button.
done=False

# Used to manage how fast the screen updates
clock=pygame.time.Clock()
background_image = pygame.image.load("onepiisu.png")

#screen.fill(red)
# -------- Main Program Loop -----------
while done==False:
    screen=pygame.display.set_mode(size,pygame.VIDEORESIZE)
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.display.update()        
    #pygame.display.update()
    # Set the screen background
    screen.blit(background_image, [0, 0])

    # Draw the grid
    """for row in range(int(math.ceil(size[1]/height))+1):
        for column in range(int(math.ceil(size[0]/width))+1):
            color = white
            pygame.draw.rect(screen,color,[(margin+width)*column+margin,(margin+height)*row+margin,width,height])

    # Limit to 20 frames per second"""
    clock.tick(20)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit ()
