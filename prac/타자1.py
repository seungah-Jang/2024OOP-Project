import pygame
import sys
import time
import os

# 초기화
pygame.init()

# 화면 설정
screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("타자 연습 프로그램")

# 색상 설정
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# 글꼴 설정
font = pygame.font.Font(None, 20)

# 폰트 설정
font_path = os.path.join(os.path.dirname(__file__), "NANUMGOTHIC.TTF")
font = pygame.font.Font(font_path, 20)

# 테스트 문장
sentence = "import pygame sys time\n aksgh"
typed_text = ""
start_time = None
wpm = 0

# 메인 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_BACKSPACE:
                typed_text = typed_text[:-1]
            elif event.key == pygame.K_RETURN:
                end_time = time.time()
                time_taken = end_time - start_time
                wpm = (len(typed_text) / 5) / (time_taken / 60)
                typed_text = ""
                start_time = None
            else:
                if start_time is None:
                    start_time = time.time()
                typed_text += event.unicode

    # 화면 그리기
    screen.fill(WHITE)
    text_surface = font.render(sentence, True, BLACK)
    screen.blit(text_surface, (50, 100))
    typed_surface = font.render(typed_text, True, BLACK)
    screen.blit(typed_surface, (50, 200))
    if wpm:
        wpm_surface = font.render(f"WPM: {wpm:.2f}", True, BLACK)
        screen.blit(wpm_surface, (50, 300))

    pygame.display.flip()

# 종료
pygame.quit()
sys.exit()
