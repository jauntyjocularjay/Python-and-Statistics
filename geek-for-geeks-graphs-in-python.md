# Graphs in python
source: [Geek for Geeks](https://www.geeksforgeeks.org/python/introduction-to-graphs-in-python/)

## Components of graph data structure

1. vertices: fundamental units of a graph - aka vertex or nodes - can be labeled or not

1. edges: used to connect two nodes on a graph.
    - can be ordered pair of nodes
    - can connect two nodes in any possible way. no rules!
    - aka as arcs may/may not be labeled

## Representation of graph data structure

### Adjascency Matrix Representation of a graph data structure

The graph is stored as a 2d matrix where rows and columns denote vertices. each entry in the matrix represents the weight of the edge between vertices.

    Adjacency Matrix:
    0 1 1 0
    1 0 1 0
    1 1 0 1
    0 0 1 0

### Adjascency List representation of graph data structure

Represented as a linked-list collection with an array of pointer which points to the edges connect to the vertex.

    Adjacency List Representation:
    0: 1 2 
    1: 0 2 
    2: 0 1 3 
    3: 2 

### Comparison between adjency matrix and list

When a graph contains many edges, go with a matrix because few entries will be empty.

|action|adjency matrix|adjency list|
|---|---|---|
|adding edge| O(1) | O(1) |
|removing edge|  O(1) | O(n) |
|initializing| O(n<sup>2</sup>) | O(n)|

