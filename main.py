import pygame, sys
from pygame.locals import *

WIDTH=800
HEIGHT=600

def main():
    screen=pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("Terrible juego amigo")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
    return 0

if __name__ == '__main__':
    pygame.init
    main()
    #hola mundo
