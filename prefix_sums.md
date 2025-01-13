# Prefix Sums

Prefix sums maintain a running total sum of values of an iterable object.

### applications of prefix sum

It has constant time access to the sums and can be used to efficiently determine the sums, product or count of specific values of subarrays.


When to use prefix sums vs sliding window?
If you have a problem where you need to check the subtotal values of an array it is likely a prefix sum or sliding window problem. If the array can have negative integers then it is not solveable with a sliding window and is likely solveable with a prefix sum.

### prefix sum examples

prefix sum and getting the sum between ranges


```python

# basic prefix sum of an array

array = [1, 5, 10, 15, 20]

prefix_sums = [0] * len(array) # initialize prefix sums

running_total = 0 # running total

for i in range(len(array)): 
    running total += array[i]
    prefix_sums[i] = running total

# get value at index

def get_sum(array, prefix_sums, index):
    return prefix_sums[index]


# get a sum between range 

def get_sum_between_range(array, prefix_sums, start, end):
    if left == 0:
        return prefix_sums[end]

    else:
        return prefix_sums[end] - prefix_sums[start - 1]


```