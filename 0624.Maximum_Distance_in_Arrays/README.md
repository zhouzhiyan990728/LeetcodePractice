# 624.Maximum Distance in Arrays

## Question
You are given , where each array is sorted in ascending order.

You can pick up two integers from two different arrays (each array picks one) and calculate the distance. We define the distance between two integers and to be their absolute difference .ab|a - b|

Return the maximum distance.

### Example
```
Input: arrays = [[1,2,3],[4,5],[1,2,3]]
Output: 4
Explanation: One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array.
```

## Solution
* As the arrays are in ascending order, we just need to compare the extreme points in different arrays.
* Considering the two points should belong different arrays, just iterate every arrays and keep track of the maximum distance found so far. 

## Code
```python3
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_value = arrays[0][0]
        max_value = arrays[0][-1]

        max_distance = 0

        for array in arrays[1:]:
            # Update max_distance
            max_distance = max(max_distance, abs(array[0] - max_value), abs(array[-1] - min_value))

            # Update min and max values for subsequent iterations
            min_value = min(min_value, array[0])
            max_value = max(max_value, array[-1])

        return max_distance
```