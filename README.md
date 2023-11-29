# Pathfinding Algorithms

This Python script implements two pathfinding algorithms, Greedy Best-First Search and A* Algorithm, to find the shortest path between two nodes in a graph.

## Algorithms

1. **Greedy Best-First Search:**
   - Uses a heuristic function to estimate the cost of reaching the goal from a given node.
   - Expands nodes based on their heuristic values, prioritizing nodes that seem closer to the goal.
   - Outputs the path found using this approach.

2. **A* Algorithm:**
   - Combines the cost to reach a node from the start (g-value) and the estimated cost to reach the goal from that node (heuristic).
   - Expands nodes based on the sum of g-value and heuristic, favoring nodes with lower total costs.
   - Outputs the path found using this approach.

## Graph Representation

The graph is represented as a dictionary (`Graph_nodes`) where each node is a key, and the associated value is a list of neighbors with their corresponding weights.

## Heuristic Function

A heuristic function (`heuristic`) is provided to estimate the cost from each node to the goal. This function is specific to the problem being solved and can be adjusted based on the problem domain.

## Usage

1. Choose an algorithm:
   - 1: Greedy Best-First Search
   - 2: A* Algorithm
   - 3: Exit

2. Enter the start and stop nodes when prompted.

3. The program outputs the path found using the chosen algorithm or notifies if the path does not exist.

## Example

```bash
Choose an algorithm:
1. Greedy Best-First Search
2. A* Algorithm
3. Exit
1

Enter the start node: A
Enter the stop node: G

Path found using Greedy Best-First Search: ['A', 'B', 'G']
