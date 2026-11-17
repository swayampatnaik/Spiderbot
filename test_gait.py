
import numpy as np

from chromosome import create_chromosome
from gait_generator import generate_gait


# Create a random chromosome
chromosome = create_chromosome()

# Generate gait
gait = generate_gait(chromosome)

# Save gait to CSV
np.savetxt(
    "gait.csv",
    gait,
    delimiter=","
)


# Display results
print("Random gait generated successfully!")

print("Chromosome shape:", chromosome.shape)

print("Gait shape:", gait.shape)

print("Total genes:", chromosome.size)

print("First pose:")
print(gait[0])

print("Last pose:")
print(gait[-1])
