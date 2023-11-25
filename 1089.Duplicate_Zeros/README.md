# 1089.Duplicate Zeros

## Question
Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.

## Example
```
Input: arr = [1,0,2,3,0,4,5,0]
Output: [1,0,0,2,3,0,0,4]
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
```

# Solution
* Given an integer array, duplicate each zero and keep the array in the same length.
* Although it can be easily solved by insert() and pop(), due to the requirement that it should be in-space, we need to replace each element after the zero in the reverse order.

# Code
```python3
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        index = 0;
        length = len(arr);
        while index<length-1:
            if arr[index] == 0:
                new_index = length-1;
                while new_index > index+1:
                    arr[new_index] = arr[new_index-1];
                    new_index -= 1;
                arr[index+1] = 0;
                index += 2;
            else:
                index += 1;
```