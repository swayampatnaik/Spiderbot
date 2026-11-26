
import os
import csv
import matplotlib.pyplot as plt


# FIND THE LATEST EXPERIMENT

current_folder = os.path.dirname(os.path.abspath(__file__))
results_folder = os.path.join(current_folder, "results")

experiments = [
    folder for folder in os.listdir(results_folder)
    if folder.startswith("experiment_")
    and os.path.isdir(os.path.join(results_folder, folder))
]

if not experiments:
    raise FileNotFoundError("No experiment folders found.")

latest_experiment = sorted(experiments)[-1]

experiment_folder = os.path.join(results_folder, latest_experiment)

statistics_file = os.path.join(
    experiment_folder,
    "generation_statistics.csv"
)


# READ GENERATION STATISTICS

generations = []
best_fitness = []
average_fitness = []
worst_fitness = []

with open(statistics_file, "r", newline="") as file:

    reader = csv.DictReader(file)

    for row in reader:

        generations.append(int(row["generation"]))
        best_fitness.append(float(row["best_fitness"]))
        average_fitness.append(float(row["average_fitness"]))
        worst_fitness.append(float(row["worst_fitness"]))


# PLOT FITNESS AGAINST GENERATION

plt.figure(figsize=(10, 6))

plt.plot(
    generations,
    best_fitness,
    marker="o",
    label="Best Fitness"
)

plt.plot(
    generations,
    average_fitness,
    marker="o",
    label="Average Fitness"
)

plt.plot(
    generations,
    worst_fitness,
    marker="o",
    label="Worst Fitness"
)

plt.xlabel("Generation")
plt.ylabel("Fitness (metres)")
plt.title("Genetic Algorithm Fitness Progression")

plt.xticks(generations)
plt.grid(True)
plt.legend()

plt.tight_layout()

# Save the graph in the experiment folder.
graph_file = os.path.join(
    experiment_folder,
    "fitness_progression.png"
)

plt.savefig(graph_file, dpi=300)

print("Graph saved to:", graph_file)

plt.show()
