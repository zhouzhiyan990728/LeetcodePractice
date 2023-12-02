from typing import List


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