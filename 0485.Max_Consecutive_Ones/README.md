# 485.Max Consecutive Ones

## Question
Given a binary array nums, return the maximum number of consecutive 1's in the array.

### Example
```python
Input: nums = [1,1,0,1,1,1]

Output: 3

Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
```

## Solution
* Given a binary array, calculate the maximum number of consecutive 1s.
* Sweep through the array, accumulate the number of 1's, dynamically maintain the maximum count, and then output the final result.
* For optimization, you can use max() to save the maximum value.

## Code
```python3
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0;
        maxCount = 0;
        for i in nums:
            if i==1:
                count += 1;
                if maxCount<count:
                    maxCount = count;
            else:
                count=0;
        return maxCount;
```