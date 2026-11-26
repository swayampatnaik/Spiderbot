
## Chromosome Representation

- A chromosome represents one complete walking gait for one candidate.
- A gait is represented as a 300-frame chromosome.
- Each frame contains 24 joint angles: 8 legs x 3 joints.
- The robot has eight legs: R1, R2, R3, R4, L1, L2, L3, and L4.
- Each leg has a hip, thigh, and knee joint.
- Therefore, one chromosome contains 300 x 24 = 7200 values
- The chromosome NumPy shape is `(300, 24)`,
- Joint angles are stored in radians.
- The population is a collection of several complete gait candidates

## Motor Limits

- Uses Webots motor limits, in radians.
- Hip: `-1.571` to `1.571`
- Thigh: `-1.571` to `1.571`
- Knee: `-2.000` to `1.000`

## Chromosome Functions

- `create_chromosome()` generates one random gait.
- Joint values are generated within the motor limits.
- `create_population(population_size)` generates multiple chromosomes for the genetic algorithm.



## Population and Evaluation

- Starts with a population of 700 random chromosomes.
- Evaluates each chromosome and gives it a fitness score based on how far the spider moves.
- Each candidate currently needs to be run manually in Webots for evaluation.

## Selection, Crossover, and Mutation

- Selects parents by randomly choosing 3 candidates and keeping the one with the highest fitness.
- Combines pairs of parents using crossover, which happens 80% of the time.
- Randomly mutates some joint angles and keeps them within the motor limits.

## Generations

- Repeats the process for the configured number of generations.
- Creates a new population of 700 candidates for each generation.

## Saved Results

- Saves each generation's population and fitness scores, plus fitness statistics.
- Saves the best chromosome from each generation as a separate CSV file.

 