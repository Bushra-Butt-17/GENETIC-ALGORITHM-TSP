---

# 🚀 **Genetic Algorithm for Traveling Salesman Problem (TSP)** 🗺️

## **Overview**

The **Genetic Algorithm for TSP** implements an evolutionary approach to solve the **Traveling Salesman Problem (TSP)**, a classic optimization challenge. The goal is to find the shortest route visiting all cities once and returning to the starting point. Given its **NP-hard** nature, exact methods become computationally expensive as the number of cities increases. The **Genetic Algorithm (GA)** provides an efficient heuristic to find near-optimal solutions by mimicking natural selection principles.

Through **selection**, **crossover**, **mutation**, and **elitism**, this project refines potential solutions across generations, yielding shorter and more efficient routes. 🧬

---

## 🌟 **Features**

- 🗺️ **Dynamic Distance Matrix:** Automatically generates random city distances or allows custom input.
- 🧑‍🤝‍🧑 **Population-Based Evolution:** Starts with a population of random routes that evolve using GA techniques.
- 🎯 **Roulette Wheel Selection:** Ensures individuals with higher fitness are more likely to reproduce.
- 🔗 **Order Crossover (OX):** Combines parent routes while maintaining city order.
- 🔄 **Random Mutation:** Introduces diversity by swapping two cities in a route.
- 📉 **Fitness Evaluation:** Uses total route distance, favoring shorter routes.
- 🏁 **Termination Criteria:** Stops after a fixed number of generations or upon convergence.

---

## 💻 **Installation**

Follow these steps to set up and run the project:

### 1. **Clone the Repository**
```bash
git clone https://github.com/Bushra-Butt-17/GENETIC-ALGORITHM-TSP.git
cd GENETIC-ALGORITHM-TSP
```

### 2. **Install Dependencies**
Ensure Python 3.x and `numpy` are installed:
```bash
pip install numpy
```

### 3. **Run the Algorithm**
Execute the script:
```bash
python genetic_algorithm.py
```

---

## ⚙️ **Usage**

### Example Code:

```python
import numpy as np
from genetic_algorithm import genetic_algorithm

# Example data
city_names = ["A", "B", "C", "D", "E", "F"]
population_size = 50
generations = 1000

# Distance matrix (distances between cities)
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
print("🌟 Best Route:", best_route)
print("📏 Best Distance:", best_distance)
```

### Example Output:

```bash
🌟 Best Route: ['A', 'C', 'F', 'E', 'D', 'B']
📏 Best Distance: 120
```

---

## 🔍 **Algorithm Explanation**

### **1. Initialization**
- Generates an initial **population** of random routes (permutations of cities).  
  Example: For 6 cities, a route might look like `[2, 0, 3, 5, 1, 4]`.

### **2. Fitness Evaluation**
- Calculates **fitness** based on the total distance of the route:
  \[
  \text{Fitness} = \frac{1}{\text{Total Distance of the Route}}
  \]
- Shorter routes = Higher fitness! 🚴‍♀️

### **3. Selection**
- Implements **Roulette Wheel Selection** where individuals with better fitness have a higher probability of being selected for reproduction. 🎯

### **4. Crossover (Order Crossover - OX)**
- Combines two parent routes while preserving city order:
  1. Select a subset of cities from one parent.
  2. Fill in the remaining cities in the order they appear in the second parent.

### **5. Mutation**
- Introduces diversity by randomly swapping two cities in a route.  
  Example: `[A, B, C, D, E]` → `[A, E, C, D, B]` 🔄

### **6. Replacement**
- Replaces the current population with the offspring, retaining the **elite** individuals with the best fitness. 👑

### **7. Termination**
- Stops after a fixed number of **generations** or when the solution converges to a satisfactory route.

### **8. Solution Extraction**
- Outputs the best route and its total distance as the solution. ✅

---

## 🔧 **Customization**

### Parameters You Can Adjust:
- 🏙️ **`city_names`:** List of cities (e.g., `["A", "B", "C", "D", "E", "F"]`).
- 👥 **`population_size`:** Number of individuals in the population (e.g., `50`).
- ⏳ **`generations`:** Number of iterations (e.g., `1000`).
- 📊 **`distance_matrix`:** A 2D array with distances between cities.

### Experiment with:
- ⚙️ **Selection Methods:** Try alternatives like **Tournament Selection** or **Stochastic Universal Sampling (SUS)**.
- 🔄 **Mutation Rate:** Adjust the probability of mutation for better exploration/exploitation.

---

## 📂 **File Structure**

```
GENETIC-ALGORITHM-TSP/
│
├── genetic_algorithm.py         # Main script 🧬
├── README.md                    # Project details 📄
└── LICENSE                      # License 📝
```

---

## 🌟 **Features to Add in the Future**

- 🔧 **Hyperparameter Tuning:** Automatically optimize population size, mutation rate, etc.
- 🌲 **Other Algorithms:** Implement alternatives like **Simulated Annealing** or **Ant Colony Optimization**.
- 📈 **Dynamic Visualization:** Animate the evolution of routes over generations.

---

## 🤝 **Contributing**

We welcome contributions to enhance this project! Open an issue or submit a pull request to share your ideas.  

### How to Contribute:
1. Fork the repository.
2. Clone your fork locally:
   ```bash
   git clone https://github.com/your-username/GENETIC-ALGORITHM-TSP.git
   ```
3. Create a new branch:
   ```bash
   git checkout -b feature-branch
   ```
4. Commit your changes and push to your fork.
5. Submit a pull request! 🎉

---

## 🛡️ **License**
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details. 📜

---

🌟 **Let’s optimize the Traveling Salesman Problem together!** 🌟

