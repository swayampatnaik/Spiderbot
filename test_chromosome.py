from chromosome import create_chromosome, create_population

chromosome = create_chromosome()

print("Chromosome:", chromosome)
print("Number of genes:", len(chromosome))

population = create_population(30)

print("Population size:", len(population))