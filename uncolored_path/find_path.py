import numpy as np

def find(adjacency, used_edges, node, path, all_paths):
    nodes_count = adjacency.shape[0]
    neighbors = [
        i
        for i in range(nodes_count)
        if not used_edges[i, node]
           and adjacency[node, i]
           and i != node
    ]

    if not neighbors:
        all_paths.append(path)
        return

    for i in neighbors:
        used_edges[i][node] = True
        used_edges[node][i] = True
        find(adjacency, used_edges, i, path + [i], all_paths)



def find_first_full_path(adjacency: np.ndarray) -> list[int]:
    weight, _ = adjacency.shape
    all_paths = []

    for i in range(weight):
        used_edges = np.zeros((weight, weight), dtype=bool)
        find(adjacency, used_edges.copy(), i, [i], all_paths)

    return all_paths