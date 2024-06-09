import pygame
from Parent import *

class Setting(Screen):
    def draw(self):
        self.screen.fill(WHITE)
        draw_text('Start Setting', font, BLACK, self.screen, 400, 300)
        pygame.display.update()