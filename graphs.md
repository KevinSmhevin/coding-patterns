# Graphs

graphs are data structures that consist of **vertices**(nodes) and **edges** connecting them.

### Types of Graphs 

  - undirected graphs - edges are bidirectional connecting vertices in both directions
  - directed graphs - edges are directional connecting vertices in one direction
  - weighted graphs - edges have a specifying value representing distance, cost, weight etc
  - unweighted graphs - edges are unweighted and are all the same
  - acylic graphs - a graph that contains a cycle 
  - cylic graphs - a directional graph that does not contain a cycle 

graphs can be represented in either an **adjacency list** or **adjacency matrix**. 

##### graph examples 
![graph-example](/images/graph-one.png)

```
# bidirectional     # directional
    a -- b            a --> b
    |    |            ^     |
    d -- c            |     V
                      d <-- c
```




##### adjacency matrix examples

##### bidirectional

|   | a | b | c | d |
|:--|:--|:--|:--|:--|
|a  | 0 | 1 | 0 | 1 |
|b  | 1 | 0 | 1 | 0 |
|c  | 0 | 1 | 0 | 1 |
|d  | 1 | 0 | 1 | 0 |

##### directional

|   | a | b | c | d |
|:--|:--|:--|:--|:--|
|a  | 0 | 1 | 0 | 0 |
|b  | 0 | 0 | 1 | 0 |
|c  | 0 | 0 | 0 | 1 |
|d  | 1 | 0 | 0 | 0 |


##### python code of bidirectional matrix 

matrixes are implemented using nested list
  * 0 represents no edge
  * 1 represents an edge(connection)

```python

    matrix = [[0, 1, 0, 1],
              [1, 0, 1, 0],
              [0, 1, 0, 1],
              [1, 0, 1, 0]]
```


##### adjacency list example 

adjacency list are implemented using dictionaries/hash tables
  *  the keys should represent the vertices
  *  the values should be a list or set with the elements being the connected vertices(representing edges)

```python

    #bidirectional
    adj_list_bi = {
        "a": [b, d],
        "b": [a, c],
        "c": [b, d],
        "d": [c, a]
    }

    #directional
    adj_list_dir = {
        "a": [b],
        "b": [c],
        "c": [d],
        "d": [a]
    }

```

##### complete implementation of an abstract adjacency list 

```python

  from collections import defaultdict

  class Graph:
    def __init__(self):
      self.adjacency_list = defaultdict(list)

    def add_vertex(self, vertex):
      if vertex not in self.adjacency_list:
        self.adjacency_list[vertex] = []

    def remove_vertex(self, vertex):
      if vertex not in self.adjacency_list:
        return

      del self.adjacency_list[vertex]

      for vertices in self.adjacency_list.values():
        if vertex in vertices:
          neighbors.remove(vertex)

    def add_edges(self, vertex1, vertex2):
      self.adjacency_list[vertex1].append(vertex2)
      self.adjacency_list[vertex2].append(vertex1)

    def get_vertices(self):
      return list(self.adjacency_list.keys())

    def get_neighbors(self, vertex):
      return self.adjacency_list[vertex]

    def is_adjacent(self, vertex1, vertex2):
      return vertex2 in self.adjacency_list[vertex1]

    def get_vertex_count(self):
      return len(self.adjacency_list)

    def get_edge_count(self):
      count = sum(len(neighbors) for neighbors in self.adjacency_list.values())
      return count // 2


```

### Traversing Graphs
  - DFS - Depth First Search
    -  prioritizes depth
    -  typically implemented with recursion
    -  use DFS when you need to search deep. Backtracking, maze and map problems
    
  - BFS - Breadth First Search
    - prioritizes neighbors
    - typically implemented iteratively with a queue
    - use BFS when you need to prioritize searching neighboring nodes. Find shortest path

#### DFS traversal implementation

```python

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices  # Number of vertices
        self.adjacencyList = [[] for _ in range(vertices)]  # Adjacency list

    # Method to add an edge to the graph
    def addEdge(self, source, destination):
        self.adjacencyList[source].append(destination)
        self.adjacencyList[destination].append(source)  # For an undirected graph

    # Method to perform DFS using recursion
    def DFS(self, startVertex):
        visited = [False] * self.vertices  # Track visited nodes
        print("DFS Traversal: ", end="")
        self.DFSRecursive(startVertex, visited)  # Start DFS from the given vertex

    def DFSRecursive(self, currentVertex, visited):
        visited[currentVertex] = True  # Mark the current node as visited
        print(currentVertex, end=" ")  # Process the current node

        # Recur for all unvisited neighbors
        for neighbor in self.adjacencyList[currentVertex]:
            if not visited[neighbor]:
                self.DFSRecursive(neighbor, visited)


```

#### BFS traversal implementation

```python
from collections import defaultdict, deque

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj_list = defaultdict(list)

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)  # For undirected graph

    def BFS(self, start_vertex):
        visited = [False] * self.V  # To keep track of visited vertices
        queue = deque()

        visited[start_vertex] = True
        queue.append(start_vertex)

        while queue:
            current_vertex = queue.popleft()
            print(current_vertex, end=" ")

            # Explore adjacent vertices
            for neighbor in self.adj_list[current_vertex]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

```


### general approach to solving graph problems

- Figure out approach to traversing the graph/nodes.
  - Almost all graph problems will be solved via DFS or BFS.
    - use DFS when you need to search deep, backtrack and map problems
    - use BFS when you need to search neighboring nodes
- Decide how we want to store the graph data. (Adjacency List or Matrix)
  - If the graph has alot of vertices - list might be better
  - If the graph has alot of edges - matrix might be better
  - Matrix is easier to tell if vertices have an edge
  - When in doubt i usually use an adjancency list
- Keep track of all visited nodes using a set or hashmap 


#### Graph leetcode problems

- [number of provinces](https://leetcode.com/problems/number-of-provinces/description/?envType=problem-list-v2&envId=graph)
- [clone graph](https://leetcode.com/problems/clone-graph/description/?envType=problem-list-v2&envId=graph)
