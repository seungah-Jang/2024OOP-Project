import pygame
from Parent import *


class Analysis(Screen):
    def draw(self):
        self.screen.fill(WHITE)
        draw_text('Start Analysis', font, BLACK, self.screen, 400, 300)
        pygame.display.update()