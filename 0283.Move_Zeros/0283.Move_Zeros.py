from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        index = 0;
        for i in nums:
            if i != 0:
                nums[index] = i;
                index += 1;
        for i in range(index,len(nums)):
            nums[i] = 0;