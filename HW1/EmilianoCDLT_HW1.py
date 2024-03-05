#Emiliano Chavez De La Torre
#CS 4820

#source for deque and collections library: https://docs.python.org/3/library/collections.html#collections.deque
from collections import deque




def graphSearch(inital_Node, goal_Node, successors, search_strategy):
    if search_strategy == 'bfs':
        return BFS(inital_Node, goal_Node, successors)
    elif search_strategy == 'dfs':
        return DFS(inital_Node, goal_Node, successors)
    elif search_strategy == 'id':
        return IDS(inital_Node, goal_Node, successors)
    elif search_strategy == 'bd':
        return BD(inital_Node, goal_Node, successors)
    else:
        return None

def print_BFS_Cost(cost):
    print("\nBreadth-First Search Cost:" , cost)   

# Breadth-First Search
#Pseudocode reference was from Russell and Norvig's book Pg. 82
def BFS(inital_Node, goal_Node, successors):
    
    cost = 0
    # If the inital_Node is the goal_Node, return the inital_Node
    if inital_Node == goal_Node:
        print_BFS_Cost(cost)
        return inital_Node
    
    # Create the frontier and explored set
    frontier = deque([inital_Node])
    explored = set()
    
    # While the frontier is not empty
    while frontier:
        # Pop the first element of the frontier
        node = frontier.popleft()
        
        # If the node is the goal_Node, return the node
        if node == goal_Node:
            print_BFS_Cost(cost)
            return node
        
        
        # Add the node to the explored set
        explored.add(node)
        
        # Get the successors of the node
        children = successors(node)
        
        # For each child of the node
        for child in children:
            cost += 1
            # If the child is not in the frontier or the explored set
            if child not in frontier and child not in explored:
                # If the child is the goal_Node, return the child
                if child == goal_Node:
                    print_BFS_Cost(cost)
                    return child
                else:
                    # Add the child to the frontier
                    frontier.append(child)
    
    return None
                

def print_DFS_Cost(cost):
    print("\nDepth-First Search Cost:" , cost)


#Depth-First Search
#So this is DFS without a cutoff, so it will run until the goal is found or no more nodes are left
#Pseudocode reference was from Russell and Norvig's book Pg. 88, which I modified to be without a cutoff
#This can go into an infinite loop if the graph is infinite
def DFS(inital_Node, goal_Node, successors):
    
    cost = 0
    explored = set() #Create an empty set to store the explored nodes
    stack = deque([inital_Node]) #Create a stack with the inital_Node

    while stack: 
        node = stack.pop() #Pop the last element of the stack

        if node == goal_Node:
            print_DFS_Cost(cost)
            return node
        
        explored.add(node) #Add the node to the explored set
        children = successors(node) #Get the children of the node
        for child in children: 
            cost += 1
            #If the child is not in the explored set or the stack
            if child not in explored and child not in stack: 
                #If the child is the goal_Node, return the child
                stack.append(child)

    return None
    

def print_IDS_Cost(cost):
    print("\nIterative Deepening Search Cost:" , cost)

#Iterative Deepening Search Russell and Norvig's book Pg. 88
def IDS(inital_Node, goal_Node, successors):
    for depth in range(0, 1000):
        result = DLS(inital_Node, goal_Node, successors, depth)
        if result is not None:
            return result
    return None


#Depth-Limited Search from 
def DLS(inital_Node, goal_Node, successors, depth):
    cost = 0
    explored = set() #Create an empty set to store the explored nodes
    stack = deque([inital_Node]) #Create a stack with the inital_Node
    while stack:
        node = stack.pop() #Pop the last element of the stack and assign it to node
        if node == goal_Node: #If the node is the goal_Node, return the node
            print_IDS_Cost(cost)
            return node
        if depth == 0: #If the depth is 0, continue
            continue
        explored.add(node) #Add the node to the explored set
        children = successors(node) 
        for child in children:
            cost += 1
            #If the child is not in the explored set or the stack
            if child not in explored and child not in stack:
                stack.append(child) #Add the child to the stack
    return None


def print_BD_Cost(cost):
    print("\nBi-directional Cost:" , cost)

#Bidirectional Search
#Pseudocode reference was from Russell and Norvig's book Pg. 91
def BD(initial_Node, goal_Node, successors):
    cost = 0
    if initial_Node == goal_Node:
        print_BD_Cost(cost)
        return initial_Node

    # Create the frontier and explored set for the initial_Node
    frontier_initial = deque([initial_Node])
    explored_initial = set([initial_Node])

    # Create the frontier and explored set for the goal_Node
    frontier_goal = deque([goal_Node])
    explored_goal = set([goal_Node])

    while frontier_initial and frontier_goal:
        # Expand from initial_Node
        node_initial = frontier_initial.popleft()
        for child in successors(node_initial):
            cost += 1
            if child in explored_goal:
                print_BD_Cost(cost)
                print("The intersection is: ", child)
                return child #Found the intersection
            if child not in explored_initial:
                frontier_initial.append(child)
                explored_initial.add(child)

        #Expand from goal_Node
        node_goal = frontier_goal.popleft()
        for child in successors(node_goal):
            if child in explored_initial:
                print_BD_Cost(cost)
                print("The intersection is: ", child)
                return child #Found the intersection
            if child not in explored_goal:
                frontier_goal.append(child)
                explored_goal.add(child)

    return None


