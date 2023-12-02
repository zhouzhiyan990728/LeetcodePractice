# 283.Remove Zeros

## Question
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

### Example
```
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
```

## Solution
* Iterate elements, if the element is not equal to zero, put them in the array. And then fill the rest of the array with zeros.

## Code
```python3
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        index = 0;
        for i in nums:
            if i != 0:
                nums[index] = i;
                index += 1;
        for i in range(index,len(nums)):
            nums[i] = 0;
```