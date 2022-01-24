from platform import win32_edition
import pygame

from GameFiles.board import Board
from GameFiles.rules import Rules
from GameFiles.constants import SQUARE_SIZE

class Game:
    def __init__(self, win):
        self.win = win
        self._init()
        self.state = 'game'

    def _init(self):
        self.selected = None
        self.turn = 0
        self.num_pin = 1
        self.board = Board()
        # self.rules = Rules()
    
    # display updates
    def update(self):
        if self.state == 'game':
            self.board.draw(self.win)
        pygame.display.update()

    def winner(self):
        pass

    def main_menu(self):
        pass

    def options_menu(self):
        pass
    
    def game_loop(self):
        pos = pygame.mouse.get_pos()
        row, col = self.get_row_col_from_mouse(pos)
        self.choose_color(row, col)

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
            self.board.game_end = "Codebreaker"
            print("Codebreaker wins")
        elif self.turn == 8:
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


    
