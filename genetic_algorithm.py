import os
import csv
import numpy as np

from chromosome import (create_population, minimum_angles, maximum_angles)


#PARAMETERS

POPULATION_SIZE = 700
#NUM_GENERATIONS = ??

#SELECTION PARAMETERS
#TOURNAMENT_SIZE = ??

#CROSSOVER PARAMETERS
#CROSSOVER_RATE = ??

#MUTATION PARAMETERS
#MUTATION_RATE = ??
#MUTATION_STRENGTH = ??


#SELECTION FUNCTION

def selection():
    #TO BE IMPLEMENTED

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
    
    new_population = []
    #To be implemented




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


