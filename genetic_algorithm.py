import os
import csv
import numpy as np

from chromosome import (create_population, minimum_angles, maximum_angles)


#PARAMETERS

POPULATION_SIZE = 700
#NUM_GENERATIONS = 10

#SELECTION PARAMETERS
#TOURNAMENT_SIZE = 3

#CROSSOVER PARAMETERS
#CROSSOVER_RATE = 0.8

#MUTATION PARAMETERS
#MUTATION_RATE = 0.001
#MUTATION_STRENGTH = 0.1


#RESULTS FOLDER PATH

current_folder = os.path.dirname(os.path.abspath(__file__))

results_folder = os.path.join(current_folder, "results")



#SELECTION FUNCTION

def selection():

    #Tournament selection.
    #Randomly selects three chromosomes and returnsthe one with the highest fitness.

    contestants = np.random.choice(len(population), size=TOURNAMENT_SIZE, replace=False)

    best_contestant = contestants[np.argmax(fitness_scores[contestants])]

    return population[best_contestant].copy()


#CROSSOVER FUNCTION

def crossover(parent1, parent2):

    if np.random.random() > CROSSOVER_RATE:
        return parent1.copy(), parent2.copy()

    # generate a random mask for crossover   
    mask = np.random.random(parent1.shape) < 0.5

    # creating 2 offspring by swapping genes based on the mask
    child1 = np.where(mask, parent1, parent2)
    child2 = np.where(mask, parent2, parent1)

    return child1, child2



#MUTATION FUNCTION

def mutate(chromosome):

    # Make a copy so the original chromosome is not changed.
    mutated_chromosome = chromosome.copy()

    # Generate a random number for every joint in every frame.
    # Each value has a 30% chance of being selected for mutation.
    mutation_mask = np.random.random(chromosome.shape) < MUTATION_RATE

    # Generate small random changes to the joint angles.
    # Normal distribution uses 0 as the average change
    # and mutation_strength as the standard deviation.
    random_changes = np.random.normal(
        loc=0,
        scale=MUTATION_STRENGTH,
        size=chromosome.shape
    )

    # Apply changes only to the genes selected by the mutation mask.
    mutated_chromosome[mutation_mask] += random_changes[mutation_mask]

    # Keep every joint angle within its Webots motor limits.
    # np.clip checks each joint against its own minimum and maximum.
    mutated_chromosome = np.clip(
        mutated_chromosome,
        minimum_angles,
        maximum_angles
    )

    # Return the chromosome after mutation.
    return mutated_chromosome



#NEXT GENERATION FUNCTION

def create_next_generation(population, fitness_scores):
    
    #Create a new population using:

    #1. Tournament selection
    #2. Crossover
    #3. Mutation

    #The population size remains unchanged.

    new_population = []
    
    
    #GENERATE OFFSPRING
    while len(new_population) < POPULATION_SIZE:

        # Select two parents.
        parent1 = selection(population, fitness_scores)

        parent2 = selection(population, fitness_scores)

        # Produce two offspring.
        child1, child2 = crossover(parent1, parent2)

        # Mutate the offspring.
        child1 = mutation(child1)

        child2 = mutation(child2)

        # Add offspring to the new population.
        new_population.append(child1)

        if len(new_population) < POPULATION_SIZE:

            new_population.append(child2)

    return np.array(new_population)




#FUNCTION TO SAVE GENERATION RESULTS

def save_generation(generation, population, fitness_scores):
    # Save the population and fitness scores to a CSV file



#MAIN GENETIC ALGORITHM FUNCTION/LOOP

def genetic_algorithm():
    print("Starting Genetic Algorithm...")

    population = create_population(POPULATION_SIZE)

    print("Population created with size:", len(population))
    print("Chromosome shape:", population[0].shape)


    #main loop
    for generation in range(NUM_GENERATIONS + 1):
    #To be implemented


