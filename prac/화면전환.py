import pygame
import sys

# 초기화
pygame.init()

# 화면 설정
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("타자 연습 프로그램")

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# 폰트 설정
font = pygame.font.Font(None, 36)

# 버튼 설정
button_rects = {
    "long_text_practice": pygame.Rect(300, 200, 200, 50),
    "word_practice": pygame.Rect(300, 300, 200, 50),
    "game_mode": pygame.Rect(300, 400, 200, 50),
}

# 화면 전환을 위한 상태 변수
current_screen = "main_menu"

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)

def main_menu():
    screen.fill(WHITE)
    draw_text('타자 연습 프로그램', font, BLACK, screen, 400, 100)
    
    for button_text, rect in button_rects.items():
        pygame.draw.rect(screen, GRAY, rect)
        draw_text(button_text.replace('_', ' ').title(), font, BLACK, screen, rect.centerx, rect.centery)
    
    pygame.display.update()

def long_text_practice():
    screen.fill(WHITE)
    draw_text('긴글 연습 화면', font, BLACK, screen, 400, 300)
    pygame.display.update()

def word_practice():
    screen.fill(WHITE)
    draw_text('단어 연습 화면', font, BLACK, screen, 400, 300)
    pygame.display.update()

def game_mode():
    screen.fill(WHITE)
    draw_text('게임 모드 화면', font, BLACK, screen, 400, 300)
    pygame.display.update()

# 메인 루프
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if current_screen == "main_menu":
                for screen_name, rect in button_rects.items():
                    if rect.collidepoint(event.pos):
                        current_screen = screen_name

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                current_screen = "main_menu"

    if current_screen == "main_menu":
        main_menu()
    elif current_screen == "long_text_practice":
        long_text_practice()
    elif current_screen == "word_practice":
        word_practice()
    elif current_screen == "game_mode":
        game_mode()
