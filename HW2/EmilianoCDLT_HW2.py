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
    max_generations = 10000
    population = genetic_algorithm_initial_population(n)
    
    for generation in range(max_generations):
        #print("Generation:", generation)
        parents = selection(population, fitness_fn)
        x, y = parents
        child = reproduce(x, y)
        if random.random() < 0.1:
            child = mutate(child)
        population.append(child)
        if fitness_fn(child) == 1:
            print("Solution Found:", child, "in", generation, "generations")
            child_board = create_board(child)
            print_board(child_board)
            return child
    print("No solution found in", max_generations, "generations")
    return None


    


#Genetic Algorithm Initial Population
#This will create an initial population of 10 individuals
#It will retturn a list of tuples, where each tuple is a permutation of column positions
def genetic_algorithm_initial_population(n):
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
def selection(population, fitness_function):
    fitness = [fitness_function(individual) for individual in population]
    x = random.choices(population, weights=fitness, k=1)[0]
    y = random.choices(population, weights=fitness, k=1)[0]
    parents = (x, y)
    return parents
    


#Particle Swarm Optimization

'''
First I will create a class for the Particle Swarm Optimization.
The first class will be the Particle class
It seems easier to impelemnt this way and it will be easier to understand the code.
This is my best way to translate the matlab code given in class to python.
'''

class Particle:
    def __init__(self, n):
        self.position = [random.randint(0, n-1) for _ in range(n)]
        self.velocity = [0 for _ in range(n)]
        self.fitness = float('inf')
        self.pbest_position = self.position.copy()
        self.pbest_value = float('inf')

def initialize_swarm(num_particles, n):
    return [Particle(n) for _ in range(num_particles)]

#This function will evaluate the fitness of the particle
def evaluate_fitness(particle, n):
    #Calculate the number of conflicts
    row_conflicts = len(particle.position) - len(set(particle.position))
    diagonal_conflicts = 0
    for i in range(n):
        for j in range(i+1, n):
            #Check if the queens are on the same diagonal
            if abs(particle.position[i] - particle.position[j]) == j - i:
                diagonal_conflicts += 1 #Increment the diagonal conflicts
    return row_conflicts + diagonal_conflicts

#This function will update the velocity of the particle
def update_velocity(particle, gbest_position, w, c1, c2):
    for i in range(len(particle.position)):
        #Update the velocity of the particle
        social = c1 * random.random() * (gbest_position[i] - particle.position[i])
        #Update the velocity of the particle
        cognitive = c2 * random.random() * (particle.pbest_position[i] - particle.position[i])
        #Update the velocity
        particle.velocity[i] = w * particle.velocity[i] + social + cognitive

#This function will update the position of the particle
def update_position(particle, n):
    #Update the position of the particle
    for i in range(len(particle.position)):
        if random.random() < abs(particle.velocity[i]):
            #Shift the position of the particle
            shift = 1 if particle.velocity[i] > 0 else -1
            #Update the position
            particle.position[i] = (particle.position[i] + shift) % n

#This function will update the personal best
def update_pbest(particle):
    #Check if the particle's fitness is better than its personal best
    if particle.fitness < particle.pbest_value:
        #Update the personal best
        particle.pbest_position = particle.position.copy()
        particle.pbest_value = particle.fitness

#This function will update the global best
def update_gbest(swarm, gbest):
    for particle in swarm:
        #Check if the particle's personal best is better than the global best
        if particle.pbest_value < gbest.fitness:
            #Update the global best
            gbest.position = particle.pbest_position.copy()
            #Update the global best fitness value
            gbest.fitness = particle.pbest_value

def pso(n):
    num_particles = 100
    max_iterations = 10000
    swarm = initialize_swarm(num_particles, n)
    gbest = Particle(n)  #Global best
    gbest.fitness = float('inf')


    for iteration in range(max_iterations):
        for particle in swarm:
            #Evaluate fitness
            particle.fitness = evaluate_fitness(particle, n)
            #Update personal best
            update_pbest(particle)
        update_gbest(swarm, gbest)

        for particle in swarm:
            #Update velocity and position
            update_velocity(particle, gbest.position, w=0.5, c1=1, c2=1)
            #Update position
            update_position(particle, n)

        #Check if solution is found
        if gbest.fitness == 0:
            print(f'Solution Found: {gbest.position} in {iteration} iterations')
            #Print the board
            gbest_board = create_board(gbest.position)
            print_board(gbest_board)
            return gbest.position, gbest.fitness
        
    print(f'No solution found in {max_iterations} iterations')

    return None



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

    
    #Bellow is me calling the alogrithms to solve the N-Queens problem
    print("\n\nHill Climbing Algorithm")
    hill_climbing(initial_state)
    
    
    print("\n\nGenetic Algorithm")
    genetic_algorithm(n)
    
    print("\n\nParticle Swarm Optimization")
    pso(n)
    
    
    
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
print("Initial Board:")
created_board = create_board(initial_board)
print_board(created_board)
nQueens(n, initial_board)


'''
********************************************************************
'''

