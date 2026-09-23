# SLE-2: BFS vs DFS Profiling

**Course:** 02AML204 – Introduction to Artificial Intelligence
**PRN:** 25UME044
**Name:** Ganesh Ujesh Raut
**Division:** A

## About the Project

This project is developed as part of **SLE-2: Profiling Report** for the *Introduction to Artificial Intelligence* course.

The experiment focuses on the practical performance comparison of two uninformed search techniques:

* **Breadth-First Search (BFS)**
* **Depth-First Search (DFS)**

Both algorithms are implemented in Python and evaluated using the same binary-tree graph and search target.

## Objective

The main objectives of this experiment are to:

* Implement BFS and DFS using Python.
* Measure the execution time of both algorithms.
* Track the number of nodes expanded during the search.
* Profile the program using **Py-Spy**.
* Generate flamegraphs for performance visualization.
* Compare the practical behaviour of BFS and DFS.

## Graph Used

A binary-tree graph is used for conducting the experiment.

The graph contains:

* **Vertices (V):** 65,535
* **Edges (E):** 65,534
* **Start Node:** 0
* **Goal Node:** 30,000

Both algorithms use the same graph, starting point, and goal node so that their observed performance can be compared under the same conditions.

## Profiling Tools

### 1. `timeit`

Python's built-in `timeit` module is used to measure the execution time of the BFS and DFS implementations.

The reported values represent the selected experimental measurements used in the SLE-2 report.

### 2. Py-Spy

**Py-Spy** is used for runtime profiling of the Python program.

It helps identify where the program spends its execution time and is used to generate flamegraphs for both BFS and DFS.

### 3. Node Counter

A `nodes_expanded` counter is maintained in each search algorithm.

This counter records the number of nodes processed by the algorithm before the goal node is reached.

## Experimental Results

The selected experimental results are shown below:

| **Metric**     | **BFS** |  **DFS** |
| -------------- | ------: | -------: |
| Average Time   | 4.53 ms | 22.33 ms |
| Nodes Expanded |  15,000 |   54,472 |

The above values were obtained from the experiment documented in the SLE-2 report.

## Complexity

| **Algorithm** | **Best Case** | **Average Case** | **Worst Case** | **Space Complexity** |
| ------------- | ------------- | ---------------- | -------------- | -------------------- |
| BFS           | O(1)          | O(V)             | O(V)           | O(V)                 |
| DFS           | O(1)          | O(V)             | O(V)           | O(V)                 |

Where **V** represents the number of vertices in the graph.

The actual execution behaviour can vary depending on the graph structure, goal-node position, implementation, and system conditions.

## Analysis

For the selected binary-tree experiment, BFS recorded a lower execution time and expanded fewer nodes than DFS.

* **BFS:** 5.29 ms and 15,000 nodes expanded
* **DFS:** 23.42 ms and 54,472 nodes expanded

Based on these measurements, BFS required less execution time and examined fewer nodes for the selected goal node.

However, these results are specific to the graph structure, implementation, hardware, and experimental conditions used in this project. They should not be considered a universal performance comparison between BFS and DFS.

## Flamegraphs

The flamegraphs generated using Py-Spy are stored inside the `profiling` directory.

Files included:

* `bfs_flamegraph.svg`
* `dfs_flamegraph.svg`

The flamegraphs provide a visual representation of the program's runtime activity and help identify the functions that contribute to the execution time.

## Repository Structure

```text
IAI_SLE-2_25UME044/
│
├── README.md
├── bfs_dfs_profiling.py
├── AI_Contribution_Log.md
│
├── profiling/
│   ├── bfs_flamegraph.svg
│   └── dfs_flamegraph.svg
│
└── report/
    └── SLE2_25UAM042_Koustubh_Sampat_Chorade.pdf
```

## AI Contribution

ChatGPT was used during the development and documentation of this project for:

* Understanding the concepts of BFS and DFS.
* Structuring the Python implementation.
* Understanding performance measurement using `timeit`.
* Learning the profiling workflow using Py-Spy.
* Understanding flamegraph output.
* Interpreting the experimental observations.
* Assisting in the preparation of the SLE-2 documentation.

The final program was executed and tested by the student. The performance values reported in this README were obtained from the student's execution.

## Conclusion

This project provides a practical comparison of BFS and DFS using the same binary-tree graph and search objective.

The experiment demonstrates that **execution time and the number of nodes expanded** are useful metrics for evaluating search algorithms in practice.

For the selected experimental conditions, BFS recorded lower execution time and fewer node expansions than DFS. The use of **Py-Spy flamegraphs** further provides a visual way to examine the runtime behaviour of the implementations.

Overall, the experiment helps demonstrate the difference between theoretical algorithmic complexity and the performance observed during an actual program execution.
