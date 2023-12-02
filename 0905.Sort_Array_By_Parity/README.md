# 905.Sort Array By Parity

## Question
Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.

### Example
```
Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
```

## Solution
* There are two pointers from start and end of the array.
* Considering three conditions. 
1. If the element at the first pointer is an odd number and the element at the second pointer is an even number, then switch them around.
2. If the element at the first pointer is an even number, then the second pointer moves forward.
3. If the element at the second pointer is an odd number, then the first pointer moves backward.

## Code
```python3
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i = 0;
        j = len(nums) - 1;
        while i < j:
            if nums[i] % 2 == 1 and nums[j] % 2 == 0:
                nums[i], nums[j] = nums[j], nums[i];
                i += 1;
                j -= 1;

            if nums[i] % 2 == 0:
                i += 1;
            if nums[j] % 2 == 1:
                j -= 1;

        return nums;
```
