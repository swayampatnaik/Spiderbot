import numpy as np

from chromosome import create_chromosome
from gait_generator import generate_gait

chromosome = create_chromosome()
gait = generate_gait(chromosome)

np.savetxt("gait.csv", gait, delimiter=",")

print("Gait generated and saved to gait.csv")
print("Gait shape:", gait.shape)