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

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)

class Screen:
    def __init__(self, screen):
        self.screen = screen
    
    def draw(self):
        pass

    def handle_event(self, event):
        pass

class MainMenu(Screen):
    def __init__(self, screen):
        super().__init__(screen)
        self.button_rects = {
            "long_text_practice": pygame.Rect(300, 200, 200, 50),
            "word_practice": pygame.Rect(300, 300, 200, 50),
            "game_mode": pygame.Rect(300, 400, 200, 50),
        }

    def draw(self):
        self.screen.fill(WHITE)
        draw_text('타자 연습 프로그램', font, BLACK, self.screen, 400, 100)
        
        for button_text, rect in self.button_rects.items():
            pygame.draw.rect(self.screen, GRAY, rect)
            draw_text(button_text.replace('_', ' ').title(), font, BLACK, self.screen, rect.centerx, rect.centery)
        
        pygame.display.update()

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for screen_name, rect in self.button_rects.items():
                if rect.collidepoint(event.pos):
                    return screen_name
        return None

class LongTextPractice(Screen):
    def draw(self):
        self.screen.fill(WHITE)
        draw_text('long text', font, BLACK, self.screen, 400, 300)
        pygame.display.update()

class WordPractice(Screen):
    def draw(self):
        self.screen.fill(WHITE)
        draw_text('word practice', font, BLACK, self.screen, 400, 300)
        pygame.display.update()

class GameMode(Screen):
    def draw(self):
        self.screen.fill(WHITE)
        draw_text('game', font, BLACK, self.screen, 400, 300)
        pygame.display.update()

# 메인 프로그램
class TypingPracticeProgram:
    def __init__(self):
        self.screen = screen
        self.current_screen = MainMenu(self.screen)
        self.screens = {
            "main_menu": MainMenu(self.screen),
            "long_text_practice": LongTextPractice(self.screen),
            "word_practice": WordPractice(self.screen),
            "game_mode": GameMode(self.screen),
        }

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.current_screen = self.screens["main_menu"]

                screen_name = self.current_screen.handle_event(event)
                if screen_name:
                    self.current_screen = self.screens[screen_name]

            self.current_screen.draw()

if __name__ == "__main__":
    app = TypingPracticeProgram()
    app.run()
