
import numpy as np

num_frames = 300
num_joints = 24


def generate_gait(chromosome):

    if chromosome.shape != (num_frames, num_joints):

        raise ValueError(
            "Chromosome must contain 300 poses and 24 joint angles per pose."
        )

    return chromosome
