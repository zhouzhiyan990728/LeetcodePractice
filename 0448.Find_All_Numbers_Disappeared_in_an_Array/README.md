# 448. Find All Numbers Disappeared in an Array

## Question
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

### Example
```
Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
```

## Solution
* Use an in-space method to solve this question. We can use the positive or negative state of each element in the array to indicate whether number occurs.
* Iterate the given array, if any number nums[i] appears, multiply the nums[i-1] with -1.
* Check the positive or negative state of each element, if it is positive, the value of the corresponding index is the number that does not appear.

## Code
```python3
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = [];
        for i in range(len(nums)):
            if nums[abs(nums[i])-1]>0:
                nums[abs(nums[i])-1] *= -1;

        for j in range(1,len(nums)+1):
            if nums[j-1] > 0:
                result.append(j);
                
        return result;
```