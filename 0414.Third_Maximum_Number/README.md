# 414.Third Maximum Number

## Question
Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

### Example
```
Input: nums = [3,2,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.
```

## Solution
* In this problem, we need to return the third distinct maximum number in this array.
* Sort the array in a reverse order and find the third distinct number.

## Code
```python3
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort(reverse = True);
        max = nums[0];
        count = 1;
        
        for i in nums:
            if i != max:
                max = i;
                count += 1;
            if count == 3:
                break;
                
        if count<3:
            return nums[0];
        
        return max;
```