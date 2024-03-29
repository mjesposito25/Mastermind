import pygame
import random

from GameFiles.pin import Pin
from GameFiles.constants import ROWS, COLS, SQUARE_SIZE, COLORS
from GameFiles.rules import Rules

class Board:
    def __init__(self):
        self.board = []
        self.feedback = []
        self.rules = Rules()
        self.available_colors = self.rules.get_colors()
        self.code = self._make_code()
        self.create_board()
        self.game_end = None
        self.display_score = False
        self.state = 'pvc'
        self.scores = { 
            'cpu': 0,
            'player': 0,
            'p1': 0,
            'p2': 0
        }

    # add black pin "holes"
    def draw_squares(self, win):
        win.fill(COLORS['ash'])
        for row in range(ROWS+1):
            for col in range(COLS):
                if row == 0:
                    continue
                elif not (row <= ROWS - 1 and col <= COLS - 2):
                    pygame.draw.rect(win, COLORS['grey'], (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                pygame.draw.rect(win, COLORS['black'], (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 2)
    
    # creates 5 x 10 
    # maybe see if we dont need last column of zeros, as that is for code which will be stored seperately
    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                self.board[row].append(0)
        self.available_colors_board()
    
    def print_board(self):
        for row in range(ROWS):
            for col in range(COLS):
                print(self.board[row][col], end="")
            print()

    # call draw_sqaures and get pins from self.board
    def draw(self, win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                pin = self.board[row][col]
                if pin == 0:
                    if row > 0 and col < 9:
                        pygame.draw.circle(win, COLORS['black'], (SQUARE_SIZE * col + SQUARE_SIZE // 2, SQUARE_SIZE * row + SQUARE_SIZE // 2), SQUARE_SIZE // 2 - 30)
                else:
                    pin.draw(win)
        self.draw_feedback(win)
        if self.game_end != None:
            self.draw_code(win, self.game_end)
            self.draw_end_game(win)
        if self.display_score:
            self.draw_scores(win)
        self.draw_exit_button(win)
 
    def draw_end_game(self, win):
        textList = ['Replay', 'Menu', 'Scores']
        for t in enumerate(textList):
            pygame.draw.rect(win, COLORS['white'], (350, t[0] * 150 + 100, 3 * SQUARE_SIZE, SQUARE_SIZE))
            pygame.draw.rect(win, COLORS['black'], (350, t[0] * 150 + 100, 3 * SQUARE_SIZE, SQUARE_SIZE), 2)

            self._write_text(win, 45, t[1], (500, t[0] * 150 + 150))
    
    def draw_exit_button(self, win):
        pygame.draw.rect(win, COLORS['yellow'], (900, 0, SQUARE_SIZE, SQUARE_SIZE))
        pygame.draw.rect(win, COLORS['black'], (900, 0, SQUARE_SIZE, SQUARE_SIZE), 2)

        self._write_text(win, 45, 'MENU', (950, 50))

    def get_pin(self, row, col):
        return self.board[row][col]
    
    def available_colors_board(self):
        for color in enumerate(self.available_colors):
            pin = Pin(COLORS[color[1]], 0, color[0])
            self.board[0][color[0]] = pin
    
    def move(self, pin, new_row, new_col):
        self.board[pin.row][pin.col], self.board[new_row][new_col] = self.board[new_row][new_col], self.board[pin.row][pin.col]
        pin.move(new_row, new_col)


    def give_feedback(self, turn):
        checked = self.check_code(turn)
        self.feedback.append(checked)
        if checked == ['black', 'black', 'black', 'black']:
            return True
        else:
            return False
    
    def check_code(self, turn):
        feedback = []
        for i in range(4):
            pin = self.board[i+1][turn]

            color = self._get_key(pin.color)
            
            if color == self.code[i]:
                feedback.append('black')
            elif color in self.code:
                feedback.append('white')
            else:
                feedback.append('empty')
        return feedback
    
    def draw_feedback(self, win):
        for i in range(len(self.feedback)):
            for k in range(4):
                if self.feedback[i][k] != 'empty':
                    color = COLORS[self.feedback[i][k]]
                    x = 525 if k < 2 else 575
                    y = 25 + (i * 100) + (50 * (k % 2))
                    radius = SQUARE_SIZE // 4 - 10
                    pygame.draw.circle(win, color, (y, x), radius)
    
    def draw_code(self, win, who):
        for i in range(4):
            radius = SQUARE_SIZE // 2 - 15
            color = COLORS[self.code[i]]
            pygame.draw.circle(win, COLORS['black'], (950, 150 + 100 * i), radius + 2)
            pygame.draw.circle(win, color, (950, 150 + 100 * i), radius)
        
        self._write_text(win, 100, who + ' Wins!', (500, 50))

    def change_rules(self):
        pass

    def _make_code(self):
        colors = self.rules.get_colors()
        random.shuffle(colors)
        return colors

    def _get_key(self, val):
        for key, value in COLORS.items():
            if val == value:
                return key
        return "No Key!"

    def display_scores(self, score):
        self.display_score = True
        self.scores = score
    
    def draw_scores(self, win):
        win.fill(COLORS['white'])
        if self.state == 'pvc':
            self._write_text(win, 100, 'Computer: ' + str(self.scores['cpu']), (500, 100))
            self._write_text(win, 100, 'Player: ' + str(self.scores['player']), (500, 200))
        else:
            self._write_text(win, 100, 'Player 1: ' + str(self.scores['p1']), (500, 100))
            self._write_text(win, 100, 'Player 2: ' + str(self.scores['p2']), (500, 200))
    
    def _write_text(self, win, font_size, text, pos):
        font = pygame.font.SysFont(None, font_size)
        font_ren = font.render(text, True, COLORS['black'])
        text_rect = font_ren.get_rect()
        text_rect.center = pos
        win.blit(font_ren, text_rect)
