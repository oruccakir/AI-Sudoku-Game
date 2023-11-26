import pygame
import sys
from game_constants import *
from Button import *
from Point import *
from SudokuSolver import *
import random

# Initialize the Pygame
pygame.init()

class AI_Sudoku_Game:

    def __init__(self,board):

        self.game_speed = GAME_SPEED

        self.solution_points = []

        self.isPaussed = False
        self.x = 140
        self.y = 180
        self.board = board
        # add buttons
        self.start_button = Button(300, 750, 300, 50, "AI START",GRAY,self.start_button_action)
        self.end_button = Button(300, 800, 200, 50, "END",GRAY,self.end_button_action)
        self.restart_button = Button(300, 600, 200, 50, "RESTART",GRAY,self.restart_button_action)
        self.pause_button = Button(25,25,150,40,"PAUSE",YELLOW,self.pause_button_action)
        self.settings_button = Button(375,25,150,40,"SETTINGS",BLUE,self.settings_button_action)
        self.return_game_button = Button(300,700,200,50,"RETURN",GRAY,self.return_game_button_action)

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
                value = False
                if element == 0:
                    value = False
                else:
                    value = True
                point = Point(width,height,element,value)

                if point.isThere == False:
                    self.solution_points.append(point)

                row_points.append(point)
                
                width += SQUARE_WIDTH
            
            width = self.x
           
            height += SQUARE_WIDTH
            

            points.append(row_points)
        
        return points
    
    def draw_the_points(self):
         
        x = self.x
        y = self.y
        x1 = self.x
        y1 = self.y
        line_color = BLACK
        start_point1 = (x,y)
        end_point1 = (x + 9*SQUARE_WIDTH,y)
        start_point2 = (x1,y1)
        end_point2 = (x1,y1+9*SQUARE_WIDTH)


        for row in self.points:
            
            for point in row:
                point.draw_the_point(self.game_screen)
            pygame.draw.line(self.game_screen,line_color,start_point1,end_point1,5)

            y+=SQUARE_WIDTH
            start_point1 = (x,y)
            end_point1 = (x + 9*SQUARE_WIDTH,y)
        
        pygame.draw.line(self.game_screen,line_color,start_point1,end_point1,5)

        for row in self.points:
            pygame.draw.line(self.game_screen,line_color,start_point2,end_point2,5)
            x1 += SQUARE_WIDTH
            start_point2 = (x1,y1)
            end_point2 = (x1,y1+9*SQUARE_WIDTH)
        pygame.draw.line(self.game_screen,line_color,start_point2,end_point2,5)
            
             
                  

    def start_button_action(self):
        self.STATE = GAME_STATE
    
    def end_button_action(self):
        self.RUNNING = False
    
    def settings_button_action(self):
        self.isPaussed = True
        self.STATE = SETTING_STATE
    
    def return_game_button_action(self):
        self.STATE = GAME_STATE
        self.pause_button.text = "Continue"
    
    def restart_button_action(self):
        self.RUNNING = True
        self.solution_points = []
        self.points = self.create_data_points()
        self.STATE = START_STATE
    
    def pause_button_action(self):
        if self.isPaussed == False:
            self.isPaussed = True
            self.pause_button.text = "Continue"
        else:
            self.isPaussed = False
            self.pause_button.text = "Pause"

    def play_game(self):

        # set timer
        pygame.time.set_timer(pygame.USEREVENT, self.game_speed)

        sd = Sudoku(sudoku_board,len(sudoku_board))

        solution = sd.solveSudoku()

        printMatrix(solution)

        print(len(self.solution_points))
        
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
                    
                    elif event.type == pygame.USEREVENT and self.isPaussed == False:
                        if len(self.solution_points) > 0:
                            random.shuffle(self.solution_points)
                            random_point = self.solution_points.pop()
                            random_point.number = solution[int((random_point.y - self.y) / SQUARE_WIDTH)][int((random_point.x - self.x) / SQUARE_WIDTH)]
                            random.shuffle(self.solution_points)
                            random_point.color = GREEN

                    
                    self.settings_button.check_click(event)
                    self.pause_button.check_click(event)                    
                    

                    
                    self.game_screen.fill(SILVER)

                    self.draw_the_points()

                    self.settings_button.draw_button(self.game_screen)
                    self.pause_button.draw_button(self.game_screen)

                        
                    pygame.display.flip()
                    

            elif self.STATE == SETTING_STATE:
                
                for event in pygame.event.get():
                    
                    if event.type == pygame.QUIT:
                            self.RUNNING = False
                    
                    self.restart_button.check_click(event)
                    self.end_button.check_click(event)
                    self.return_game_button.check_click(event)
                    

                
                self.settings_screen.fill(WHITE)

                self.restart_button.draw_button(self.settings_screen)
                self.end_button.draw_button(self.settings_screen)
                self.return_game_button.draw_button(self.settings_screen)


                pygame.display.flip()
            

            elif self.STATE == END_STATE:
                
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                            self.RUNNING = False
                        
                    self.end_button.check_click(event)
                    self.restart_button.check_click(event)

                
                self.end_screen.fill(MAROON)

                self.end_button.draw_button(self.end_screen)
                self.restart_button.draw_button(self.end_screen)
                    

                pygame.display.flip()
            
sudoku_board = [
    [0, 0, 0, 5, 0, 0, 3, 0, 0],
    [0, 7, 0, 0, 3, 2, 0, 0, 5],
    [0, 3, 0, 7, 6, 0, 0, 0, 9],
    [0, 0, 0, 4, 0, 7, 0, 0, 8],
    [0, 0, 0, 0, 0, 0, 0, 3, 0],
    [2, 5, 0, 0, 0, 0, 9, 0, 7],
    [7, 2, 0, 3, 0, 9, 5, 0, 0],
    [8, 9, 0, 2, 0, 0, 0, 0, 0],
    [0, 0, 5, 0, 0, 0, 0, 0, 6]
]

# You can use this list as the starting point for your 9x9 Sudoku game in Python.


game = AI_Sudoku_Game(sudoku_board)

game.play_game()
        



