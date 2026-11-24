## Fitness Function

## Overview

The `fitness.py` file is  calculating the fitness of the spider robot based on its horizontal distance travelled. It is used within the genetic algorithm to measure how effectively the robot can move.

## How It Works

The function takes the starting and ending GPS coordinates of the spider and calculates the difference between the X and Y positions.

The horizontal distance is calculated through taking the distance difference between the x and y coordinates

The further away the spider is from the starting position, the higher the fitness function value is


### Return Value

The code returns a fitness value showing the horizontal distance between the starting and ending positions.

