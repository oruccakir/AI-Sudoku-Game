import pygame
from game_constants import *

class Point:
    def __init__(self,x,y,number):
        self.x = x
        self.y = y
        self.number = number
        self.square = pygame.Rect(x,y,SQUARE_WIDTH,SQUARE_WIDTH)
        self.color = WHITE
    
    def draw_the_point(self,surface):
        pygame.draw.rect(surface,self.color,self.square)
        font = pygame.font.Font(None,50)
        #if self.number != 0:
        text = font.render(str(self.number),True,(0,0,0))
        text_rect = text.get_rect(center = self.square.center)
        surface.blit(text,text_rect)
         