import pygame
import math


class gamedata:
       
       def rects(self, hieght=640, width=640):
              
              y_difference = hieght / 9
              x_difference = width / 9
              rects = []
              y = 0
              x = 0
              for i in range(81): rects.append(i)
              
              for index, i in enumerate(rects):
                     
                     index += 1
                     
                     if math.ceil(index / 9) == 1:
                            y = 0
                     
                     if math.ceil(index / 9) == 2:
                            y = y_difference
                     
                     if math.ceil(index / 9) == 3:
                            y = y_difference * 2
                     
                     if math.ceil(index / 9) == 4:
                            y = y_difference * 3
                     
                     if math.ceil(index / 9) == 5:
                            y = y_difference * 4
                     
                     if math.ceil(index / 9) == 6:
                            y = y_difference * 5
                     
                     if math.ceil(index / 9) == 7:
                            y = y_difference * 6
                     
                     if math.ceil(index / 9) == 8:
                            y = y_difference * 7
                     
                     if math.ceil(index / 9) == 9:
                            y = y_difference * 8
                     
                     index -= 1
                     
                     if (index + 9) % 9 == 0:
                            x = 0
                     
                     if (index + 9) % 9 == 1:
                            x = x_difference
                     
                     if (index + 9) % 9 == 2:
                            x = x_difference * 2
                     
                     if (index + 9) % 9 == 3:
                            x = x_difference * 3
                     
                     if (index + 9) % 9 == 4:
                            x = x_difference * 4
                     
                     if (index + 9) % 9 == 5:
                            x = x_difference * 5
                     
                     if (index + 9) % 9 == 6:
                            x = x_difference * 6
                     
                     if (index + 9) % 9 == 7:
                            x = x_difference * 7
                     
                     if (index + 9) % 9 == 8:
                            x = x_difference * 8
                     
                     x += 15
                     
                     rect = pygame.Rect(x, y, x_difference, y_difference)
                     
                     rects[index] = rect
              
              return rects
