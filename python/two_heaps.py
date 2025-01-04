from heapq import *

class MedianFinder:
    def __init__(self):
        self.smaller_half = [] # max heap
        self.larger_half = [] # min heap
    
    def add_num(self, num):
        if not self.smaller_half or -self.smaller_half[0] >= num:
            heappush(self.smaller_half, -num)
        else:
            heappush(self.larger_half, num)
            
        #balance the heaps if needed
        
        if len(self.smaller_half) > len(self.larger_half) + 1:
            heappush(self.larger_half, -heappop(self.smaller_half))
        
        elif len(self.smaller_half) < len(self.larger_half):
            heappush(self.smaller_half, -heappop(self.larger_half))
        
        
    def find_median(self):
        # even number of elements
        if len(self.smaller_half) == len(self.larger_half):
            return (-self.smaller_half[0] + self.larger_half[0]) / 2.0
        
        # odd number of elements we know small heap has one more element
        else:
            return -self.smaller_half[0] * 1.0
         