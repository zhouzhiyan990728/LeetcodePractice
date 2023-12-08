# 1099.Two Sum Less Than K

## Question
Given an array nums of integers and integer k, return the maximum sum such that there exists i < j with nums[i] + nums[j] = sum and sum < k. If no i, j exist satisfying this equation, return -1.

### Example
Input: nums = [34,23,1,24,75,33,54,8], k = 60
Output: 58
Explanation: We can use 34 and 24 to sum 58 which is less than 60.

## Solution
* We sort the array and set two pointers from the start and the end of the given array. 
* Firstly sum the first and the last elements as the initial result. Then compare the result with the given value k, if the sum is less than k, then move the left pointer. Otherwise move the right pointer until the sum is more than k.

## Code
```python3
class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        left = 0;
        right = len(nums)-1;
        nums.sort();
        result = -1;
        
        while left<right:
            sum = nums[left]+nums[right];
            if sum<k:
                result = max(sum,result);
                left += 1;
            else:
                right -= 1;

        return result;
```