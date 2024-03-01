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
#rows             0            1           2

intial_board = [[1, 2, 3], [4, 5, 6], [7, 0, 8]]
#rows               0            1           2






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
                    temp = board[i][j] #Swap the blank tile with the tile above it
                    board[i][j] = board[i-1][j] #Move the tile above the blank tile
                    board[i-1][j] = temp #Move the blank tile to the top
                    return board #Return the new board
    return None



