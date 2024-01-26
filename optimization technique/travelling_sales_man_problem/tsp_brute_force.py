# Import necessary modules
from sys import maxsize
from itertools import permutations

# Function to solve the Traveling Salesman Problem using a naive approach
def tsp(graph, S):
    # Determine the number of vertices in the graph
    V = len(graph)
    
    # Create a list of vertices excluding the source vertex
    vertex = [i for i in range(V) if i != S]
    
    # Generate all possible permutations of the vertices (excluding the source vertex)
    next_vertex = permutations(vertex)
    
    # Initialize the minimum path cost to the maximum possible integer value
    min_path_cost = maxsize

    # Iterate through all permutations of the vertices
    for i in next_vertex:
        current_path_cost = 0
        k = S
        
        # Calculate the total cost (distance) of the current path
        for j in i:
            current_path_cost += graph[k][j]
            k = j
        current_path_cost += graph[k][S]

        # Update the minimum path cost if the current path cost is smaller
        min_path_cost = min(min_path_cost, current_path_cost)

    # Return the minimum path cost
    return min_path_cost

# Main section
if __name__ == "__main__":
    # Example graph represented as an adjacency matrix
    graph = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    
    # Source vertex (starting city)
    source_vertex = 0  

    # Compute the minimum path cost using the TSP function
    min_path_cost = tsp(graph, source_vertex)

    # Print the minimum path cost
    print("Minimum path cost:", min_path_cost)
