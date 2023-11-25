import pygame
import sys
from game_constants import *
from Button import *
from Point import *

# Initialize the Pygame
pygame.init()

class AI_Sudoku_Game:

    def __init__(self,board):
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

                    p = Point(400,200,7)
                    p.draw_the_point(self.game_screen)

                        
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
            


game = AI_Sudoku_Game()

game.play_game()

        



