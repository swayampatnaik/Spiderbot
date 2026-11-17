
import math


def calculate_fitness(start_position, end_position):
    """
    Calculate horizontal distance travelled by the spider.

    start_position: [x, y, z] at the start of the gait
    end_position:   [x, y, z] at the end of the gait

    Returns distance in metres.
    """

    start_x = start_position[0]
    start_y = start_position[1]

    end_x = end_position[0]
    end_y = end_position[1]

    distance = math.sqrt((end_x - start_x) ** 2 + (end_y - start_y) ** 2)

    return distance
