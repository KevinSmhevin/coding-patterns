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

```python

    matrix = [[0, 1, 0, 1],
              [1, 0, 1, 0],
              [0, 1, 0, 1],
              [1, 0, 1, 0]]
```
