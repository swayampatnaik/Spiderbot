
import numpy as np

# Spider configuration
num_joints = 24
num_frames = 300

# Temporary joint angle limits in radians.
# These MUST be checked against the Webots motor limits.
minimum_angle = -1.5
maximum_angle = 1.5


def create_chromosome():

    chromosome = np.random.uniform(
        minimum_angle,
        maximum_angle,
        (num_frames, num_joints)
    )

    return chromosome


def create_population(population_size):

    population = []

    for _ in range(population_size):

        chromosome = create_chromosome()
        population.append(chromosome)

    return population
