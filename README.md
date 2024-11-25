
---

# **Genetic Algorithm for Traveling Salesman Problem (TSP)**


## **Overview**

The **Genetic Algorithm for TSP** is an implementation of a **genetic algorithm** (GA) used to solve the **Traveling Salesman Problem (TSP)**. The TSP is a classical optimization problem that requires finding the shortest possible route that visits each city once and returns to the starting city. Given its NP-hard nature, the TSP is computationally expensive to solve for large numbers of cities using exact methods. Genetic algorithms offer an efficient heuristic approach to finding near-optimal solutions.

In this project, evolutionary principles (selection, crossover, mutation, and elitism) are applied to evolve solutions over successive generations. The algorithm iteratively refines a population of candidate solutions to discover shorter and more efficient routes.

## **Features**

- **Random City Distance Generation:** Cities and distances are dynamically generated, though you can also input a custom distance matrix.
- **Population Initialization:** The population starts with random routes and evolves using the genetic algorithm techniques.
- **Selection Process:** Roulette wheel selection is used to give higher fitness individuals a better chance of being selected as parents.
- **Crossover (Order Crossover - OX):** The crossover process preserves the order of cities between parent routes.
- **Mutation (Random Swap):** Mutation introduces variability by swapping two cities in a route.
- **Fitness Evaluation:** Fitness is based on the total travel distance; shorter routes have higher fitness scores.
- **Termination and Solution Extraction:** The algorithm runs for a set number of generations or until convergence, then returns the best route found.

## **Installation**

To set up and run the project, follow the steps below.

### 1. **Clone the Repository**

```bash
git clone https://github.com/Bushra-Butt-17/GENETIC-ALGORITHM-TSP.git
cd GENETIC-ALGORITHM-TSP
```

### 2. **Install Dependencies**

This project requires Python 3.x and the `numpy` package. You can install the required dependencies by running:

```bash
pip install numpy
```

### 3. **Run the Algorithm**

Once the dependencies are installed, you can run the algorithm by executing the `genetic_algorithm.py` script.

```bash
python genetic_algorithm.py
```

## **Usage**

### Example Code:

Below is an example of how to use the `genetic_algorithm.py` script to find the best route for a given set of cities.

```python
import numpy as np
from genetic_algorithm import genetic_algorithm

# Example data
city_names = ["A", "B", "C", "D", "E", "F"]
population_size = 50
generations = 1000

# Example distance matrix (distance between cities)
distance_matrix = np.array([
    [0, 10, 15, 20, 25, 30],
    [10, 0, 35, 25, 30, 35],
    [15, 35, 0, 30, 20, 40],
    [20, 25, 30, 0, 10, 15],
    [25, 30, 20, 10, 0, 5],
    [30, 35, 40, 15, 5, 0]
])

# Run genetic algorithm
best_route, best_distance = genetic_algorithm(city_names, population_size, generations, distance_matrix)

# Output results
print("Best Route:", best_route)
print("Best Distance:", best_distance)
```

### Example Output:

```bash
Best Route: ['A', 'C', 'F', 'E', 'D', 'B']
Best Distance: 120
```

## **Algorithm Explanation**

### **1. Initialization**

The algorithm begins by creating an initial population of potential solutions. Each solution is a permutation of the cities. This represents a potential route for the salesman. The population is typically large to ensure diversity.

- Example: If there are 6 cities, an individual could represent a route like `[2, 0, 3, 5, 1, 4]`.

### **2. Fitness Evaluation**

The fitness of each individual in the population is calculated by determining the total distance traveled in its route. The total distance for a route is the sum of the distances between successive cities, plus the distance from the last city back to the first city.

- **Fitness Function:** 
  \[
  \text{Fitness} = \frac{1}{\text{Total Distance of the Route}}
  \]
  A lower distance corresponds to a higher fitness value.

### **3. Selection**

In the selection step, individuals are chosen based on their fitness. The better an individual performs, the higher the chance it has of being selected. In this implementation, **roulette wheel selection** is used, where the probability of selecting an individual is proportional to its fitness.

- **Roulette Wheel Selection:** Individuals with shorter routes (higher fitness) have a better chance of being selected.

### **4. Crossover (Order Crossover - OX)**

Once parents are selected, the crossover operator combines parts of two parents to produce offspring. The **Order Crossover (OX)** method is used, which preserves the order of cities in the parent routes.

- The process involves selecting a subset of cities from one parent and then filling the remaining cities in the order they appear in the second parent.

### **5. Mutation**

Mutation occurs by randomly swapping two cities in a route. This introduces variability and helps to explore the solution space more thoroughly. Without mutation, the algorithm might get stuck in local optima.

### **6. Replacement**

The current population is updated by replacing part of the population with the newly created offspring. This can be done using **elitism**, which keeps the best individuals, or by replacing the entire population.

### **7. Termination**

The algorithm terminates after a specified number of generations. You can also stop the algorithm if the fitness converges or if a satisfactory solution is found.

### **8. Solution Extraction**

At the end of the algorithm, the best solution found is the route with the shortest total distance. This is the approximate solution to the TSP.

## **Customization**

### **Parameters You Can Customize:**

- **`city_names`**: List of cities involved in the TSP.
  - Example: `["A", "B", "C", "D", "E", "F"]`
- **`population_size`**: Number of individuals in the population.
  - Example: `50`
- **`generations`**: Number of generations to evolve.
  - Example: `1000`
- **`distance_matrix`**: A 2D array representing the distances between each pair of cities.
  - Example:
    ```python
    np.array([
        [0, 10, 15, 20, 25, 30],
        [10, 0, 35, 25, 30, 35],
        [15, 35, 0, 30, 20, 40],
        [20, 25, 30, 0, 10, 15],
        [25, 30, 20, 10, 0, 5],
        [30, 35, 40, 15, 5, 0]
    ])
    ```

### **Experimenting with Other Selection Methods**

You can implement different selection methods, such as **Tournament Selection** or **Stochastic Universal Sampling (SUS)**, to experiment with different ways of selecting parents.

### **Adjusting Mutation Rate**

If you want to modify how often mutation occurs, you can introduce a mutation rate (probability of mutation per offspring) and adjust it to maintain a balance between exploration and exploitation.

## **Contributing**

We welcome contributions to improve the algorithm or add new features. If you have any ideas, feel free to open an issue or submit a pull request.

### **Steps to Contribute:**

1. Fork the repository.
2. Clone your fork locally.
3. Create a new branch (`git checkout -b feature-branch`).
4. Make your changes and commit them.
5. Push to your fork and create a pull request.

## **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
