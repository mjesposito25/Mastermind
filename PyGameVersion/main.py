import pygame
from GameFiles.constants import SIZE, SQUARE_SIZE
from GameFiles.game import Game

FPS = 60

WIN = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Mastermind")

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE

    return row, col

def main():
    clock = pygame.time.Clock()
    run = True

    game = Game(WIN)
    pygame.font.init()

    while run:
        # ensures doesn't run more than fps cap
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
            if event.type == pygame.MOUSEBUTTONDOWN:
                game.game_loop()

        game.update()
        
    pygame.quit()

if __name__ == "__main__":
    main()
