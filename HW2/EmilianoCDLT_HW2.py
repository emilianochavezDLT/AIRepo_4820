'''
Emiliano Chavez De La Torre
CS 4820 AI
Homework 2
Solution to the N-Queens problem using the Hill Climbing algorithm,
Gennetic Algorithm, and Particle Swarm Optimization.
'''






'''
Below is a copy and paste of the code from the previous homework.
This is my original code for the N-Queens problem.
I will have to retrofit this code to work with the Hill Climbing algorithm, 
Gennetic Algorithm, and Particle Swarm Optimization.
'''
def nQueens(n, initial_state):
    print("\n\n N_Queens Problem")
    if n == 1:
        return initial_state
    if n == 2 or n == 3:
        print("No solution exists")

    def create_board(state):
        board = []
        for row in range(n):
            board.append(['.'] * n)
            for col in range(n):
                if state[row] == col:
                    board[row][col] = 'Q'
        return board

    def print_board(board):
        for row in board:
            print(' '.join(row))
        print()

    create_board(initial_state)
    print_board(create_board(initial_state))
    
    #Bellow is me calling the alogrithms to solve the N-Queens problem
    print("\n\nHill Climbing Algorithm")
    
    
    
#This code initializes the board with -1s, one for each row
def nqueens_initial_board(n):
    return (-1,) * n  #Tuple of -1s, one for each row

def n_queens_successors(state):
    n = len(state)
    successors = []
    
    #Check if all queens are already placed
    if -1 not in state:
        return successors  #No more successors as all queens are placed

    #Find the next row to place a queen
    next_row = state.index(-1)
    
    for col in range(n):
        if is_safe(state, next_row, col):
            new_state = list(state)
            new_state[next_row] = col
            successors.append(tuple(new_state))  #Convert list back to tuple

    return successors


#Reference for is_safe function https://www.geeksforgeeks.org/n-queen-problem-backtracking-3/
#Adapted to work with the n-queens problem
def is_safe(state, row, col):
    for r in range(row):
        # Check if the queen in row r is attacking the queen we want to place
        if state[r] == col or state[r] - r == col - row or state[r] + r == col + row:
            return False
    return True


def is_goal_state(state):
    # Check if all queens are placed
    all_queens_placed = -1 not in state
    
    #Now we check if the state is safe
    state_is_safe = is_safe_state(state)
    return all_queens_placed and state_is_safe
    

def is_safe_state(state):
    #Now we check if the state is safe
    n = len(state)
    for row in range(n):
        #Check if the queen in row r is attacking the queen we want to place
        if not is_safe(state, row, state[row]):
            #If the state is not safe, return False
            return False
    return True

#N is the size of the board
n = 4 #So this is a 4x4 board
initial_board = nqueens_initial_board(n)
print("Initial Board:", initial_board)
nQueens(n, initial_board)

'''
********************************************************************
'''

