from .EmilianoCDLT_HW1 import *

# Path: HW1/EmilianoCDLT_HW1.py

'''
This is the n_puzzle problem where we are given a board of
size 8 and we have to move the tiles to reach the goal state

The goal state is:
 1 2 3  or  0 1 2
 4 5 6      3 4 5
 7 8 0      6 7 8

''' 
#Lets first represent the board as a list of lists

goal_board = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
#rows             0th       1st        2nd

intial_board = [[1, 2, 3], [4, 5, 6], [7, 0, 8]]
#rows               0th        1st         2nd


'''
We will next represent the moves that can be made by the blank tile
'''

def move_up(board):
    rows = len(board)
    cols = len(board[0]) if rows > 0 else 0
    for i in range(rows): #Iterate through the rows
        for j in range(cols): #Iterate through the columns
            if board[i][j] == 0: #If the blank tile is found
                #Then check if the blank tile can be moved up
                if i == 0: # If the blank tile is in the top row
                    return None #Cannot move up because this is an invalid move
                else:
                    new_board = [x[:] for x in board] #Create a new board
                    new_board[i][j] = new_board[i-1][j] #Move the tile above the blank tile
                    new_board[i-1][j] = 0 #Move the blank tile to the top
                    return new_board #Return the new board
    return None

def move_down(board):
    rows = len(board)
    cols = len(board[0]) if rows > 0 else 0
    for i in range(rows):
        for j in range(cols): 
            if board[i][j] == 0: 
                if i == rows-1: # If the blank tile is in the bottom row
                    return None 
                else:
                    new_board = [x[:] for x in board] 
                    new_board[i][j] = new_board[i+1][j] #Move the tile below the blank tile
                    new_board[i+1][j] = 0 #Move the blank tile to the bottom
                    return new_board 
    return None

def move_left(board):
    rows = len(board)
    cols = len(board[0]) if rows > 0 else 0
    for i in range(rows): 
        for j in range(cols):
            if board[i][j] == 0: 
                if j == 0: # If the blank tile is in the leftmost column
                    return None 
                else:
                   new_board = [x[:] for x in board] 
                   new_board[i][j] = new_board[i][j-1] #Move the tile to the left of the blank tile
                   new_board[i][j-1] = 0  #Move the blank tile to the left
                   return new_board 
    return None

def move_right(board):
    rows = len(board)
    cols = len(board[0]) if rows > 0 else 0
    for i in range(rows): 
        for j in range(cols): 
            if board[i][j] == 0:
                if j == cols-1: # If the blank tile is in the rightmost column
                    return None 
                else:
                    new_board = [x[:] for x in board] 
                    new_board[i][j] = new_board[i][j+1] #Move the tile to the right of the blank tile
                    new_board[i][j+1] = 0 #Move the blank tile to the right
                    return new_board
    return None

