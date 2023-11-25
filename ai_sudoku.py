import pygame
import sys
from game_constants import *

# Initialize the Pygame
pygame.init()

class AI_Sudoku_Game:

    def __init__(self):
        self.STATE = START_STATE
        self.RUNNING = True
        # create game state screens
        # Create the screen
        self.game_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.start_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.end_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.settings_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


    def play_game(self):

        while self.RUNNING:

            if self.STATE == START_STATE:

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                            self.RUNNING = False

                self.start_screen.fill(OLIVE)
                pygame.display.flip()



            elif self.STATE == GAME_STATE:

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                            self.RUNNING = False
            

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

        



