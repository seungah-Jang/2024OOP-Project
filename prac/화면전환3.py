import pygame
import sys

# Pygame 초기화
pygame.init()

# 화면 설정
screen = pygame.display.set_mode((800, 900))
pygame.display.set_caption("타자 연습 프로그램")

# 폰트 설정
font = pygame.font.Font(None, 36)

class Screen:
    def __init__(self, screen):
        self.screen = screen
    
    def draw(self):
        pass

    def handle_event(self, event):
        pass

class GrammerScreen(Screen):
    def draw(self):
        self.screen.fill((255, 255, 255))
        text = font.render("Grammer Practice", True, (0, 0, 0))
        self.screen.blit(text, (100, 100))

class ProgramScreen(Screen):
    def draw(self):
        self.screen.fill((255, 255, 255))
        text = font.render("Program Practice", True, (0, 0, 0))
        self.screen.blit(text, (100, 100))

class GameScreen(Screen):
    def draw(self):
        self.screen.fill((255, 255, 255))
        text = font.render("Game", True, (0, 0, 0))
        self.screen.blit(text, (100, 100))

class AnalysisScreen(Screen):
    def draw(self):
        self.screen.fill((255, 255, 255))
        text = font.render("Analysis", True, (0, 0, 0))
        self.screen.blit(text, (100, 100))

class SettingScreen(Screen):
    def draw(self):
        self.screen.fill((255, 255, 255))
        text = font.render("Setting", True, (0, 0, 0))
        self.screen.blit(text, (100, 100))

class ExitScreen(Screen):
    def draw(self):
        self.screen.fill((255, 255, 255))
        text = font.render("Exit", True, (0, 0, 0))
        self.screen.blit(text, (100, 100))

class MainScreen:
    def __init__(self):
        self.current_screen = None
        self.menu_options = [
            "Grammer Practice",
            "Program Practice",
            "Game",
            "Analysis",
            "Setting",
            "Exit"
        ]
        self.screens = {
            "Grammer Practice": GrammerScreen(screen),
            "Program Practice": ProgramScreen(screen),
            "Game": GameScreen(screen),
            "Analysis": AnalysisScreen(screen),
            "Setting": SettingScreen(screen),
            "Exit": ExitScreen(screen)
        }
        self.run()
        
    def run(self):
        global screen
        clock = pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        self.current_screen = self.screens["Grammer Practice"]
                    elif event.key == pygame.K_2:
                        self.current_screen = self.screens["Program Practice"]
                    elif event.key == pygame.K_3:
                        self.current_screen = self.screens["Game"]
                    elif event.key == pygame.K_4:
                        self.current_screen = self.screens["Analysis"]
                    elif event.key == pygame.K_5:
                        self.current_screen = self.screens["Setting"]
                    elif event.key == pygame.K_6:
                        pygame.quit()
                        sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    self.check_mouse_click(mouse_pos)

            if self.current_screen:
                self.current_screen.draw()
            else:
                self.draw_main_menu()
                
            pygame.display.flip()
            clock.tick(60)

    def draw_main_menu(self):
        screen.fill((255, 255, 255))
        y = 100
        self.menu_rects = []
        for i, option in enumerate(self.menu_options, 1):
            text = font.render(f"{i}. {option}", True, (0, 0, 0))
            rect = text.get_rect(topleft=(100, y))
            screen.blit(text, rect.topleft)
            self.menu_rects.append((rect, option))
            y += 50

    def check_mouse_click(self, pos):
        for rect, option in self.menu_rects:
            if rect.collidepoint(pos):
                if option == "Exit":
                    pygame.quit()
                    sys.exit()
                else:
                    self.current_screen = self.screens[option]

if __name__ == "__main__":
    main_screen = MainScreen()
