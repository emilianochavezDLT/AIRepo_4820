'''
Emiliano Chavez De La Torre
CS 4820 AI
Homework 2
Solution to the N-Queens problem using the Hill Climbing algorithm,
Gennetic Algorithm, and Particle Swarm Optimization.
'''
import random

#Hill Climbing Algorithm
def hill_climbing(initial_state):
    print("\n\nHill Climbing Algorithm")
    current = initial_state
    
    #Sending the initial state to the heuristic function for attacks
    attack_heuristic = hill_climb_attacks(current) #returns the state with the least amount of attacks
    attack_heuristic_board = create_board(attack_heuristic) #Creates the board with the state with the least amount of attacks
    print_board(attack_heuristic_board) #Prints the board with the state with the least amount of attacks

    #Sending the initial state to the heuristic function for safety
    safety_heuristic = hill_climb_saftey(current) #returns the state with the least amount of unsafe queens
    safety_heuristic_board = create_board(safety_heuristic) #Creates the board with the state with the least amount of unsafe queens
    print_board(safety_heuristic_board) #Prints the board with the state with the least amount of unsafe queens



#Hill Climbing Heuristic Based on Attacks
def hill_climb_attacks(initial_state):
    print("\n\nHill Climbing Heuristic Attacks")
    current = initial_state
    while True:
        print("Current State:", current)
        value_attacks = heuristic_attacks(current)
        print("Heuristic Value Attacks:", value_attacks)
        if value_attacks == 0:
            return current
        
        successors = n_queens_successors(current)
        if not successors:
            return current
        #The min function will return the state with the least amount of attacks
        #The key parameter is the heuristic function where the state with the least amount of attacks is returned
        next_state = min(successors, key=heuristic_attacks) 
        #If the next state has more attacks than the current state, return the current state
        if heuristic_attacks(next_state) >= value_attacks:
            return current
        current = next_state
        
        
def heuristic_attacks(state):
    #This is the heuristic function that I will use for the N-Queens problem
    #The heuristic value is the number of pairs of queens that are attacking each other
    n = len(state)
    attacks = 0
    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j] or state[i] - i == state[j] - j or state[i] + i == state[j] + j:
                attacks += 1
    return attacks

#Hill Climbing Heuristic Based on Saftey
def hill_climb_saftey(initial_state):
    print("\n\nHill Climbing Heuristic Saftey")
    current = initial_state
    while True:
        print("Current State:", current)
        value_saftey = heuristic_based_on_saftey(current)
        print("Heuristic Value Saftey:", value_saftey)
        if value_saftey == 0:
            return current
        successors = n_queens_successors(current)
        if not successors:
            return current
        #The min function will return the state with the least amount of unsafe queens
        #The key parameter is the heuristic function where the state with the least amount of unsafe queens is returned
        next_state = min(successors, key=heuristic_based_on_saftey)
        #If the next state has more unsafe queens than the current state, return the current state
        if heuristic_based_on_saftey(next_state) >= value_saftey:
            return current
        current = next_state
    

def heuristic_based_on_saftey(state):
    #This is the heuristic function that I will use for the N-Queens problem
    #The heuristic value is the number of pairs of queens that are attacking each other
    if is_goal_state(state):
        return 0
    unsafe_queens = 0
    n = len(state)
    for row in range(n):
        if not is_safe(state, row, state[row]):
            unsafe_queens += 1
    return unsafe_queens



#Genetic Algorithm

#Here, Im just going to pass in n to specify the size of the board
def genetic_algorithm(n):
    max_generations = 1000

    print("\n\nGenetic Algorithm")
    population = genetic_algorithm_initial_population(n)
    
    for generation in range(max_generations):
        print("Generation:", generation)
        fitness_values = {
            individual: fitness_fn(individual) for individual in population
        }
        parents = selection(population, fitness_values)
        print("Parents:", parents)
        x, y = parents
        child = reproduce(x, y)
        if random.random() < 0.1:
            child = mutate(child)
        population.append(child)
        print("Population:", population)
        if fitness_fn(child) == 1:
            print("Solution Found:", child)
            return child
    print("No solution found")
    return None


    


#Genetic Algorithm Initial Population
#This will create an initial population of 10 individuals
#It will retturn a list of tuples, where each tuple is a permutation of column positions
def genetic_algorithm_initial_population(n):
    print("\n\nGenetic Algorithm Initial Population")
    population = []
    for i in range(10):  #Population size of 10
        #Generate a random permutation of column positions
        individual = tuple(random.sample(range(n), n))
        population.append(individual)
    return population

#Genetic Algorithm Fitness Function
#Creating the fitness function for the genetic algorithm

#This fiteness function will count the number of pairs of queens that are attacking each other
#If the fitness function returns 0, then the individual is a solution to the N-Queens problem
def fitness_fn(individual):
    attacking_pairs = heuristic_attacks(individual)
    #Calculate the fitness value
    fitnees_calculation = 1 / (attacking_pairs + 1)  #Add 1 to avoid division by zero
    if attacking_pairs == 0:
        return 1  #This is a solution to the N-Queens problem
    else:
        #Return the fitness value
        return fitnees_calculation


#Reproduction Function
#This function will take two individuals and produce a new individual/child
def reproduce(x, y):
    n = len(x)
    c = random.randint(0, n - 1)  #Random crossover point
    return x[:c] + y[c:]

#Mutation Function
#This function will take an individual and change one of its values
def mutate(individual):
    n = len(individual)
    c = random.randint(0, n - 1)  #Random mutation point
    m = random.randint(0, n - 1)  #Random mutation value
    individual = list(individual)
    individual[c] = m
    return tuple(individual)

#Selection Function
#This function will select the best individuals to be parents
def selection(population, fitness_values):
    #Sort the population by fitness value
    sorted_population = sorted(population, key=lambda individual: fitness_values[individual], reverse=True)
    #Select the best individuals to be parents
    parents = sorted_population[:2]
    return parents
    
    
    









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

    '''
    #Bellow is me calling the alogrithms to solve the N-Queens problem
    print("\n\nHill Climbing Algorithm")
    hill_climbing(initial_state)
    '''

    print("\n\nGenetic Algorithm")
    genetic_algorithm(n)



    print("\n\nParticle Swarm Optimization")
    
    
    
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

'''
********************************************************************
'''






'''
Safety Checks From the Previous Homework
********************************************************************
'''
#Reference for is_safe function https://www.geeksforgeeks.org/n-queen-problem-backtracking-3/
#Adapted to work with the n-queens problem
def is_goal_state(state):
    # Check if all queens are placed
    all_queens_placed = -1 not in state
    
    #Now we check if the state is safe
    state_is_safe = is_safe_state(state)
    return all_queens_placed and state_is_safe



def is_safe(state, row, col):
    for r in range(row):
        # Check if the queen in row r is attacking the queen we want to place
        if state[r] == col or state[r] - r == col - row or state[r] + r == col + row:
            return False
    return True


def is_safe_state(state):
    #Now we check if the state is safe
    n = len(state)
    for row in range(n):
        #Check if the queen in row r is attacking the queen we want to place
        if not is_safe(state, row, state[row]):
            #If the state is not safe, return False
            return False
    return True

'''
********************************************************************
'''


'''
Necessary Print Functions to Print the Board
********************************************************************
'''
#print board functions:
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

'''
********************************************************************
'''




'''
Main Function Being Called to Solve the N-Queens Problem
********************************************************************
'''
#N is the size of the board
n = 4 #So this is a 4x4 board
initial_board = nqueens_initial_board(n)
print("Initial Board:", initial_board)
nQueens(n, initial_board)







'''
********************************************************************
'''

