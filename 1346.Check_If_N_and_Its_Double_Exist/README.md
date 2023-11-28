# 1346.Check if N and Its Double Exist

## Question
Given an array arr of integers, check if there exist two indices i and j such that :

* i != j
* 0 <= i, j < arr.length
* arr[i] == 2 * arr[j]

### Example
```
Input: arr = [10,2,5,3]
Output: true
Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]
```

## Solution
* It can be easily solved by two for loop.
* In order to have a less time complexity, here we try to have a O(n) complexity. We remove all the zeros in the array and then iterate each element and check if there is a double value in the array.

## Code
```python3
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        if arr.count(0)>1:
            return True;

        index = 0;
        for i in arr:
            if i == 0:
                arr.pop(index);
            index += 1;

        for i in arr:
            if i*2 in arr:
                return True;

        return False;
```