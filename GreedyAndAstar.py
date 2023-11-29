def greedyBestFirstSearch(start_node, stop_node):
    open_set = [(heuristic(start_node), start_node)]
    closed_set = set()
    parents = {start_node: None}
    while open_set:
        _, n = open_set.pop(0)  # Pop the node with the lowest heuristic value
        if n == stop_node or Graph_nodes[n] is None:
            pass
        else:
            for (m, _) in get_neighbors(n):
                if m not in closed_set and m not in [
                        node for (_, node) in open_set
                ]:
                    open_set.append((heuristic(m), m))
                    parents[m] = n
        if n == stop_node:
            path = []
            while n:
                path.append(n)
                n = parents[n]
            path.reverse()
            print('Path found using Greedy Best-First Search: {}'.format(path))
            return path
        closed_set.add(n)
    print('Path does not exist!')
    return None


def aStarAlgo(start_node, stop_node):
    open_set = set([start_node])
    closed_set = set()
    g = {start_node: 0}
    parents = {start_node: start_node}
    while len(open_set) > 0:
        n = None
        for v in open_set:
            if n is None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v
        if n == stop_node or Graph_nodes[n] is None:
            pass
        else:
            for (m, weight) in get_neighbors(n):
                if m not in open_set and m not in closed_set:
                    open_set.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n
                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.add(m)
        if n is None:
            print('Path does not exist!')
            return None
        if n == stop_node:
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start_node)
            path.reverse()
            print('Path found using A* Algorithm: {}'.format(path))
            return path
        open_set.remove(n)
        closed_set.add(n)
    print('Path does not exist!')
    return None


def get_neighbors(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        return None


def heuristic(n):
    H_dist = {
        'A': 11,
        'B': 6,
        'C': 99,
        'D': 1,
        'E': 7,
        'G': 0,
    }
    return H_dist[n]


Graph_nodes = {
    'A': [('B', 2), ('E', 3)],
    'B': [('C', 1), ('G', 9)],
    'C': None,
    'E': [('D', 6)],
    'D': [('G', 1)],
}
while True:
    algorithm_choice = int(
        input(
            "Choose an algorithm:\n1. Greedy Best-First Search\n2. A* Algorithm\n3. Exit\n"
        ))
    if algorithm_choice == 1:
        start_node = input("Enter the start node: ")
        stop_node = input("Enter the stop node: ")
        greedyBestFirstSearch(start_node, stop_node)
    elif algorithm_choice == 2:
        start_node = input("Enter the start node: ")
        stop_node = input("Enter the stop node: ")
        aStarAlgo(start_node, stop_node)
    elif algorithm_choice == 3:
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please select 1, 2, or 3.")