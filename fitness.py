
import math


def calculate_fitness(start_position, end_position):
    """
    Calculate horizontal distance travelled by the spider.

    Parameters:
        start_position: GPS coordinates at the start (X, Y, Z).
        end_position: GPS coordinates at the end (X, Y, Z).

    Returns:
        Horizontal distance between the two positions.
    """

    change_x = end_position[0] - start_position[0]
    change_y = end_position[1] - start_position[1]

    fitness = math.sqrt(change_x ** 2 + change_y ** 2)

    return fitness
