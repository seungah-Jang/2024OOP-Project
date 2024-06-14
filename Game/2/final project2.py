import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 600
ROWS, COLS = 6, 6
CIRCLE_RADIUS = 40
GRID_OFFSET = 100  # Offset for the grid to prevent overlap with text

# Colors
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Font
FONT = pygame.font.Font(None, 36)

# Words list
words = ["python", "java", "ruby", "javascript", "swift", "kotlin"]

# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bomb Tracking Game")

# Player starting position
player_pos = [ROWS - 1, COLS - 1]

# Bomb position
bomb_pos = [random.randint(0, ROWS - 1), random.randint(0, COLS - 1)]

# Defused bomb counter
defused_bomb_count = 0

# Timer
start_time = time.time()
time_limit = 60  # 60 seconds time limit

# Function to draw grid
def draw_grid():
    for row in range(ROWS):
        for col in range(COLS):
            pygame.draw.circle(screen, BLUE, (col * WIDTH // COLS + WIDTH // (COLS * 2), row * (HEIGHT - GRID_OFFSET) // ROWS + (HEIGHT - GRID_OFFSET) // (ROWS * 2) + GRID_OFFSET), CIRCLE_RADIUS)
    pygame.draw.circle(screen, RED, (bomb_pos[1] * WIDTH // COLS + WIDTH // (COLS * 2), bomb_pos[0] * (HEIGHT - GRID_OFFSET) // ROWS + (HEIGHT - GRID_OFFSET) // (ROWS * 2) + GRID_OFFSET), CIRCLE_RADIUS)

# Function to draw player
def draw_player():
    pygame.draw.circle(screen, BLACK, (player_pos[1] * WIDTH // COLS + WIDTH // (COLS * 2), player_pos[0] * (HEIGHT - GRID_OFFSET) // ROWS + (HEIGHT - GRID_OFFSET) // (ROWS * 2) + GRID_OFFSET), CIRCLE_RADIUS)

# Main game loop
def main():
    global bomb_pos, defused_bomb_count
    run = True
    word = random.choice(words)
    typed_word = ""
    move_allowed = False

    while run:
        screen.fill(WHITE)
        draw_grid()
        draw_player()
        
        # Display word
        word_surface = FONT.render(word, True, BLACK)
        screen.blit(word_surface, (WIDTH // 2 - word_surface.get_width() // 2, 10))
        
        # Display typed word
        typed_surface = FONT.render(typed_word, True, BLACK)
        screen.blit(typed_surface, (WIDTH // 2 - typed_surface.get_width() // 2, 50))

        # Display timer
        elapsed_time = time.time() - start_time
        remaining_time = max(0, time_limit - elapsed_time)
        timer_surface = FONT.render(f"Time: {int(remaining_time)}", True, BLACK)
        screen.blit(timer_surface, (10, 10))

        # Display defused bomb count
        bomb_count_surface = FONT.render(f"Defused: {defused_bomb_count}", True, BLACK)
        screen.blit(bomb_count_surface, (WIDTH - 150, 10))
        
        # Check for time out
        if remaining_time == 0:
            run = False
            print("Time's up! You failed to defuse the bomb.")
            break
        
        # Check for player reaching bomb
        if player_pos == bomb_pos:
            defused_bomb_count += 1
            bomb_pos = [random.randint(0, ROWS - 1), random.randint(0, COLS - 1)]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if move_allowed:
                    if event.key == pygame.K_UP and player_pos[0] > 0:
                        player_pos[0] -= 1
                        move_allowed = False
                    elif event.key == pygame.K_DOWN and player_pos[0] < ROWS - 1:
                        player_pos[0] += 1
                        move_allowed = False
                    elif event.key == pygame.K_LEFT and player_pos[1] > 0:
                        player_pos[1] -= 1
                        move_allowed = False
                    elif event.key == pygame.K_RIGHT and player_pos[1] < COLS - 1:
                        player_pos[1] += 1
                        move_allowed = False
                else:
                    if event.key == pygame.K_BACKSPACE:
                        typed_word = typed_word[:-1]
                    elif event.key == pygame.K_RETURN:
                        if typed_word == word:
                            move_allowed = True
                            word = random.choice(words)
                            typed_word = ""
                    else:
                        typed_word += event.unicode
        
        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()
