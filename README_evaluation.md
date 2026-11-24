
# Evaluation Function

## Overview

The `evaluation.py` file evaluates the performance of each chromosome using the Webots simulation. It connects the genetic algorithm to the simulation and uses the GPS coordinates of the spider robot to calculate its fitness.

## How It Works

The chromosome is saved into a `gait.csv` file, where each row represents one pose containing 24 joint angles.

The user is then asked to run or restart the Webots simulation, allowing the spider to perform the movement pattern stored in the CSV file.

Once the simulation is completed, the starting and ending GPS coordinates are retrieved from `evaluation_result.csv`. These coordinates are passed into the fitness function to calculate the horizontal distance travelled by the spider.

## Functions

### save_gait(chromosome)

Saves the chromosome into a CSV file so the Webots controller can execute the movement pattern.

### read_evaluation_result()

Reads the starting and ending GPS coordinates from the evaluation result file and returns them as NumPy arrays.

### evaluate_chromosome(chromosome)

Evaluates an individual chromosome by saving its movement pattern, removing previous evaluation results, waiting for the simulation to finish and calculating its fitness value.

A FileNotFoundError is raised if the evaluation result file is not generated.

### evaluate_population(population)

Evaluates each chromosome in the population individually and stores the calculated fitness values in a NumPy array.

## Return Value

The individual chromosome evaluation returns a fitness value that represents the horizontal distance of the spider.

The population evaluation returns a NumPy array containing one fitness value for each chromosome in the population.
