from platform import win32_edition
import pygame

from GameFiles.board import Board
from GameFiles.rules import Rules
from GameFiles.menu import Menu
from GameFiles.constants import SQUARE_SIZE

class Game:
    def __init__(self, win):
        self.win = win
        self._init()
        self.state = 'menu'
        self.menu = Menu(self.win)
        self.score = { 
            'cpu': 0,
            'player': 0,
            'p1': 0,
            'p2': 0
        }

    def _init(self):
        self.selected = None
        self.turn = 0
        self.num_pin = 1
        self.board = Board()
    
    # display updates
    def update(self):
        if self.state == 'menu':
            self.menu.draw(self.win)
        elif self.state == 'pvc':
            self.board.draw(self.win)
        pygame.display.update()
    
    def game_loop(self):
        pos = pygame.mouse.get_pos()
        if self.state == 'menu':
            self.state = self.menu.button_click(pos)
        elif self.state == 'pvc':
            row, col = self.get_row_col_from_mouse(pos)
            if row == 0 and col == 9:
                self.state = 'menu'
                self.reset()
            self.choose_color(row, col)
        else:
            self.state = 'menu'

    # using mouse button, set empty pin to color
    def choose_color(self, row, col):
        pin = self.board.get_pin(row, col)
        if pin != 0:
            self.selected = pin
            self.board.move(pin, self.num_pin, self.turn)
            self.num_pin += 1
            if self.num_pin == 5:
                self.next_turn()
    
    def print_board(self):
        self.board.print_board()

    def next_turn(self):
        winner = self.board.give_feedback(self.turn)
        if winner:
            self.score['player'] += (10 - self.turn)
            self.board.game_end = "Codebreaker"
            print("Codebreaker wins")
        elif self.turn == 8:
            self.score['cpu'] += 10
            self.board.game_end = "Mastermind"
            print('Mastermind wins')
        else:
            self.turn += 1
            self.num_pin = 1
            self.board.available_colors_board()
    
    def get_row_col_from_mouse(self, pos):
        x, y = pos
        row = y // SQUARE_SIZE
        col = x // SQUARE_SIZE

        return row, col
    
    def reset(self):
        self._init()


    
