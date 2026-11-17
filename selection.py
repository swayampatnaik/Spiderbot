
import random


def roulette_wheel_selection(population, fitness_scores):
    """
    Selects one individual from the population using roulette wheel selection.

    Individuals with higher fitness scores have a greater probability
    of being selected.
    """

    # Step 1: Add together all fitness scores
    total_fitness = sum(fitness_scores)

    # Make sure fitness scores are valid
    if total_fitness <= 0 or any(score < 0 for score in fitness_scores):
        raise ValueError("Fitness scores must be non-negative and have a positive total.")

    if len(population) != len(fitness_scores):
        raise ValueError("Population and fitness scores must have equal lengths.")

    # Step 2: Generate a random number between 0 and the total fitness
    random_number = random.uniform(0, total_fitness)

    # Step 3: Work through the population, adding fitness scores
    cumulative_fitness = 0

    for individual, fitness in zip(population, fitness_scores):

        cumulative_fitness += fitness

        # Step 4: Select the individual when the random number
        # falls within its section of the roulette wheel
        if random_number <= cumulative_fitness:
            return individual

    # Fallback for floating-point rounding
    return population[-1]
