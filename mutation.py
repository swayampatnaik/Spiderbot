# import random as rd

# def mutate(chromo):

#    for idx in range(len(chromo)):

#        if rd.random() < 0.3:

#            chromo = chromo[:idx] + [1 - chromo[idx]] + chromo[idx + 1:]

#    return chromo






import numpy as np

# =========================================================
# CHROMOSOME SETTINGS
# =========================================================

num_joints = 24
num_frames = 300
chromosome_size = num_joints * num_frames

# Joint order to match ga_controller.py
# R1, R2, R3, R4, L1, L2, L3, L4
# Each leg: hip, thigh, knee

# Webots motor limits, in radians.
# From Webots, we found out the motor limits.
# Hip_max = 1.571, hip_min = -1.571, thigh_max = 1.571, thigh_min = -1.571, knee_max = 1.00, knee_min = -2.00
# A small margin keeps generated values away from the hard limits.
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


# =========================================================
# CREATE ONE CHROMOSOME
# =========================================================

def create_chromosome():

    chromosome = np.random.uniform(
        low=minimum_angles,
        high=maximum_angles,
        size=(num_frames, num_joints)
    )

    return chromosome


# =========================================================
# CREATE A POPULATION
# =========================================================

def create_population(population_size):

    population = []

    for _ in range(population_size):

        chromosome = create_chromosome()
        population.append(chromosome)

    return population


# =========================================================
# MUTATION FUNCTION
# =========================================================

def mutate(chromosome, mutation_rate=0.3, mutation_strength=0.1):

    # Make a copy so the original chromosome is not changed.
    mutated_chromosome = chromosome.copy()

    # Generate a random number for every joint in every frame.
    # Each value has a 30% chance of being selected for mutation.
    mutation_mask = np.random.random(chromosome.shape) < mutation_rate

    # Generate small random changes to the joint angles.
    # Normal distribution uses 0 as the average change
    # and mutation_strength as the standard deviation.
    random_changes = np.random.normal(
        loc=0,
        scale=mutation_strength,
        size=chromosome.shape
    )

    # Apply changes only to the genes selected by the mutation mask.
    mutated_chromosome = np.where(
        mutation_mask,
        mutated_chromosome + random_changes,
        mutated_chromosome
    )

    # Keep every joint angle within its Webots motor limits.
    # np.clip checks each joint against its own minimum and maximum.
    mutated_chromosome = np.clip(
        mutated_chromosome,
        minimum_angles,
        maximum_angles
    )

    # Return the chromosome after mutation.
    return mutated_chromosome


# =========================================================
# TEST THE MUTATION FUNCTION
# =========================================================

# Create one chromosome.
original_chromosome = create_chromosome()

# Apply mutation to the chromosome.
mutated_chromosome = mutate(original_chromosome)

# Display the results.
print("Original chromosome shape:", original_chromosome.shape)
print("Mutated chromosome shape:", mutated_chromosome.shape)

# Display the first frame before and after mutation.
print("\nOriginal first frame:")
print(original_chromosome[0])

print("\nMutated first frame:")
print(mutated_chromosome[0])

# Count how many joint values have changed.
changed_values = np.sum(original_chromosome != mutated_chromosome)

print("\nNumber of changed joint values:", changed_values)
