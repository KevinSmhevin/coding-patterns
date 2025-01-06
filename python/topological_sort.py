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