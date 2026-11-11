import numpy as np

num_frames = 300
num_joints = 24

def generate_gait(chromosome):
    """
    Convert a chromosome into a complete gait sequence for the spider.

    Each chromosome contains:
    -24 offsets
    -24 amplitudes
    -24 phases

    Return:
    - An array containing 300 poses
    - Each pose to have 24 joint angles
    """
    offsets = chromosome[:num_joints]
    amplitudes = chromosome[num_joints:2*num_joints]
    phases = chromosome[2*num_joints:]

    "Store all the generated poses"
    gait = []

    "Generate one pose for every frame"
    for frame in range(num_frames):

        "Calculate the position in the cycle"
        t = 2 * np.pi * frame / num_frames
        

        "Calculate the 24 joint angles for the current frame"
        angles = offsets + amplitudes * np.sin(t + phases)

        "Add the generated pose to the gait"
        gait.append(angles)

    "Return the complete gait sequence"
    return np.array(gait)

