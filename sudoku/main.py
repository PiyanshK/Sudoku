import pygame
from game import Game


def main():
       screen = pygame.display.set_mode((640, 640))
       pygame.display.set_caption('Sudoku')
       game = Game(screen)
       game.mainloop()


if __name__ == '__main__':
       main()
