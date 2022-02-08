import pygame

from GameFiles.constants import COLORS
from GameFiles.button import Button

class Menu:
    def __init__(self, win):
        self.win = win
        self.states = ['pvc', 'pvp', 'rules', 'settings', 'quit']
        self.buttonClass = Button(self.win, COLORS['white'], (500, 540), (300, 100), 'Quit', 100)
    
    def draw(self, win):
        win.fill(COLORS['ash'])
        self.button('PvCpu', 'white', (500, 60), win)
        self.button('PvP', 'white', (500, 180), win)
        self.button('Rules', 'white', (500, 300), win)
        self.button('Settings', 'white', (500, 420), win)
        #self.button('Quit', 'white', (500, 540), win)
        self.buttonClass.draw(win)


    def button(self, text, color, coords, win):
        font = pygame.font.SysFont(None, 100)
        text = font.render(text, True, COLORS['black'])
        text_rect = text.get_rect()
        text_rect.center = coords
        rect = pygame.Rect(0, 0, 300, 100)
        rect.center = coords
        pygame.draw.rect(win, COLORS[color], rect)
        win.blit(text, text_rect)

    def button_click(self, pos):
        for i in range(5):
            if 350 <= pos[0] <= 650 and (60 + i * 120) - 50 <= pos[1] <= (60 + i * 120) + 50:
                return self.states[i]
