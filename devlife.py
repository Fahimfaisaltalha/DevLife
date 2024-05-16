# game_window.py
import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
DISPLAY_COLOR = (250, 202, 120)

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("DevLife")
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(DISPLAY_COLOR)

        pygame.display.flip()
        clock.tick(30)  # Limit frame rate to 30 FPS

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
