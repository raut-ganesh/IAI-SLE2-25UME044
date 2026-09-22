import timeit
from collections import deque
import networkx as nx
import matplotlib.pyplot as plt


# =========================================================
# CREATE BINARY TREE
# =========================================================

graph = {}
total_nodes = 16383

for i in range(total_nodes):

    children = []

    left_child = 2 * i + 1
    right_child = 2 * i + 2

    if left_child < total_nodes:
        children.append(left_child)

    if right_child < total_nodes:
        children.append(right_child)

    graph[i] = children


# =========================================================
# BFS - BREADTH FIRST SEARCH
# =========================================================

def bfs(graph, start, goal):

    queue = deque([start])
    visited = {start}
    parent = {start: None}
    nodes_expanded = 0

    while queue:

        current = queue.popleft()
        nodes_expanded += 1

        if current == goal:

            path = []

            while current is not None:
                path.append(current)
                current = parent[current]

            return nodes_expanded, path[::-1]

        for neighbor in graph[current]:

            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)

    return nodes_expanded, []


# =========================================================
# DFS - DEPTH FIRST SEARCH
# =========================================================

def dfs(graph, start, goal):

    stack = [start]
    visited = {start}
    parent = {start: None}
    nodes_expanded = 0

    while stack:

        current = stack.pop()
        nodes_expanded += 1

        if current == goal:

            path = []

            while current is not None:
                path.append(current)
                current = parent[current]

            return nodes_expanded, path[::-1]

        for neighbor in reversed(graph[current]):

            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                stack.append(neighbor)

    return nodes_expanded, []


# =========================================================
# START AND GOAL
# =========================================================

start_node = 0
goal_node = 15000


# Run BFS and DFS
bfs_nodes, bfs_path = bfs(graph, start_node, goal_node)
dfs_nodes, dfs_path = dfs(graph, start_node, goal_node)


# =========================================================
# MEASURE EXECUTION TIME
# =========================================================

number_of_runs = 100

bfs_total_time = timeit.timeit(
    lambda: bfs(graph, start_node, goal_node),
    number=number_of_runs
)

dfs_total_time = timeit.timeit(
    lambda: dfs(graph, start_node, goal_node),
    number=number_of_runs
)


# Average time in milliseconds
bfs_average = (bfs_total_time / number_of_runs) * 1000
dfs_average = (dfs_total_time / number_of_runs) * 1000


# =========================================================
# DISPLAY RESULTS
# =========================================================

print("======================================")
print("          BFS AND DFS RESULTS")
print("======================================")

print("Start Node:", start_node)
print("Goal Node :", goal_node)

print("\nBFS Nodes Expanded:", bfs_nodes)
print("BFS Average Time:", bfs_average, "ms")

print("\nDFS Nodes Expanded:", dfs_nodes)
print("DFS Average Time:", dfs_average, "ms")

print("\nBFS Path:")
print(bfs_path)

print("\nDFS Path:")
print(dfs_path)


# =========================================================
# VISUALIZE THE TREE
# =========================================================

visible_nodes = 31

tree_graph = nx.DiGraph()

for node in range(visible_nodes):

    for child in graph[node]:

        if child < visible_nodes:
            tree_graph.add_edge(node, child)


# =========================================================
# CREATE TREE POSITIONS
# =========================================================

positions = {}

for level in range(5):

    first_node = 2 ** level - 1
    last_node = 2 ** (level + 1) - 2

    nodes_in_level = last_node - first_node + 1

    for index, node in enumerate(
        range(first_node, last_node + 1)
    ):

        x = (index + 1) / (nodes_in_level + 1)
        y = -level

        positions[node] = (x, y)


# =========================================================
# DRAW GRAPH
# =========================================================

plt.figure(figsize=(14, 8))

nx.draw(
    tree_graph,
    positions,
    with_labels=True,
    node_size=900,
    font_size=9,
    arrows=True
)


# =========================================================
# HIGHLIGHT BFS PATH
# =========================================================

bfs_edges = []

for i in range(len(bfs_path) - 1):

    first = bfs_path[i]
    second = bfs_path[i + 1]

    if first < visible_nodes and second < visible_nodes:
        bfs_edges.append((first, second))


nx.draw_networkx_edges(
    tree_graph,
    positions,
    edgelist=bfs_edges,
    width=3
)


# =========================================================
# FINAL DISPLAY
# =========================================================

plt.title(
    "Binary Tree Graph - BFS and DFS\n"
    "First 31 Nodes of 16,383 Node Graph"
)

plt.axis("off")
plt.tight_layout()
plt.show()
