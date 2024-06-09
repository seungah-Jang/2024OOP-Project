import pygame
import random
import sys

# 초기화
pygame.init()

# 화면 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("타자 연습 게임")

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# 글꼴 설정
font = pygame.font.Font(None, 36)
large_font = pygame.font.Font(None, 74)

# 단어 리스트
easy_words = ["cat", "dog", "apple", "banana", "grape"]
medium_words = ["cherry", "orange", "strawberry", "mango"]
hard_words = ["watermelon", "pineapple", "blueberry", "pomegranate"]

# 단어 클래스 정의
class Word:
    def __init__(self, text):
        self.text = text
        self.x = random.randint(50, screen_width - 100)
        self.y = -50
        self.speed = random.randint(1, 3)
    
    def draw(self, screen):
        word_surface = font.render(self.text, True, BLACK)
        screen.blit(word_surface, (self.x, self.y))
    
    def update(self):
        self.y += self.speed

# 게임 변수 설정
falling_words = []
current_word = ''
score = 0
lives = 5
time_limit = 60  # 게임 시간 제한 (초)
start_ticks = pygame.time.get_ticks()  # 시작 시간
user_accuracy = 1.0  # 사용자 정확도
difficulty_level = 'easy'  # 초기 난이도

# 단어 추가 함수
def add_word():
    global difficulty_level
    if difficulty_level == 'easy':
        new_word = Word(random.choice(easy_words))
    elif difficulty_level == 'medium':
        new_word = Word(random.choice(medium_words))
    else:
        new_word = Word(random.choice(hard_words))
    falling_words.append(new_word)

# 손가락 강조 함수
def draw_fingers(screen, highlighted_finger=None):
    pass  # 손가락 가이드 기능 추가 시 구현

# 게임 루프
running = True
while running:
    screen.fill(WHITE)
    time_passed = (pygame.time.get_ticks() - start_ticks) / 1000  # 경과 시간

    highlighted_finger = None

    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_RETURN:
                if current_word != '':
                    for word in falling_words:
                        if word.text == current_word:
                            falling_words.remove(word)
                            score += 1
                            break
                    current_word = ''
            elif event.key == pygame.K_BACKSPACE:
                current_word = current_word[:-1]
            else:
                current_word += event.unicode
                # 손가락 강조 기능 추가 시 highlighted_finger 설정

    # 단어 떨어뜨리기
    if random.randint(1, 50) == 1:
        add_word()

    # 단어 업데이트 및 충돌 처리
    for word in falling_words:
        word.update()
        if word.y > screen_height:
            falling_words.remove(word)
            lives -= 1
        word.draw(screen)

    # 사용자 정확도에 따른 난이도 조절
    if len(falling_words) > 0:
        total_characters = sum(len(word.text) for word in falling_words)
        correct_characters = total_characters - sum(word.y > screen_height for word in falling_words)
        user_accuracy = correct_characters / total_characters if total_characters > 0 else 1.0
        if user_accuracy > 0.9:
            difficulty_level = 'hard'
        elif user_accuracy > 0.7:
            difficulty_level = 'medium'
        else:
            difficulty_level = 'easy'

    # 시간 제한 확인
    if time_passed >= time_limit or lives <= 0:
        running = False

    # 텍스트 렌더링
    input_surface = font.render(current_word, True, RED)
    score_surface = font.render(f"Score: {score}", True, BLACK)
    lives_surface = font.render(f"Lives: {lives}", True, BLACK)
    time_surface = font.render(f"Time: {int(time_limit - time_passed)}", True, BLACK)

    # 텍스트 화면에 표시
    screen.blit(input_surface, (10, screen_height - 50))
    screen.blit(score_surface, (10, 10))
    screen.blit(lives_surface, (10, 50))
    screen.blit(time_surface, (screen_width - 150, 10))

    pygame.display.flip()

    # 초당 60프레임으로 설정
    pygame.time.Clock().tick(60)

# 게임 종료 후 게임 오버 화면
screen.fill(WHITE)
game_over_surface = large_font.render("Game Over", True, BLACK)
final_score_surface = font.render(f"Final Score: {score}", True, BLACK)
screen.blit(game_over_surface, (screen_width // 2 - game_over_surface.get_width() // 2, screen_height // 2 - 50))
screen.blit(final_score_surface, (screen_width // 2 - final_score_surface.get_width() // 2, screen_height // 2 + 50))
pygame.display.flip()
pygame.time.wait(3000)

pygame.quit()
sys.exit()
