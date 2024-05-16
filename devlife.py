# character_and_desk.py
import pygame
import sys
import os

# Initialize Pygame
pygame.init()

# Get the current working directory
current_dir = os.path.dirname(__file__)

# Constants
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
DISPLAY_COLOR = (250, 202, 120)
CHARACTER_SIZE = (100, 100)  # Character size
DESK_SIZE = (70, 70)  # Desk size

class Character:
    def __init__(self):
        self.image = pygame.image.load(os.path.join(current_dir, 'character.png'))  # Load character image
        self.image = pygame.transform.scale(self.image, CHARACTER_SIZE)
        self.rect = self.image.get_rect()
        self.rect.x = 0  # Initial position on the first desk
        self.rect.y = SCREEN_HEIGHT // 3 - CHARACTER_SIZE[1] // 2  # Center character vertically

class Desk:
    def __init__(self, x, y):
        self.image = pygame.image.load(os.path.join(current_dir, 'desk.png'))  # Load desk image
        self.image = pygame.transform.scale(self.image, DESK_SIZE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("DevLife")
    clock = pygame.time.Clock()
    character = Character()
    desks = [Desk(200 + i * 200, SCREEN_HEIGHT // 3 - DESK_SIZE[1] // 2) for i in range(5)]  # Create limited desks

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(DISPLAY_COLOR)

        # Draw desks
        for desk in desks:
            screen.blit(desk.image, desk.rect)

        # Draw character
        screen.blit(character.image, character.rect)

        pygame.display.flip()
        clock.tick(30)  # Limit frame rate to 30 FPS

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
