# Dijkstra's Algorithm

Allow's us to find the shortest path between two vertices in a graph. GPS navigation systems like google maps fundamentality rely on Dijkstra's algorithm

    - must be on a weighted graph
    - weighted graph must not have negative values on edges

[helpful video from spanning trees](https://www.youtube.com/watch?v=EFg3u_E6eHU)

### Dijkstra's algorithm steps 

Dijkstra's algorithm uses a modified BFS approach that uses a min heap and visited data structure

    - STEP 1: create an adjacency list or matrix to store the graph
        -   populate the data structure with vertex being the key and a list of neighbor nodes as the value
    - STEP 2: initialize a min heap and create required variables/data structures 
        - create a variable to track the time/distance/cost that is represented on each edge. set it to 0
            - example: time = 0 
        - initialize a min heap and add the starting time/distance and starting node as a tuple
            - its important to have the time/distance as the first element of the tuple so the min heap can work.
            - example: (0, node)
        - created a visited data structure to keep track of nodes that we visited.
            - usually a hash set
        - create an output/result data variable (if needed)
    - STEP 3: Breadth First Search through the shortest edges while min heap has elements
        -  pop the top element of the min heap 
            - add node to visited ds
            - iterate through node neighbors in adjacency list 
                - for each neighbor thats not in visited add them to the heap
                - add the time/distance of the current node + neighbor node
    
### Dijkstra's algorithm example

```python

    # input example takes in an edges list that contains tuples of (current_node, destination_node, weight/distance)
    # edges = [(0, 1, 3), (0, 2, 5), (1, 3, 8), (2, 3, 2)]

    from heapq import *

    class Djikstra:
        def __init__(self, edges : List[List[int]], no_of_nodes: int):
            self.adj_list = {}
            for i in range(no_of_nodes):
                self.adj_list[i] = []
            
            for src, dst, time in edges:
                adj[src].append((dst, time))


        def find_shortest_path(self, source: int, destination: int):

            path = str(source)
            time = 0
            visited = set()

            min_heap = []
            heapq.heappush(min_heap, (time, source, path))
            
            while min_heap:
                current_time, current_node, current_path = heap.heappop(min_heap)
                    visited.add(current_node)

                    if current_node == destination:
                        return current_path

                    for next_node, travel_time in self.adj_list[current_node]:
                        if next_node not in visited:
                            heapq.heappush(min_heap, 
                            (current_time + travel_time, next_node, current_path + "->" + str(next_node)))

            
            return "no path"

```
        
