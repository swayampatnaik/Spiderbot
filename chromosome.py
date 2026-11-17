import numpy as np


num_joints = 24
num_frames = 300
chromosome_size = num_joints * num_frames

# Joint order to match ga_controller.py
# R1, R2, R3, R4, L1, L2, L3, L4
# Each leg: hip, thigh, knee

# Webots motor limits, in radians.
# From Webots, we found out the motor limits. 
# Hip_max = 1.571, hip_min = -1.571, thigh_max = 1.571, thigh_min = -1.571, knee_max = 1.00, knee_min = -2.00
hip_min = -1.571
hip_max = 1.571

thigh_min = -1.571
thigh_max = 1.571

knee_min = -2.000
knee_max = 1.000

# Repeat the three joint limits for all eight legs.
minimum_angles = np.array(
    [hip_min, thigh_min, knee_min] * 8
)

maximum_angles = np.array(
    [hip_max, thigh_max, knee_max] * 8
)



# CREATE ONE CHROMOSOME

def create_chromosome():

    chromosome = np.random.uniform(
        low=minimum_angles,
        high=maximum_angles,
        size=(num_frames, num_joints)
    )

    return chromosome



# CREATE A POPULATION

def create_population(population_size):

    population = []

    for _ in range(population_size):

        chromosome = create_chromosome()
        population.append(chromosome)

    return population