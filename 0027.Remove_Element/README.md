# 88.Remove Element

## Question
Given an integer array and an integer , remove all occurrences of in in-place. The order of the elements may be changed. Then return the number of elements in which are not equal to .numsvalvalnumsnumsval

Consider the number of elements in which are not equal to be , to get accepted, you need to do the following things:numsvalk

Change the array such that the first elements of contain the elements which are not equal to . The remaining elements of are not important as well as the size of .numsknumsvalnumsnums
Return k.

### Example
``` 
Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).
```

## Solution
* Actually it can be easily solved by using two pointers, I was confused by the example. The order of the output array has no effect on the result.
* So here I provide two solutions. One can output the same sequence array as the example, and one just only remove the element.
* Remove the last element if it equals val. And then iterate over all elements, and if it is equal to val, swap it with the last digit.

## Code (Easy)
```python3
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0;
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j];
                i += 1;
        return i;
```

## Code
```python3
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        self.checkLastElement(nums, val);
        index = 0;
        for i in nums:
            if nums and i == val:
                nums[index] = nums[-1];
                nums.pop(-1);
                self.checkLastElement(nums, val);
            index += 1;
        return len(nums);

    def checkLastElement(self, nums: List[int], val: int):
        while nums and nums[-1] == val:
            nums.pop(-1);
```