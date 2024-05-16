# character_only.py
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

class Character:
    def __init__(self):
        self.image = pygame.image.load(os.path.join(current_dir, 'character.png'))  # Load character image
        self.image = pygame.transform.scale(self.image, CHARACTER_SIZE)
        self.rect = self.image.get_rect()
        self.rect.x = 0  # Initial position
        self.rect.y = SCREEN_HEIGHT // 2 - CHARACTER_SIZE[1] // 2  # Center character vertically

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("DevLife - Character Only")
    clock = pygame.time.Clock()
    character = Character()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(DISPLAY_COLOR)

        # Draw character
        screen.blit(character.image, character.rect)

        pygame.display.flip()
        clock.tick(30)  # Limit frame rate to 30 FPS

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
