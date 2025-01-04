from collections import heapq

class MedianFinder:
    '''
    small_heap will be a max heap containing all the smaller numbers
    large_heap will be a min heap containing all the larger numbers
    '''
    def __init__(self):
        self.small_heap, self.large_heap = [], []
        
    
    def add_num(self, num):
        if not self.small_heap or -self.small_heap[0] >= num:
            heapq.heappush(self.small_heap, -num)
        else:
            heapq.heappush(self.large_heap, num)
            
        #balance the heaps if needed
        
        if len(self.small_heap) > len(self.large_heap) + 1:
            heapq.heappush(self.large_heap, -heapq.heappop(self.small_heap))
        
        elif len(self.small_heap) < len(self.large_heap):
            heapq.heappush(self.small_heap, -heapq.heappop(self.large_heap))
        
        
    def find_median(self):
        # even number of elements
        if len(self.small_heap) == len(self.large_heap):
            return (-self.small_heap[0] + self.large_heap[0]) / 2.0
        
        # odd number of elements we know small heap has one more element
        else:
            return -self.small_heap[0] * 1.0
         