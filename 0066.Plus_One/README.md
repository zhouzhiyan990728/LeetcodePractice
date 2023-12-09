# 66.Plus One

## Question
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

### Example
```
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
```

## Solution
* There are two different situations:
1. The last digit is not 9. 
2. The last digit is 9.
* For the first situation, just plus 1 on the last digit.
* For the second situation, set the last digit as 0 and the former digit plus 1.

## Code
```python3
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        index = len(digits)-1;
        if digits[index] != 9:
            digits[index] += 1;
            return digits;
        
        digits[index] += 1;
        while digits[index] == 10 and index > 0:
            digits[index] = 0;
            index -= 1;
            digits[index] += 1;
            
        if digits[index] == 10 and index == 0:
            digits[index] = 0;
            digits.insert(0,1);
        
        return digits;
```
