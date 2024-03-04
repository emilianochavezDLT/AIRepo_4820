#Emiliano Chavez De La Torre

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
    

# Breadth-First Search
#Pseudocode reference was from Russell and Norvig's book Pg. 82
def BFS(inital_Node, goal_Node, successors):
    
    # If the inital_Node is the goal_Node, return the inital_Node
    if inital_Node == goal_Node:
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
            return node
        
        
        # Add the node to the explored set
        explored.add(node)
        
        # Get the successors of the node
        children = successors(node)
        
        # For each child of the node
        for child in children:
            # If the child is not in the frontier or the explored set
            if child not in frontier and child not in explored:
                # If the child is the goal_Node, return the child
                if child == goal_Node:
                    return child
                else:
                    # Add the child to the frontier
                    frontier.append(child)
    
    return None
                

#So this is DFS without a cutoff, so it will run until the goal is found or no more nodes are left
#Pseudocode reference was from Russell and Norvig's book Pg. 88, which I modified to be without a cutoff
#This can go into an infinite loop if the graph is infinite
def DFS(inital_Node, goal_Node, successors):
    
    explored = set() #Create an empty set to store the explored nodes
    stack = deque([inital_Node]) #Create a stack with the inital_Node

    while stack: 
        node = stack.pop() #Pop the last element of the stack

        if node == goal_Node:
            return node
        
        explored.add(node) #Add the node to the explored set
        children = successors(node) #Get the children of the node
        for child in children: 
            #If the child is not in the explored set or the stack
            if child not in explored and child not in stack: 
                #If the child is the goal_Node, return the child
                stack.append(child)

    return None
    

#Iterative Deepening Search Russell and Norvig's book Pg. 88
def IDS(inital_Node, goal_Node, successors):
    for depth in range(0, 1000):
        result = DLS(inital_Node, goal_Node, successors, depth)
        if result is not None:
            return result
    return None

#Depth-Limited Search from 
def DLS(inital_Node, goal_Node, successors, depth):
    explored = set() #Create an empty set to store the explored nodes
    stack = deque([inital_Node]) #Create a stack with the inital_Node
    while stack:
        node = stack.pop() #Pop the last element of the stack and assign it to node
        if node == goal_Node: #If the node is the goal_Node, return the node
            return node
        if depth == 0: #If the depth is 0, continue
            continue
        explored.add(node) #Add the node to the explored set
        children = successors(node) 
        for child in children:
            #If the child is not in the explored set or the stack
            if child not in explored and child not in stack:
                stack.append(child) #Add the child to the stack
    return None



#Bidirectional Search
#Pseudocode reference was from Russell and Norvig's book Pg. 91
def BD(initial_Node, goal_Node, successors):
    if initial_Node == goal_Node:
        return initial_Node

    # Create the frontier and explored set for the initial_Node
    frontier_initial = deque([initial_Node])
    explored_initial = set()

    # Create the frontier and explored set for the goal_Node
    frontier_goal = deque([goal_Node])
    explored_goal = set()

    while frontier_initial and frontier_goal:
        # Run BFS from initial_Node
        node_initial = BFS(frontier_initial[0], goal_Node, successors)
        if node_initial is not None:
            return node_initial
        frontier_initial.popleft()
        explored_initial.add(node_initial)

        # Run BFS from goal_Node
        node_goal = BFS(frontier_goal[0], initial_Node, successors)
        if node_goal is not None:
            return node_goal
        frontier_goal.popleft()
        explored_goal.add(node_goal)

    return None


def successors(node):
    moves = [move_up, move_down, move_left, move_right]
    return [move(node) for move in moves if move(node) is not None]



'''This is the start of the n_puzzle problem
********************************************************************
'''

'''
This is the n_puzzle problem where we are given a board of
size 8 and we have to move the tiles to reach the goal state

The goal state is:
 1 2 3  or  0 1 2
 4 5 6      3 4 5
 7 8 0      6 7 8
''' 

#Lets first represent the board as a list of lists

goal_board = ((1, 2, 3), (4, 5, 6), (7, 8, 0))
#rows             0th       1st        2nd

initial_board = ((1, 2, 3), (4, 5, 6), (7, 0, 8))
#rows               0th        1st         2nd

initial_board2 = ((1, 2, 3), (4, 5, 6), (7, 8, 0))


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


''' Implmenting the solve function for the n_puzzle problem
********************************************************************
'''
#print(graphSearch(initial_board2, goal_board, successors, "bfs"))
#print(graphSearch(initial_board2, goal_board, successors, "dfs"))
#print(graphSearch(initial_board, goal_board, successors, "id"))
print(graphSearch(initial_board, goal_board, successors, "bd"))


