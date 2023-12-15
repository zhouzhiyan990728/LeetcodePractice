from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = [];
        for i in range(len(nums)):
            if nums[abs(nums[i]) - 1] > 0:
                nums[abs(nums[i]) - 1] *= -1;

        for j in range(1, len(nums) + 1):
            if nums[j - 1] > 0:
                result.append(j);

        return result;
