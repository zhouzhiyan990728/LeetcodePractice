from typing import List


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