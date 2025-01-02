# Topological Sort 

Topological sorting is a method used to order vertices/nodes in a **directed acyclic graph**. 
Examples are:
- determining prerequisite courses are required for an advanced course
- which task should be completed before other task that depend on it
- which letters or characters are ahead of other characters/letters

Topological sorting may not be unique and could have multiple valid topological orders depending on the structure of the graph.

```
      1              0
    /   \          /   \
  3      5        2      4
    \   /        /        \
      7        6            8
```

in this graph there are several possible topological sorts such as :
`0, 1, 3, 7, 2, 6, 5, 4, 8`
`1, 0, 2, 3, 6, 7, 5, 4, 8`


## Pseudo Code (BFS method)

1.  Map input/graph to adjacency list or matrix if possible.
2.  Calculate in-degrees for each vertex and increase in-degrees of its neighbors by 1.
3.  Initialize queue and enqueue nodes with in-degrees of 0.
4.  Process nodes. for each node , add node to output array and subtract each of its neighboring in-degrees by 1.
5.  Queue neighboring nodes with 0 indegrees. If neighboring nodes in-degrees become 0, queue it.
6.  Check for cycles. if total output/list is different from size of in-degrees - there is a cycle and there is no valid sorting.
7.  Return output.

## Algorithm

```python
from collections import deque

class TopologicalSort:
    def __init__(self, vertices: int):
        # initialize the graph
        self.in_degree = {i: 0 for i in range(vertices)}
        self.graph = {i: [] for i in range(vertices)} # graph as adjacency list
        
    def sort(self, edges: list[list]):
        sorted_order = []
        
        if len(self.in_degree) <= 0:
            return sorted_order
        
        # build the graph
        
        for edge in edges:
            parent, child = edge[0], edge[1]
            self.graph[parent].append(child)
            self.in_degree[child] += 1
            
        # initialize queue and enqueue all in degrees of 0 
        sources = deque([self.in_degree[i] for i in self.in_degree if self.in_degree[i] == 0])
        
        
        ''' 
            method above uses list comprehension. below is how you would do it normally.
            
            for degree in self.in_degree:
                if self.in_degree[degree] == 0:
                sources.append(degree)
                
        '''
        
        # process nodes
        
        while sources:
            vertex = sources.popleft()
            sorted_order.append(vertex) # add vertex to output
            
            for child in self.graph[vertex]:
                self.in_degree[child] -= 1 # decrement indegree of child nodes
                
                # enqueue child nodes with 0 indegree
                if self.in_degree[child] == 0:
                    sources.append(child)
        
        if len(sorted_order) != len(self.in_degree): # check for cycles
            return []
        
        return sorted_order
```
