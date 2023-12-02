from typing import List


class Solution:
    def replaceElements(self, arr:  List[int]) -> List[int]:
        maxValue = arr[-1];
        arr[-1] = -1;
        for i in range(len(arr)-2,-1,-1):
            value = maxValue;
            maxValue = max(maxValue,arr[i]);
            arr[i] = value;
        return arr;