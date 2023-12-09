from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_num = max(nums);
        for i in nums:
            if i * 2 > max_num and i != max_num:
                return -1;

        return nums.index(max_num);