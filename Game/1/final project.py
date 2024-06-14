import pygame
import random
import time

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Typing Game")

# Load background image
background = pygame.image.load('background.jpg')
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

# bomb image
bomb = pygame.image.load('bomb.png')
bomb_size = bomb.get_rect().size
bomb_width = bomb_size[0]
bomb_height = bomb_size[1]

#bomb2 image
bomb2 = pygame.image.load('bomb2.png')
bomb2_size = bomb.get_rect().size
bomb2_width = bomb_size[0]
bomb2_height = bomb_size[1]

# Font
font = pygame.font.Font(None, 74)
player_font = pygame.font.Font(None, 30)
small_font = pygame.font.Font(None, 36)

# Word list
words = ["python", "java", "swift", "javascript", "typescript", "ruby", "go", "kotlin"]

# Game variables
current_word = random.choice(words)
player_score = 0
computer_score = 0
player_input_text = ""
computer_input_text = ""
game_over = False
timer_start = time.time()
TIMER_DURATION = 30  # seconds for the bomb timer
computer_level = 2  # Computer level (1: easy, 2: medium, 3: hard)
input_box = pygame.Rect(100, SCREEN_HEIGHT - 220, 140, 32)

def computer_typing_simulation():
    global computer_input_text, computer_score, current_word
    if computer_level == 1:
        typing_chance = 0.0002  # 2% chance per frame
    elif computer_level == 2:
        typing_chance = 0.0015  # 5% chance per frame
    elif computer_level == 3:
        typing_chance = 0.002  # 10% chance per frame
    else:
        typing_chance = 0.02  # default to easy level if unknown level

    if random.random() < typing_chance:
        computer_input_text = current_word
        computer_score += 1
        current_word = random.choice(words)
        computer_input_text = ""

# Main game loop
running = True
while running:
    #screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if player_input_text == current_word:
                    player_score += 1
                    current_word = random.choice(words)
                player_input_text = ""
            elif event.key == pygame.K_BACKSPACE:
                player_input_text = player_input_text[:-1]
            else:
                player_input_text += event.unicode
        if player_score > computer_score:
            bomb_x_pos = SCREEN_WIDTH/4* 3
            bomb_y_pos = SCREEN_HEIGHT - 350
        else:
            bomb_x_pos = SCREEN_WIDTH/7
            bomb_y_pos = SCREEN_HEIGHT - 350
    screen.blit(background,(0,0))
    screen.blit(bomb, (bomb_x_pos, bomb_y_pos))

    #pygame.display.update()
    
    # Simulate computer typing
    computer_typing_simulation()
    
    # Draw current word
    word_surface = font.render(current_word, True, BLACK)
    screen.blit(word_surface, (SCREEN_WIDTH//2 - word_surface.get_width()//2, 50))
    
    # Draw input texts
    player_input_surface = player_font.render(player_input_text, True, BLACK)
    screen.blit(player_input_surface, (input_box.x + 5, input_box.y + 7))
    
    computer_input_surface = font.render(computer_input_text, True, BLACK)
    screen.blit(computer_input_surface, (SCREEN_WIDTH - computer_input_surface.get_width() - 100, SCREEN_HEIGHT - 100))
    
    # Draw input box
    pygame.draw.rect(screen, BLACK, input_box, 2)
    
    # Draw scores
    player_score_surface = small_font.render(f"{player_score}", True, BLACK)
    screen.blit(player_score_surface, (100, 50))
    computer_score_surface = small_font.render(f"{computer_score}", True, BLACK)
    screen.blit(computer_score_surface, (SCREEN_WIDTH - 100, 50))
    
    # Timer and bomb logic
    elapsed_time = time.time() - timer_start
    remaining_time = TIMER_DURATION - elapsed_time
    timer_surface = small_font.render(f"{int(remaining_time)}", True, RED)
    screen.blit(timer_surface, (bomb_x_pos, bomb_y_pos))
    
    if remaining_time <= 0:
        game_over = True
        running = False
    
    pygame.display.flip()

# Game over screen

screen.blit(bomb2,(bomb_x_pos - 100, bomb_y_pos - 100))
game_over_surface = font.render("Game Over", True, RED)
screen.blit(game_over_surface, (SCREEN_WIDTH//2 - game_over_surface.get_width()//2, SCREEN_HEIGHT//2 - game_over_surface.get_height()//2))
pygame.display.flip()
pygame.time.wait(6000)

pygame.quit()
