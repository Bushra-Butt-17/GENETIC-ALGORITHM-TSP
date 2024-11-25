import numpy as np


def generate_random_distance_matrix(num_cities):
    return np.random.randint(1, 100, size=(num_cities, num_cities))


# Function to calculate the total distance of a route
def calculate_total_distance(route, distance_matrix):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += distance_matrix[route[i]][route[i + 1]]
    total_distance += distance_matrix[route[-1]][
        route[0]
    ]  # Returning to the starting city
    return total_distance


# Function to perform Order Crossover (OX)
def order_crossover(parent1, parent2):
    # Randomly selecting two crossover points
    point1, point2 = sorted(np.random.choice(len(parent1), 2, replace=False))

    # Creating offspring using genetic material from parents
    offspring = [-1] * len(parent1)
    offspring[point1 : point2 + 1] = parent1[point1 : point2 + 1]
    remaining_cities = [city for city in parent2 if city not in offspring]

    # Filling in the remaining cities in cyclic order from the second parent
    remaining_index = 0
    for i in range(len(offspring)):
        if offspring[i] == -1:
            offspring[i] = remaining_cities[remaining_index]
            remaining_index += 1
    return offspring


# Function to perform mutation (swaping two cities)
def mutate(route):
    mutation_point1, mutation_point2 = np.random.choice(len(route), 2, replace=False)
    route[mutation_point1], route[mutation_point2] = (
        route[mutation_point2],
        route[mutation_point1],
    )
    return route


# Function to convert city names to indices and vice versa
def create_city_mapping(city_names):
    city_to_index = {city: i for i, city in enumerate(city_names)}
    index_to_city = {i: city for i, city in enumerate(city_names)}
    return city_to_index, index_to_city


# Genetic Algorithm function
def genetic_algorithm(city_names, population_size, generations, distance_matrix):
    num_cities = len(city_names)
    city_to_index, index_to_city = create_city_mapping(city_names)

    # Initialize the population
    population = [
        list(np.random.permutation(num_cities)) for _ in range(population_size)
    ]

    for generation in range(generations):
        # Calculate fitness for each individual in the population
        fitness_values = [
            1 / calculate_total_distance(route, distance_matrix) for route in population
        ]

        # Select parents based on fitness (roulette wheel selection)
        selected_parents = np.random.choice(
            population_size,
            size=(population_size // 2, 2),
            p=fitness_values / np.sum(fitness_values),
        )

        # Create offspring using crossover
        offspring = [
            order_crossover(population[parent1], population[parent2])
            for parent1, parent2 in selected_parents
        ]

        # Perform mutation on offspring
        mutated_offspring = [mutate(route) for route in offspring]

        # Replacing the old population with the combined offspring
        population[: population_size // 2] = offspring
        population[population_size // 2 :] = mutated_offspring
    # Finding the best route in the final population
    best_route_index = np.argmax(
        [calculate_total_distance(route, distance_matrix) for route in population]
    )
    best_route = population[best_route_index]

    # Converting indices back to city names
    best_route_names = [index_to_city[index] for index in best_route]

    return best_route_names, calculate_total_distance(best_route, distance_matrix)


if __name__ == "__main__":
    city_names = ["A", "B", "C", "D", "E", "F"]
    population_size = 50
    generations = 1000

    # Example distance matrix
    distance_matrix = np.array(
        [
            [0, 10, 15, 20, 25, 30],
            [10, 0, 35, 25, 30, 35],
            [15, 35, 0, 30, 20, 40],
            [20, 25, 30, 0, 10, 15],
            [25, 30, 20, 10, 0, 5],
            [30, 35, 40, 15, 5, 0],
        ]
    )
    # distance_matrix = generate_random_distance_matrix(len(city_names))

    best_route, best_distance = genetic_algorithm(
        city_names, population_size, generations, distance_matrix
    )
    print("Best Route:", best_route)
    print("Best Distance:", best_distance)
