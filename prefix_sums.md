# Prefix Sums

Prefix sums maintain a running total sum of values of an iterable object.

### applications of prefix sum

It has constant time access to the sums and can be used to efficiently determine the sums, product or count of specific values of subarrays.


When to use prefix sums vs sliding window?
If you have a problem where you need to check the subtotal values of an array it is likely a prefix sum or sliding window problem. If the array can have negative integers then it is not solveable with a sliding window and is likely solveable with a prefix sum.

### prefix sum examples

##### array prefix sum and getting the sum between ranges


```python

class PrefixSum:
    def __init__(self, array):
        self.prefix_sums = [0] * len(array) # initialize prefix sums
        running_total = 0
        
        for i in range(len(array)):
            running total += array[i]
            prefix_sums[i] = running total

    # get value at index
    def get_sum(self, index):
        return self.prefix_sums[index]

    # get a sum between range 
    def get_sum_between_range(self, start, end):
        if start == 0:
            return self.prefix_sums[end]

        else:
            return self.prefix_sums[end] - self.prefix_sums[start - 1]


```


##### hash map prefix sum examples 

get count subarrays that == k 

example: array = [1, 2, 3, 4, 5] k = 5

```python

def get_subarrays_equal_k(array, k):
    prefix_sums = {0 : 1}
    total = 0
    count = 0

    for i in range(len(array)):
        total += array[i]
        
        if total - k in prefix_sums:
            count += prefix_sums[total - k]

        prefix_sums[total] = prefix_sums.get(total, 0) + 1

    return count 

```


