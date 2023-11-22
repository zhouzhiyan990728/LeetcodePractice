# 1285.Find_Numbers_With_Even_Number_of_Digits

## Question
Given an array nums of integers, return how many of them contain an even number of digits.

### Example
```Python
Input: nums = [12,345,2,6,7896]
Output: 2
Explanation: 
12 contains 2 digits (even number of digits). 
345 contains 3 digits (odd number of digits). 
2 contains 1 digit (odd number of digits). 
6 contains 1 digit (odd number of digits). 
7896 contains 4 digits (even number of digits). 
Therefore only 12 and 7896 contain an even number of digits.
```

## Solution
* Given an integer array, calculate the number of the numbers that have even digits.
* Sweep through the array, transfer each integer to string type and check if its length is an even number.

## Code
```Python
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 1;
        evenCount = 0;
        for i in nums:
            if len(str(i)) % 2 ==0:
                evenCount += 1;
        return evenCount;
```