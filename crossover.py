import numpy as np

def crossover(parent1, parent2):

    child1 = parent1.copy()
    child2 = parent2.copy()

    # Select a random crossover point
    # There are 8 legs, each with 3 angles

    crossover_point = np.random.randint(1, 8)

    # Convert leg position into gene position

    gene_point = crossover_point * 3

    # Exchange chromosome sections

    child1[:gene_point] = parent1[:gene_point]
    child1[gene_point:] = parent2[gene_point:]

    child2[:gene_point] = parent2[:gene_point]
    child2[gene_point:] = parent1[gene_point:]

    return child1, child2