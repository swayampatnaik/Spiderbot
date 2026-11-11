import numpy as np

num_joints = 24

"""
For each joint, we have 3 parameters: offset, amplitude, and phase. This makes the total chromosome sizeequal to 
3 times the number of joints.
"""
chromosome_size = num_joints * 3

"""
Offset is the base position of the joint, amplitude is how much it moves from that base position, and phase is 
the starting point of the movement in its cycle.
"""
offset_range = (-0.5, 0.5)
amplitude_range = (0.0, 0.5)
phase_range = (0.0, 2 * np.pi)


def create_chromosome():
    """
    Creates a random chromosome with parameters for each joint.
    Each joint has an offset, amplitude, and phase.
    """

    offsets = np.random.uniform(offset_range[0], offset_range[1], num_joints)

    amplitudes = np.random.uniform(amplitude_range[0], amplitude_range[1], num_joints)

    phases = np.random.uniform(phase_range[0], phase_range[1], num_joints)


    chromosome = np.concatenate([offsets, amplitudes, phases])

    return chromosome


def create_population(population_size):

    population = []

    for _ in range(population_size):
        chromosome = create_chromosome()
        population.append(chromosome)

    return population