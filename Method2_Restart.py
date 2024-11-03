############################################################################
#                 CS316 – Introduction to AI                               #
#            Assignment 2: The Knapsack Problem                            #
#                                                                          #
# Name: Ulas DEMIRTAS                                                      #
# ID : 002326630                                                           #
############################################################################


import random

# Solving the Knapsack Problem with Hill Climbing - METHOD2 - Item Inclusion/Exclusion Toggle
# Step 1: Define the Items

items = [
    {"weight": 2, "value": 3},  
    {"weight": 3, "value": 4},  
    {"weight": 4, "value": 5},  
    {"weight": 5, "value": 8}   
]
knapsack_capacity = 5

# Randomly include or exclude each item to create a random solution 

def random_solution(items):
 
    solution = [random.choice([0, 1]) for _ in range(len(items))]
    return solution


#Step 3 Evaluate the current random solution
def evaluate_solution(solution, items, capacity):
    total_weight = 0
    total_value = 0
    for i, selected in enumerate(solution):
        if selected == 1:
            total_weight += items[i]["weight"]
            total_value += items[i]["value"]
    
    if total_weight > capacity:
        return 0 
    return total_value

#Step 4: Explore Neighbors / generate new neighbors list by toogling method1
def generate_neighbors(solution):
    neighbors = []
    for i in range(len(solution)):
        neighbor = solution.copy()
        # Toggle the inclusion of the item in each loop lenght of solution
        neighbor[i] = 1 - neighbor[i]
        neighbors.append(neighbor) # Creates a list of 4 neighbors with toogled bits
    return neighbors

# Step 5: Select the Best Neighbor
def select_best_neighbor(neighbors, items, capacity):
    best_value = 0
    best_neighbor = None
    for neighbor in neighbors:
        value = evaluate_solution(neighbor, items, capacity)
        if value > best_value:
            best_value = value
            best_neighbor = neighbor
    return best_neighbor, best_value

# Step 6: Hill Climbing Algorithm
# After the algorithm gets stuck in a local optimuma, it restarts with a new random solution.
def hill_climbing(items, capacity, max_iterations=100, restarts=5):
    best_global_solution = None
    best_global_value = 0
    
    for restart in range(restarts):
        # Start with a new random solution for each restart
        current_solution = random_solution(items)
        current_value = evaluate_solution(current_solution, items, capacity)
        
        # Hill climbing inner loop for each restart
        for iteration in range(max_iterations):
            neighbors = generate_neighbors(current_solution)
            best_neighbor, best_value = select_best_neighbor(neighbors, items, capacity)
            
            # If the best neighbor is better, move to that neighbor
            if best_value > current_value:
                current_solution = best_neighbor
                current_value = best_value
            else:
                # No better neighbors found, stop and restart with a new random solution
                break
        
        # Track the best global solution across all restarts
        if current_value > best_global_value:
            best_global_solution = current_solution
            best_global_value = current_value

    return best_global_solution, best_global_value



best_solution, best_value = hill_climbing(items, knapsack_capacity)
print("Best solution:", best_solution)
print("Best value:", best_value)