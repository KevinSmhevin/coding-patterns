 # Union Find (Disjoint Set Union)

a data structure that keeps track of a partition of a set into disjoint subsets (no sets overlap)

### Two Core Operations: 
- **Find** - determine which set an element belongs to. determines if 2 elements are in the same set.
- **Union** - merge two sets together. Useful when there is a relationship between 2 elements.

useful for when we need to find whether 2 elements belong to the same group.


Union Find Algorithm Properties
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
