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

##### prefix products
 - you need to intialize the array values to 1 instead of 0
 - to get product between ranges it is prefix_product[end] // prefix_product[start -1]

##### hash map prefix sum examples 

##### get count subarrays that == k 

strategy:
 - use a hashmap with `key => total; value => count`

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

EX: k = 32
array = [7, 5, 20, 8, 4, 9]
 - explanation
 - From index 1 we will have prefix_sum[12] = 1 
 - From index 2 we will have prefix_sum[32] = 1
 - from initializing prefix_sums {0: 1} will run since prefix_sum[32 - 32 (0)] = 1 
 - From index 4 we will have prefix_sum[44] = 1 so we add to count
 - prefix_sum[44 - 32 (12)] = 1 so we add that to count
 - the final count will be 2



##### get longest length of subarrays that == k

strategy:
 - user a hashmap with key => total; value => index

```python

def longest_subarray_equal_k(array, k):
    prefix_sums = {}
    max_length = 0
    total = 0

    for i in range(len(array)):
        total += array[i]

        if total == k:
            max_length = i + 1

        elif total - k in prefix_sums:
            max_length = max(max_length, i - prefix_sums[total - k])
        
        else:
            prefix_sums[total] = i
    
    return max_length


```
