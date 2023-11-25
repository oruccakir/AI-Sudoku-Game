import pygame
import sys
from game_constants import *
from Button import *
from Point import *

# Initialize the Pygame
pygame.init()

class AI_Sudoku_Game:

    def __init__(self,board):
        self.x = 200
        self.y = 250
        self.board = board
        # add buttons
        self.start_button = Button(300, 750, 300, 50, "AI START",GRAY,self.start_button_action)
        self.STATE = START_STATE
        self.RUNNING = True
        # create game state screens
        # Create the screen
        self.game_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.start_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.end_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.settings_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        self.points = self.create_data_points()
        

    def create_data_points(self):
        points = []
        width = self.x
        height = self.y
        for row in self.board:
            row_points = []
            for element in row: 
                row_points.append(Point(width,height,element))
                
                width += SQUARE_WIDTH
            
            width = self.x

            height += SQUARE_WIDTH
            

            points.append(row_points)
        
        return points
    
    def draw_the_points(self):
         for row in self.points:
              
              for point in row:
                   point.draw_the_point(self.game_screen)
            
                  

    def start_button_action(self):
        self.STATE = GAME_STATE

    def play_game(self):

        while self.RUNNING:

            if self.STATE == START_STATE:

                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                            self.RUNNING = False
                    
                    self.start_button.check_click(event)
                
                self.start_screen.fill(OLIVE)

                # Update the display
                self.start_button.draw_button(self.start_screen)

            
                pygame.display.flip()


            elif self.STATE == GAME_STATE:

                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                            self.RUNNING = False
                    
                    self.game_screen.fill(SILVER)

                    self.draw_the_points()

                        
                    pygame.display.flip()
                    
                    

            

            elif self.STATE == SETTING_STATE:
                
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                            self.RUNNING = False
            
            elif self.STATE == PAUSE_STATE:
                
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                            self.RUNNING = False
            
            elif self.STATE == END_STATE:
                
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                            self.RUNNING = False
            
sudoku_board = [
    [0, 2, 0, 4, 0, 6, 0, 8, 0],
    [4, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 6, 0, 0, 0, 7, 0, 0],
    [0, 0, 0, 5, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 8, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 9, 0, 0, 0],
    [0, 0, 5, 0, 0, 0, 6, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 4],
    [0, 6, 0, 8, 0, 2, 0, 3, 0]
]

# You can use this list as the starting point for your 9x9 Sudoku game in Python.


game = AI_Sudoku_Game(sudoku_board)

game.play_game()

        



