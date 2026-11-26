
import os
import csv
import numpy as np
import time

from fitness import calculate_fitness


# FILE PATHS

current_folder = os.path.dirname(os.path.abspath(__file__))

project_folder = os.path.dirname(current_folder)

controller_folder = os.path.join(project_folder, "Spider_world_demo", "controllers", "ga_controller")

gait_file = os.path.join(controller_folder, "gait.csv")

result_file = os.path.join(controller_folder, "evaluation_result.csv")

status_file = os.path.join(controller_folder, "status.txt")

run_request_file = os.path.join(controller_folder, "run_request.txt")



# SAVE CHROMOSOME AS GAIT CSV

def save_gait(chromosome):

    # Save one chromosome to gait.csv. Each row represents one pose andcontains 24 joint angles.

    with open(gait_file, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerows(chromosome)

    print("Gait saved to:", gait_file)



# READ WEBOTS GPS RESULTS

def read_evaluation_result():

    # Read starting and ending GPS coordinates from evaluation_result.csv.

    with open(result_file, "r", newline="") as file:

        reader = csv.DictReader(file)

        row = next(reader)

    start_position = np.array([
        float(row["start_x"]),
        float(row["start_y"]),
        float(row["start_z"])
    ])

    end_position = np.array([
        float(row["end_x"]),
        float(row["end_y"]),
        float(row["end_z"])
    ])

    return start_position, end_position


# EVALUATE ONE CHROMOSOME


def evaluate_chromosome(chromosome):

    # Remove results and status from the previous evaluation.
    if os.path.exists(result_file):
        os.remove(result_file)

    if os.path.exists(status_file):
        os.remove(status_file)

    # Save the chromosome for Webots.
    save_gait(chromosome)

    # Tell Webots that a new chromosome is ready.
    with open(run_request_file, "w") as file:
        file.write("run")

    print("\nCHROMOSOME SENT TO WEBOTS")
    print("Waiting for evaluation to finish...")

    # Wait for Webots to finish.
    timeout = 300
    start_time = time.monotonic()

    while True:

        if os.path.exists(status_file):

            with open(status_file, "r") as file:
                status = file.read().strip()

            if status == "finished":
                break

        if time.monotonic() - start_time > timeout:
            raise TimeoutError(
                "Webots did not finish evaluating the chromosome."
            )

        time.sleep(0.1)

    # Read the GPS results.
    start_position, end_position = read_evaluation_result()

    # Calculate fitness.
    fitness = calculate_fitness(start_position, end_position)

    print("\nCHROMOSOME EVALUATION COMPLETED")
    print("Starting position:", start_position)
    print("Ending position:", end_position)
    print("Fitness:", fitness)

    return fitness





# EVALUATE ENTIRE POPULATION

def evaluate_population(population):

    # Evaluate every chromosome in the population. Returns an array containing one fitness score for every chromosome.

    fitness_scores = []

    total_chromosomes = len(population)

    print("\nEVALUATING POPULATION")

    print("Population size:", total_chromosomes)


    # EVALUATE CHROMOSOMES ONE AT A TIME

    for i, chromosome in enumerate(population):

        print("\n----------------------------------------------")

        print(
            "Evaluating chromosome:",
            i + 1,
            "of",
            total_chromosomes
        )

        fitness = evaluate_chromosome(chromosome)

        fitness_scores.append(fitness)


    # RETURN FITNESS SCORES

    fitness_scores = np.array(fitness_scores)

    print("\nPOPULATION EVALUATION COMPLETED")

    print("Number of fitness scores:", len(fitness_scores))

    return fitness_scores
