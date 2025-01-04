# Two Heaps

A popular coding pattern is to efficiently find the median between a set of elements.
An efficient way to continously do this is to divide the elements into two heaps.

## Finding Median from data stream

consider the following leetcode problem: https://leetcode.com/problems/find-median-from-data-stream

The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.

### Naive approach to the problem - sorted list

The naive approach to the problem is to keep a sorted array.

Consider arr = [2,3,4]

`findMedian()` # should be to return 3 --> `return arr[mid]`

`addNum(1)` # should result in arr being [1,2,3,4]

`findMedian()` # should be to return 2.5 --> `return (arr[mid] + arr[mid + 1]) / 2`

in both cases findMedian is O(1)
but addNum() is O(N)

how can we do better for addNum?

### Two heap solution 

#### approach

we'll have two heaps:
  - we'll store half the numbers in each heap. 
  - a small heap `small_heap`
    - this will be a **max heap**
    - keeps the smaller half of numbers with the largest being at the top of the heap
  - a large heap `large_heap`
    - this will be a **min heap**
    - keeps the larger half of numbers with the smallest numbers at the top of the heap

consider arr = [1, 3, 4, 5, 7, 8]

these are how each heaps should store the elements

```python
    small_heap = [1, 3, 4]

    # tree visualized
          4
        /   \
      1       3

    large_heap = [8, 7, 5]

    # tree visualized

        5
      /    \
    7        8

```

since we are using heaps `add_num()` will be log(n) time

by default we'll add numbers to the `small_heap` and if small heap is larger than `large_heap` by 1 than we'll `pop()` from `small_heap` and `push()` it to the `large_heap`. 
This is important to keep the heaps at even length when total number of numbers is even and to keep the difference of length no more than 1 when the total number of numbers is odd.

but what happens when if we add 6 to the scenario above

now the heaps will look like this 

```python
    small_heap = [1, 3, 4, 6]

    # tree visualized
          6
        /   \
      1       4
            /
          3

    large_heap = [8, 7, 5]

    # tree visualized

        5
      /    \
    7        8

```

the problem is now `small_heap`'s max number is larger than `large_heap`'s min number. we need to always make sure small heaps numbers < large heaps numbers
we'll have to `pop()` 6 and add it to the large heap.





