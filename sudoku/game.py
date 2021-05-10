import sys
from random import sample
from pygame.locals import *
import pygame
from data import gamedata
from sudokusolver import solve


class Game(gamedata):
       
       def __init__(self, screen):
              
              self.screen = screen
              self.Width, self.Height = pygame.display.get_surface().get_size()
              self.rects = super().rects()
              pygame.font.init()
              self.font = pygame.font.SysFont("Times New Roman", 60)
       
       def makeboard(self, difficulty: int = 40) -> [[]]:
              
              '''
              
              Taken from https://stackoverflow.com/questions/45471152/how-to-create-a-sudoku-puzzle-in-python
              Full credit to https://stackoverflow.com/users/5237560/alain-t
              
              '''
              
              base = 3
              side = base * base
              
              def pattern(r, c):
                     return (base * (r % base) + r // base + c) % side
              
              def shuffle(s):
                     return sample(s, len(s))
              
              rBase = range(base)
              rows = [g * base + r for g in shuffle(rBase) for r in shuffle(rBase)]
              cols = [g * base + c for g in shuffle(rBase) for c in shuffle(rBase)]
              nums = shuffle(range(1, base * base + 1))
              
              board = [[nums[pattern(r, c)] for c in cols] for r in rows]
              squares = side * side
              empties = squares * difficulty // 81
              for p in sample(range(squares), empties):
                     board[p // side][p % side] = 0
              
              return board
       
       def drawlines(self, linecolor: str = "#000000", LineWidth: int = 4) -> pygame.display:
              
              x_distance = self.Width / 9
              y_distance = self.Height / 9
              first_line_x = second_line_x = third_line_x = fourth_line_x = fifth_line_x = sixth_line_x = seventh_line_x = eighth_line_x = 0
              first_line_y = second_line_y = third_line_y = fourth_line_y = fifth_line_y = sixth_line_y = seventh_line_y = eighth_line_y = 0
              x_lines = [first_line_x, second_line_x, third_line_x, fourth_line_x, fifth_line_x, sixth_line_x,
                         seventh_line_x, eighth_line_x]
              y_lines = [first_line_y, second_line_y, third_line_y, fourth_line_y, fifth_line_y, sixth_line_y,
                         seventh_line_y, eighth_line_y]
              
              for index, line in enumerate(x_lines):
                     new_line = line + ((index + 1) * x_distance)
                     x_lines[index] = new_line
              
              for index, line in enumerate(y_lines):
                     new_line = line + ((index + 1) * y_distance)
                     y_lines[index] = new_line
              
              for index, line in enumerate(y_lines):
                     if (index + 1) % 3 == 0:
                            LineWidth = 9
                     
                     pygame.draw.line(self.screen, linecolor, (line, 0), (line, self.Height), LineWidth)
                     LineWidth = 4
              
              for index, line in enumerate(x_lines):
                     if (index + 1) % 3 == 0:
                            LineWidth = 9
                     
                     pygame.draw.line(self.screen, linecolor, (0, line), (self.Width, line), LineWidth)
                     LineWidth = 4
              
              pygame.display.flip()
       
       def drawboard(self, board=None) -> pygame.display:
              
              if board == None:
                     returnboard = self.makeboard()
                     board = [item for sublist in returnboard for item in sublist]
                     for index, rect in enumerate(self.rects):
                            number = board[index]
                            textsurface = self.font.render(str(number), True, '#000000')
                            if number == 0:
                                   textsurface = self.font.render('', True, '#000000')
                                   self.screen.blit(textsurface, rect)
                            else:
                                   self.screen.blit(textsurface, rect)
                                   pygame.display.update()
              else:
                     returnboard = board
                     board = [item for sublist in board for item in sublist]
                            
                     
                     for index, rect in enumerate(self.rects):
                            number = board[index]
                            textsurface = self.font.render(str(number), True, '#000000')
                            self.screen.blit(textsurface, rect)
                            pygame.display.update()
                     
              return returnboard
       
       def mainloop(self) -> pygame.display:
              
              self.screen.fill('#ffffff')
              
              board = self.drawboard()
              
              while True:
                     solve(board)
                     self.drawlines()
                     user_input = input('Type reset to reset board or solve to solve board: ')

                     event = pygame.event.poll()
                     if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                     if event.type == pygame.K_ESCAPE:
                            pygame.quit()
                            sys.exit()
                     
                     if user_input.lower() == 'reset':
                            self.screen.fill('#ffffff')
                            board = self.drawboard()
                            pygame.display.update()
                     
                     if user_input.lower() == 'solve':
                            self.screen.fill('#ffffff')
                            board = self.drawboard(board)
                            pygame.display.update()
                     
                     if user_input.lower() != 'reset' and user_input.lower() != 'solve':
                            print('Only Type reset or solve board is supported')
