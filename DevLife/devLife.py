import pygame
import sys
import os

# Initialize the Pygame
pygame.init()

# For getting current working directory
current_dir = os.path.dirname(__file__)


SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
DISPLAY_COLOR = (250, 202, 120)
CHARACTER_SIZE = (200, 200)  
DESK_SIZE = (150, 150)  
FONT_SIZE = 30

class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

class Character:
    def __init__(self):
        self.image = pygame.image.load(os.path.join(current_dir, 'character.png'))  # Load character image
        self.image = pygame.transform.scale(self.image, CHARACTER_SIZE)
        self.rect = self.image.get_rect()
        self.rect.x = 0  # position of the first desk
        self.rect.y = SCREEN_HEIGHT // 2 - CHARACTER_SIZE[1] // 2  # Center character vertically
        self.start_position = self.rect.topleft  

    def move_to_next_desk(self):
        
        self.rect.x += 200
        # If character exits the desk area charecter will  move it back to the starting position
        if self.rect.right > SCREEN_WIDTH:
            self.rect.topleft = self.start_position

class Desk:
    def __init__(self, x, y):
        self.image = pygame.image.load(os.path.join(current_dir, 'desk.png'))  # Load desk image
        self.image = pygame.transform.scale(self.image, DESK_SIZE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class DevLifeGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("DevLife")
        self.clock = pygame.time.Clock()
        self.character = Character()
        self.desks = [Desk(200 + i * 200, SCREEN_HEIGHT // 2 - DESK_SIZE[1] // 2) for i in range(5)]  
        self.questions = self.generate_questions()
        self.current_question_index = 0
        self.user_input = ""
        self.cash_bar_width = 0
        self.frustration_bar_width = 0

        # Load background image
        self.background_image = pygame.image.load(os.path.join(current_dir, 'background.webp'))
        self.background_image = pygame.transform.scale(self.background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

    def generate_questions(self):
        
        questions = [
            Question("Who is the best Programmer","Me"),
            Question("Which programming language doesn't have pointers?", "Java"),
            Question("Which programming language uses pointers extensively?", "C"),
            Question("Which programming language uses reference instead of pointers?", "Python"),
            Question("Which programming language is known for its safety features and lack of manual memory management?", "Rust"),
            Question("Which programming language has both pointers and references?", "C++"),
            Question('Which is the first Programming language',"Assembaly Language")
            
        ]
        return questions

    def display_text(self, text, x, y, color=(0, 0, 0)):
        font = pygame.font.Font(None, FONT_SIZE)
        text_surface = font.render(text, True, color)
        self.screen.blit(text_surface, (x, y))

    def run(self):
        running = True
        desk_index = 0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        self.user_input = self.user_input[:-1]
                    elif event.key == pygame.K_RETURN:
                        # Check if the answer is correct
                        current_question = self.questions[self.current_question_index]
                        if self.user_input.lower() == current_question.answer.lower():
                            self.character.move_to_next_desk()  # Move character to the next desk
                            self.cash_bar_width += 30  # Increase cash bar
                            if self.cash_bar_width > 200:
                                self.cash_bar_width = 200
                            self.display_text("Correct! +$100", 50, 200, (0, 128, 0))
                        else:
                            self.character.move_to_next_desk()  # Move character to the next desk
                            self.frustration_bar_width += 30  # Increase frustration bar
                            if self.frustration_bar_width > 200:
                                self.frustration_bar_width = 200
                            self.display_text("Wrong! Frustration +1", 50, 200, (255, 0, 0))
                        # Move to the next question
                        self.current_question_index += 1
                        if self.current_question_index >= len(self.questions):
                            None
                        else:
                            self.user_input = ""
                    else:
                        self.user_input += event.unicode

            # Blit background image
            self.screen.blit(self.background_image, (0, 0))

            # Draw desks
            for desk in self.desks:
                self.screen.blit(desk.image, desk.rect)

            # Draw character
            self.screen.blit(self.character.image, self.character.rect)

            # Draw cash bar
            pygame.draw.rect(self.screen, (0, 128, 0), [50, 500, 200, 30])
            pygame.draw.rect(self.screen, (0, 255, 0), [50, 500, self.cash_bar_width, 30])

            # Draw frustration bar
            pygame.draw.rect(self.screen, (255, 0, 0), [50, 550, 200, 30])
            pygame.draw.rect(self.screen, (255, 128, 0), [50, 550, self.frustration_bar_width, 30])

            # Display current question
            if self.current_question_index < len(self.questions):
                current_question = self.questions[self.current_question_index]
                self.display_text("Question:", 50, 50)
                self.display_text(current_question.text, 50, 100)
            else:
                self.display_text("No more questions! Game over.", 50, 100)

            # Player stats
            self.display_text("Cash Bar:", 50, 480)
            self.display_text("Frustration Bar:", 50, 530)
            self.display_text("Your Answer:", 50, 450)
            self.display_text(self.user_input, 200, 450)

            pygame.display.flip()
            self.clock.tick(30)  

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = DevLifeGame()
    game.run()
