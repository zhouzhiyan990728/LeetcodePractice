# 747.Largest Number At Least Twice of Others

## Question
You are given an integer array nums where the largest integer is unique.

Determine whether the largest element in the array is at least twice as much as every other number in the array. If it is, return the index of the largest element, or return -1 otherwise.

### Example
```
Input: nums = [3,6,1,0]
Output: 1
Explanation: 6 is the largest integer.
For every other number in the array x, 6 is at least twice as big as x.
The index of value 6 is 1, so we return 1.
```

## Solution
* Use max() to find the maximum number in the array.
* Then Iterate the array to check if there is an element whose twice is larger than the maximum value.

## Code
```python3
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_num = max(nums);
        for i in nums:
            if i * 2 > max_num and i != max_num:
                return -1;

        return nums.index(max_num);
```