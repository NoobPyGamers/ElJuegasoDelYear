import pygame, sys
from pygame.locals import * 

pygame.init()

WIDTH=800
HEIGHT=600

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Test")

red = (255,0,0)
black = (0,0,0)
screen.fill(black)

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            screen.fill(red)
        if event.type == pygame.MOUSEBUTTONUP:
            screen.fill(black)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.display.update()
