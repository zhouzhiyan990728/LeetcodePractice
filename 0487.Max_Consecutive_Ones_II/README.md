# 487.Max Consecutive Ones II

## Question
Given a binary array nums, return the maximum number of consecutive 1's in the array if you can flip at most one 0.

### Example
```
Input: nums = [1,0,1,1,0]
Output: 4
Explanation: 
- If we flip the first zero, nums becomes [1,1,1,1,0] and we have 4 consecutive ones.
- If we flip the second zero, nums becomes [1,0,1,1,1] and we have 3 consecutive ones.
The max number of consecutive ones is 4.
```

## Solution
* Iterate each element, and count the length of each sequence containing only one zero.
* If there is a second zero, we should recalculate the sequence from the element after the first zero.

## Code
```python3
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        index = 0;
        count = 0;
        count_zero = 0;
        max_count = 0;
        max_index = 0;
        while index < len(nums):
            if nums[index] == 1:
                count += 1;
                index += 1;
            elif nums[index] == 0 and count_zero == 0:
                count += 1;
                count_zero += 1;
                index += 1;
                max_index = index;
            else:
                index = max_index;
                count = 0;
                count_zero = 0;

            if count > max_count:
                max_count = count;

        return max_count;
```