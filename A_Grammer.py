from Parent import *
import pygame
import sys
import os

class Grammer(Screen):
    def draw(self):
        self.screen.fill(WHITE)
        draw_text('Start grammer practice', font, BLACK, self.screen, 400, 300)
        pygame.display.update()




