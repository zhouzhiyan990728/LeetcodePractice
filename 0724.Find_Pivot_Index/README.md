# 724.Find Pivot Index

## Question
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

### Example
```
Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11
```

## Solution
* Here we create two arrays to store the sum from left or right. Then match them, if there is the same index that has the same value, return the index.

## Code
```python3
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum_left,sum_right = [None]*len(nums),[None]*len(nums);
        sum_num = 0;
        for i in range(len(nums)):
            sum_left[i] = sum_num;
            sum_num += nums[i];
        
        sum_num = 0;
        for i in range(len(nums)-1,-1,-1):
            sum_right[i] = sum_num;
            sum_num += nums[i];
            
        for i in range(len(nums)):
            if sum_left[i] == sum_right[i]:
                return i;
        
        return -1;
```
