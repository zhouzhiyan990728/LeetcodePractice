from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0;
        for i in range(len(nums)-1):
            if nums[i+1]>nums[i]:
                index += 1
                nums[index] = nums[i+1];

        return index+1;