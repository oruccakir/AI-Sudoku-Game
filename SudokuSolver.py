import math

class Sudoku:

    def __init__(self,board,n):
        self.board = board
        self.dim = n
        self.box_dim = int(math.sqrt(self.dim))
        self.truth_table = []
        

        for row in board:
            truth_row = []
            for element in row:
                if element == 0:
                    truth_row.append(False)
                else:
                    truth_row.append(True)
                
            self.truth_table.append(truth_row)


    
    def isSafe(self,row,col,num):

        for i in range(0,self.dim):
            if self.board[row][i] == num:
                return False
        
        for i in range(0,self.dim):
            if self.board[i][col] == num:
                return False
        
        start_row = row - row % self.box_dim
        start_col = col - col % self.box_dim

        for i in range(0,self.box_dim):
            for k in range(0,self.box_dim):
                if self.board[i+start_row][k+start_col] == num:
                    return False
        
        return True
    

    def solveUtil(self):
        row = -1
        col = -1
        isEmpty = True

        i=0
        while i < self.dim and isEmpty:
            k=0
            while k < self.dim and isEmpty:
                if self.board[i][k] == 0:
                    row = i
                    col = k
                    isEmpty = False
                k=k+1
            i=i+1
        
        if isEmpty:
            return True
        
        for num in range(1,self.dim+1,1):

            if self.isSafe(row,col,num):

                self.board[row][col] = num

                if self.solveUtil():
                    return True

                self.board[row][col] = 0
        
        return False
    

    def solveSudoku(self):
        solution = []
        if self.solveUtil():
            for row in self.board:
                r1 = []
                for element in row:
                    r1.append(element)
                solution.append(r1)

        return solution
    
def printMatrix(matrix):
    for row in matrix:
        for element in row:
            print(element,end=" ")
        print()
    
def printSolutions(solution_set):
    for element in solution_set:
        printMatrix(element)



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