def successors(node):
    moves = [move_up, move_down, move_left, move_right] #List of moves that can be made
    successors_states = []
    for move in moves:
        new_state = move(node) #Get the new state after making the move
        #If the new state is not None, add it to the list of successors
        if new_state is not None: 
            successors_states.append(new_state)
    return successors_states



'''This is the start of the n_puzzle problem
********************************************************************
'''

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
                    new_board = [list(row) for row in board] #Create a new board
                    new_board[i][j] = new_board[i-1][j] #Move the tile above the blank tile
                    new_board[i-1][j] = 0 #Move the blank tile to the top
                    return tuple(tuple(row) for row in new_board) #Return the new board
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
                    new_board = [list(row) for row in board] 
                    new_board[i][j] = new_board[i+1][j] #Move the tile below the blank tile
                    new_board[i+1][j] = 0 #Move the blank tile to the bottom
                    return tuple(tuple(row) for row in new_board) 
                    
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
                   new_board = [list(row) for row in board]
                   new_board[i][j] = new_board[i][j-1]
                   new_board[i][j-1] = 0
                   return tuple(tuple(row) for row in new_board)                 
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
                    new_board = [list(row) for row in board]
                    new_board[i][j] = new_board[i][j+1] #Move the tile to the right of the blank tile
                    new_board[i][j+1] = 0 #Move the blank tile to the right
                    return tuple(tuple(row) for row in new_board) #Return the new board
    return None

'''
This is the n_puzzle problem where we are given a board of
size 8 and we have to move the tiles to reach the goal state

The goal state is:
 1 2 3 
 4 5 6 
 7 8 0 
''' 

def nPuzzle(n, initial_board):
    print("\n\n N_Puzzle Problem\n")
    # Create the goal state for an n-puzzle
    goal_board = [tuple(range(i*n + 1, (i+1)*n + 1)) for i in range(n)]
    goal_board[-1] = goal_board[-1][:-1] + (0,)  # Replace the last element of the last tuple with 0
    goal_board = tuple(goal_board)  # Convert the list of tuples to a tuple of tuples

    
    print("Initial Board:", initial_board)
    print("Goal Board:", goal_board)

    # Run the search algorithms
    result = graphSearch(initial_board, goal_board, successors, 'bfs')
    print("BFS Result:", result)
    result = graphSearch(initial_board, goal_board, successors, 'dfs')
    print("DFS Result:", result)
    result = graphSearch(initial_board, goal_board, successors, 'id')
    print("IDS Result:", result)
    result = graphSearch(initial_board, goal_board, successors, 'bd')
    print("BD Result:", result)



initial_board = ((1, 2, 3), (4, 5, 6), (0, 7, 8))
#rows               0th        1st         2nd
nPuzzle(3, initial_board)

initial_board2 = ((1, 2, 3, 4), (5, 6, 7, 8), (9, 10, 11, 12), (0, 13, 14, 15))
nPuzzle(4, initial_board2)




''' 
********************************************************************
'''




''' The n_queens problem 
********************************************************************
'''
'''
The Rules of the n-queens problem are:

1: No two queens can be in the same row
2: No two queens can be in the same column
3: No two queens can be in the same diagonal

This is a 4x4 board
    0 1 2 3
    
    0 Q . . .
    1 . . Q .
    2 . . . Q
    3 . Q . .

The goal is to place the queens in such a way that no two queens are attacking each other

The 4x4 Goal state is:

    0 1 2 3

    0 . Q . .
    1 . . . Q
    2 Q . . .
    3 . . Q .

'''

def graphSearch_queens(inital_Node, goal_state, successors, search_strategy):
    if search_strategy == 'bfs':
        return BFS_queens(inital_Node, goal_state, successors)
    elif search_strategy == 'dfs':
        return DFS_queens(inital_Node, goal_state, successors)
    elif search_strategy == 'id':
        return IDS_queens(inital_Node, goal_state, successors)
    elif search_strategy == 'bd':
        return BD_queens(inital_Node, goal_state, successors)
    else:
        return None


def print_BFS_Cost(cost):
    print("\nBreadth-First Search Cost:" , cost)   

