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
def DFS(inital_Node, goal_Node, successors, explored=None):
    
    # If explored is supplied with None, then create a new set
    if explored is None:
        explored = set()


    # If the inital_Node is the goal_Node, return the inital_Node
    if inital_Node == goal_Node:
        return inital_Node
    
    # Add the inital_Node to the explored set
    explored.add(inital_Node)

    #Recursivly call the DFS function for each child of the inital_Node
    for child in successors(inital_Node):
        if child not in explored:
            result = DFS(child, goal_Node, successors, explored)
            if result is not None:
                return result
    
    # If the goal_Node is not found, then backtrack until the goal_Node is found or no more nodes are left
    return None

#Iterative Deepening Search
def IDS(inital_Node, goal_Node, successors):
    
    for depth in range(0, 10000):
        result = DFS(inital_Node, goal_Node, successors, depth)
        if result is not None:
            return result
    return None

#Bidirectional Search
def BD(inital_Node, goal_Node, successors):
    
    
    


