import pygame

from GameFiles.constants import COLORS

class Button():
    def __init__(self, win, color, pos, size, text=None, font_size=0):
        self.win = win
        self.color = color
        self.pos = pos
        self.size = size
        self.text = text
        self.font_size = font_size

    def draw(self, win):
        self.win = win
        font = pygame.font.SysFont(None, self.font_size)
        text = font.render(self.text, True, COLORS['black'])
        text_rect = text.get_rect()

        coords = ((self.pos[1] + self.size[1] / 2), (self.pos[0] + self.size[0] / 2))

        text_rect.center = coords
        rect = pygame.Rect(0, 0, self.size[1], self.size[0])
        rect.center = coords
        pygame.draw.rect(self.win, self.color, rect)
        self.win.blit(text, text_rect)
