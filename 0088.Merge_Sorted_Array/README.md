# 0088.Merge Sorted Array

## Question
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

### Example
```
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
```

## Solution
* There are two solutions. The easier one is to merge the two arrays first and to use sort() to sort the merged array. However, this solution has a higher time complexity.
* The solution that has the lowest time complexity is to process the merge and sorting together.

## Code using sort()
```python3
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index = 0;
        for i in range(m, m+n):
            nums1[i] = nums2[index];
            index += 1;
        nums1.sort();
```

## Code2
```python3
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m-1;
        p2 = n-1;
        for i in range(m+n-1,-1,-1):
            if p2<0:
                break;
            elif p1>=0 and nums1[p1]>=nums2[p2]:
                nums1[i] = nums1[p1];
                p1 -= 1;
            else:
                nums1[i] = nums2[p2];
                p2 -= 1;
```
