 # Union Find (Disjoint Set Union)

a data structure that keeps track of a partition of a set into disjoint subsets (no sets overlap)

Union find keeps track of the relationships between nodes/vertexes in a graph by using 2 arrays/list.
The overall purpose/advantage of union find is to quickly determine if 2 nodes are disjointed or connected.
Union find does this by organizing connected nodes and determining a parent node to represent all those connected nodes.
Nodes that are not connected to eachother(directly or indirectly) will therefore have a different parent node.

### Why union find over DFS/BFS

When applicable union find provides near constant time operations for union and find operations (overall `O log n` time).
In contrast BFS/DFS will take `O(V + E)` where `v = vertices e = edges` overall `O(n)` linear time.
The main drawbacks of union find are space overhead to store the parent and rank of each node/vertex and the initial setup to create the union find data structure.


### Union find class properties
 - the 2 arrays are the `parent` array and `rank` array.
   - the *parent* array keeps track of the nodes parents
     - the index represents the node and the value represents its parent
     - every node/index value is initialized to itself

   - the *rank* array keeps track of a nodes rank and is used to evaluate which nodes are parents
     - the index represents the node and the value represents the rank
     - every node/index value is initialized to the same value(usually 0 or 1)
    
```python
# in a graph with vertices 0 through 4 every vertices parents start as itself
parent = [0, 1, 2, 3, 4]

# in the graph below:
# vertex 0 and 1 parent[0], parent[1] is itself
# vertex 2's parent[2] parent is vertex 1
# vertex 3's parent[3] parent is vertex 0
# vertex 4's parent[4] parent is vertex 3
parent = [0, 1, 1, 0, 3]

# ranks are all initialized to 1, index represents the vertex, value is the rank
rank = [1, 1, 1, 1, 1]

# with the parents above the ranks array might look like this:
rank = [3, 2, 1, 2, 1]

# the graphs might look like this

       0         1
        \         \
          3         2
         /
       4

# the graph has 2 disjointed sets with vertex 0 and 1 being the parent or leader nodes
```


### Two Core Operations: 
- **Find** - determine which set an element belongs to. determines if 2 elements are in the same set.
- **Union** - merge two sets together. Useful when there is a relationship between 2 elements.

useful for when we need to find whether 2 elements belong to the same group.


### Union Find Algorithm Properties
- parent array with all vertices referencing themselves `[0, 1, 2]`
- rank array representing all vertices with initialized values of 1 `[1, 1, 1]`
- find method
  - finds parent of selected node/vertex
  - needs to do path compression for the child node `0 <- 1 <- 2` --> `0 <- 1` and `0 <- 2`
- union method (by size)
  - takes 2 vertices
  - find parents of both vertices
  - if vertices have the same parents return 0 or false (nodes are already in union)
  - join the union by which vertex/nodes rank is greater
    -  update the parent of the lesser ranked vertex to the greater ranked vertex parent
    -  add the rank of the lesser ranked vertex to the greater ranked vertex parent

### Union Find Algorithm
```python
class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size)) # initialize parent to self [1, 2, 3]
        self.rank = [1] * size # initialize rank to the same rank [1, 1, 1]
        
    def find(self, node):
        if node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node]) # Path compression
        return self.parent[node]
    
    def union(self, node1, node2):
        parent1, parent2 = self.find(node1), self.find(node2) 
        
        if parent1 == parent2: # if same - do nothing
            return 
        
        else:  # union by size

            if self.rank[parent1] < self.rank[parent2]:
                self.parent[parent1] = parent2
                self.rank[parent2] += self.rank[parent1]
            
            else:
                self.rank[parent2] = parent1
                self.rank[parent1] += self.rank[parent2]
                

```
