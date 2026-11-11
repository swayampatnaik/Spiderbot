import numpy as np

from chromosome import create_chromosome
from gait_generator import generate_gait

chromosome = create_chromosome()
gait = generate_gait(chromosome)

np.savetxt("gait.txt", gait, delimiter=",")

print("Gait generated and saved to gait.txt")
print("Gait shape:", gait.shape)