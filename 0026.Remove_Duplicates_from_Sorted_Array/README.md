# 26.Remove Duplicate from Sorted Array

## Question
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.

### Example
```
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
```

## Solution
* The solution is very similar with the question 27.
* As the given array is in non-decreasing order, just need to justify if the next element is bigger, and if so, put the next element into the first few bits of the array.

## Code
```python3
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0;
        for i in range(len(nums)-1):
            if nums[i+1]>nums[i]:
                index += 1
                nums[index] = nums[i+1];

        return index+1;
```