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

def mutation(chromosome):

    # Make a copy so the original chromosome is not changed.
    mutated_chromosome = chromosome.copy()

    # Decide which genes will be mutated.
    mutation_mask = np.random.random(chromosome.shape) < MUTATION_RATE

    # Generate small random changes for the selected genes.
    random_changes = np.random.normal(
        loc=0.0,
        scale=MUTATION_STRENGTH,
        size=chromosome.shape
    )

    # Apply changes only to the genes selected.
    mutated_chromosome[mutation_mask] += random_changes[mutation_mask]

    # Keep every joint angle within its Webots motor limits.
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

    generation_file = os.path.join(results_folder, f"generation_{generation:03d}.npz")

    np.savez_compressed(generation_file, chromosomes=population, fitness=fitness_scores)


    # Calculate generation statistics.
    best_fitness = np.max(fitness_scores)

    average_fitness = np.mean(fitness_scores)

    worst_fitness = np.min(fitness_scores)

    fitness_std = np.std(fitness_scores)

    best_index = np.argmax(fitness_scores)

    # Save summary statistics.
    statistics_file = os.path.join(results_folder,"generation_statistics.csv")

    file_exists = os.path.exists(statistics_file)

    with open(statistics_file, "a", newline="") as file:

        writer = csv.writer(file)

        if not file_exists:

            writer.writerow([
                "generation",
                "best_fitness",
                "average_fitness",
                "worst_fitness",
                "fitness_std",
                "best_chromosome_index"
            ])

        writer.writerow([
            generation,
            best_fitness,
            average_fitness,
            worst_fitness,
            fitness_std,
            best_index
        ])

    print("\nGeneration:", generation)
    print("Best fitness:", best_fitness)
    print("Average fitness:", average_fitness)
    print("Worst fitness:", worst_fitness)
    print("Fitness standard deviation:", fitness_std)

    print("Results saved:", generation_file)




#MAIN GENETIC ALGORITHM FUNCTION/LOOP

def genetic_algorithm(evaluate_population):
    print("Starting Genetic Algorithm...")

    print("\nCreating initial population...")

    population = np.array(create_population(POPULATION_SIZE))

    print("Population created with size:", len(population))
    print("Chromosome shape:", population[0].shape)


    #main evaluation loop
    for generation in range(NUM_GENERATIONS + 1):

        print("\nEvaluating generation:", generation)

        # Evaluate the fitness of the population.
        #fitness_scores = evaluate_population(population)

        # Check that every chromosome has a fitness score.
        if fitness_scores.shape != (POPULATION_SIZE,):

            raise ValueError(
                "The evaluator must return exactly "
                f"{POPULATION_SIZE} fitness scores."
            )

        if not np.all(np.isfinite(fitness_scores)):

            raise ValueError(
                "Fitness scores contain invalid values."
            )        

        # Save the current generation's results.
        save_generation(generation, population, fitness_scores)

        # Stop after the final generation has been evaluated.
        if generation == NUM_GENERATIONS:

            break

        # Create the next generation.
        population = create_next_generation(population, fitness_scores)

        print("Next generation created with population size:", len(population))


    print("\nGenetic Algorithm completed.")



if __name__ == "__main__":

    # Run the genetic algorithm with the evaluate_population function.

    run_genetic_algorithm(evaluate_population)