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

```
# bidirectional     # directional
    a -- b            a --> b
    |    |            ^     |
    d -- c            |     V
                      d <-- c
```

##### bidirectional

|matrix| a | b | c | d |
|:-----|:--|:--|:--|:--|
|a     | 0 | 1 | 0 | 1 |
|b     | 1 | 0 | 1 | 0 |
|c     | 0 | 1 | 0 | 1 |
|d     | 1 | 0 | 1 | 0 |

##### directional

|matrix| a | b | c | d |
|:-----|:--|:--|:--|:--|
|a     | 0 | 1 | 0 | 0 |
|b     | 0 | 0 | 1 | 0 |
|c     | 0 | 0 | 0 | 1 |
|d     | 1 | 0 | 0 | 0 |


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


```

