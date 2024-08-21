from constants import *
import pygame

def main():
    playing = True
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while playing:
        # event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # display
        screen.fill("black")
        pygame.display.flip()

if __name__ == "__main__":
    main()
