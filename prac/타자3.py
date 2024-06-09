import pygame
import sys

# 색깔 상수
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREY = (150, 150, 150)

# Pygame 초기화
pygame.init()

# 화면 크기 설정
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Typing Practice")

# 폰트 설정
font = pygame.font.SysFont(None, 30)

# 주어진 텍스트
given_text = "This is a typing practice. Type this text."

# 사용자가 입력한 텍스트
typed_text = ""

# 타이머 설정
start_time = None

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if start_time is None:
                start_time = pygame.time.get_ticks()
            typed_text += event.unicode

    # 입력한 텍스트와 주어진 텍스트를 줄 단위로 비교하며 렌더링
    input_len = len(typed_text)
    correct_text = typed_text
    remaining_text = given_text[input_len:]

    correct_lines = correct_text.split('\n')
    remaining_lines = remaining_text.split('\n')

    y_offset = 50  # 초기 y 위치
    line_height = font.get_linesize() + 10  # 각 줄 사이의 간격

    # 화면 지우기
    screen.fill((255, 255, 255))

    # 주어진 텍스트 렌더링
    for i, (correct_line, remaining_line) in enumerate(zip(correct_lines, remaining_lines)):
        # 입력한 텍스트와 비교하며 렌더링
        for index, char in enumerate(correct_line):
            color = BLACK
            if index >= len(typed_text) or char != typed_text[index]:
                color = RED
            text_surface = font.render(char, True, color)
            screen.blit(text_surface, (50 + index * 12, y_offset + i * line_height))

    # 남은 줄을 렌더링
    for j in range(i + 1, len(remaining_lines)):
        for index, char in enumerate(remaining_lines[j]):
            text_surface = font.render(char, True, GREY)
            screen.blit(text_surface, (50 + index * 12, y_offset + (j * line_height)))

    pygame.display.flip()

# Pygame 종료
pygame.quit()
sys.exit()
