import pygame
# 초기화
pygame.init()

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

#폰트
font = pygame.font.Font(None, 36)


class Screen:
    def __init__(self, screen):
        self.screen = screen
        print("ss")
    
    def draw(self):
        pass

    def handle_event(self, event):
        pass

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)