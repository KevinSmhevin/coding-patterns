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


## Toplogical Sorting Pseudo Code (BFS method)

1.  Map input/graph to adjacency list or matrix if possible.
2.  Calculate in-degrees for each vertex and increase in-degrees of its neighbors by 1.
3.  Initialize queue and enqueue nodes with in-degrees of 0.
4.  Process nodes. for each node , add node to output array and subtract each of its neighboring in-degrees by 1.
5.  Queue neighboring nodes with 0 indegrees. If neighboring nodes in-degrees become 0, queue it.
6.  Check for cycles. if total output/list is different from size of in-degrees - there is a cycle and there is no valid sorting.
7.  Return output.
