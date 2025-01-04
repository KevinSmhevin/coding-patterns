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
                