# Breadth-First Search
#Pseudocode reference was from Russell and Norvig's book Pg. 82
def BFS_queens(inital_Node, goal_state,successors):
    cost = 0

    #This creates a check 
    if goal_state(inital_Node):
        print_BFS_Cost(cost)
        return inital_Node

    frontier = deque([inital_Node])
    explored = set()

    while frontier:
        node = frontier.popleft()
        #print("Node: ", node)
        
        #print(goal_state(node))

        if goal_state(node):
            print_BFS_Cost(cost)
            return node

        explored.add(tuple(node))
        children = successors(node)

        for child in children:
            cost += 1
            if child not in frontier and tuple(child) not in explored:
                frontier.append(child)

    return None
                

def print_DFS_Cost(cost):
    print("\nDepth-First Search Cost:" , cost)


#Depth-First Search
#So this is DFS without a cutoff, so it will run until the goal is found or no more nodes are left
#Pseudocode reference was from Russell and Norvig's book Pg. 88, which I modified to be without a cutoff
#This can go into an infinite loop if the graph is infinite
def DFS_queens(inital_Node, goal_Node, successors):
    
    cost = 0
    explored = set() #Create an empty set to store the explored nodes
    stack = deque([inital_Node]) #Create a stack with the inital_Node

    while stack: 
        node = stack.pop() #Pop the last element of the stack

        if goal_Node(node):
            print_DFS_Cost(cost)
            return node
        
        explored.add(node) #Add the node to the explored set
        children = successors(node) #Get the children of the node
        for child in children: 
            cost += 1
            #If the child is not in the explored set or the stack
            if child not in explored and child not in stack: 
                #If the child is the goal_Node, return the child
                stack.append(child)

    return None
    

def print_IDS_Cost(cost):
    print("\nIterative Deepening Search Cost:" , cost)

#Iterative Deepening Search Russell and Norvig's book Pg. 88
def IDS_queens(inital_Node, goal_Node, successors):
    for depth in range(0, 1000):
        result = DLS_queens(inital_Node, goal_Node, successors, depth)
        if result is not None:
            return result
    return None


#Depth-Limited Search from 
def DLS_queens(inital_Node, goal_Node, successors, depth):
    cost = 0
    explored = set() #Create an empty set to store the explored nodes
    stack = deque([inital_Node]) #Create a stack with the inital_Node
    while stack:
        node = stack.pop() #Pop the last element of the stack and assign it to node
        if goal_Node(node): #If the node is the goal_Node, return the node
            print_IDS_Cost(cost)
            return node
        if depth == 0: #If the depth is 0, continue
            continue
        explored.add(node) #Add the node to the explored set
        children = successors(node) 
        for child in children:
            cost += 1
            #If the child is not in the explored set or the stack
            if child not in explored and child not in stack:
                stack.append(child) #Add the child to the stack
    return None


def print_BD_Cost(cost):
    print("\nBi-directional Cost:" , cost)

#Bidirectional Search
#Pseudocode reference was from Russell and Norvig's book Pg. 91
def BD_queens(initial_Node, goal_Node, successors):
    cost = 0
    print_BD_Cost(cost)
    return(":( This one is a little tricky")

    cost = 0
    if initial_Node == goal_Node:
        print_BD_Cost(cost)
        return initial_Node

    # Create the frontier and explored set for the initial_Node
    frontier_initial = deque([initial_Node])
    explored_initial = set([initial_Node])

    # Create the frontier and explored set for the goal_Node
    frontier_goal = deque([goal_Node])
    explored_goal = set([goal_Node])

    while frontier_initial and frontier_goal:
        # Expand from initial_Node
        node_initial = frontier_initial.popleft()
        for child in successors(node_initial):
            cost += 1
            if child in explored_goal:
                print_BD_Cost(cost)
                print("The intersection is: ", child)
                return child #Found the intersection, Hallelujah
            if child not in explored_initial:
                frontier_initial.append(child)
                explored_initial.add(child)

        # Expand from goal_Node
        node_goal = frontier_goal.popleft()
        for child in successors(node_goal):
            if child in explored_initial:
                print_BD_Cost(cost)
                print("The intersection is: ", child)
                return child #Found the intersection, Hallelujah
            if child not in explored_goal:
                frontier_goal.append(child)
                explored_goal.add(child)

    return None



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
    
    result = graphSearch_queens(initial_state, is_goal_state, n_queens_successors, 'bfs')
    print("BFS Result: ", result)
    print("BFS Board: ")
    print_board(create_board(result))
    result = graphSearch_queens(initial_state, is_goal_state, n_queens_successors, 'dfs')
    print("DFS Result: ", result)
    print("DFS Board: ")
    print_board(create_board(result))
    result = graphSearch_queens(initial_state, is_goal_state, n_queens_successors, 'id')
    print("IDS Result: ", result)
    print("IDS Board: ")
    print_board(create_board(result))
    result = graphSearch_queens(initial_state, is_goal_state, n_queens_successors, 'bd')
    print("BD Result: ", result)
    print("BD Board: ")
    print_board(create_board(result))
    

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
n = 4
initial_board = nqueens_initial_board(n)
nQueens(n, initial_board)

'''
********************************************************************
'''

