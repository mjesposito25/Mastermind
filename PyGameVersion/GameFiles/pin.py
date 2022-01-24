import pygame
from GameFiles.constants import SQUARE_SIZE, COLORS

class Pin:
    PADDING = 15
    OUTLINE = 2

    def __init__(self, color, row, col):
        self.color = color
        self.row = row
        self.col = col

        self.x = 0
        self.y = 0
        self.calc_pos()

    
    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

    def draw(self, win):
        radius = SQUARE_SIZE // 2 - self.PADDING
        pygame.draw.circle(win, COLORS['black'], (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
    
    def __repr__(self):
        return str(self.color)
    
    #def __eq__(self, other): self.color == other.color