# 941.Valid Mountain Array

## Question
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

* arr.length >= 3 
* There exists some i with 0 < i < arr.length - 1 such that:

    arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 

    arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

### Example
```
Input: arr = [2,1]
Output: false

Input: arr = [3,5,5]
Output: false

Input: arr = [0,3,2,1]
Output: true
```

## Solution
* To determine a mountain array, there are three conditions: 
1. array.length >= 3
2. There is only one mountain point
3. No two consecutive elements are equal.
* So we can iterate each element with two while loop to justify the status of two consecutive elements. If there are any instances that do not meet the requirement, then return False.


## Code
```python3
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        index = 0;
        if len(arr) < 3:
            return False;

        while index < len(arr) - 1 and arr[index + 1] > arr[index]:
            index += 1;

        if index == len(arr) - 1 or index == 0:
            return False;

        while index < len(arr) - 1 and arr[index + 1] < arr[index]:
            index += 1;

        if index == len(arr) - 1:
            return True;

        return False;
```