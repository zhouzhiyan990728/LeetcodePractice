from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        index = 0;
        count = 0;
        count_zero = 0;
        max_count = 0;
        max_index = 0;
        while index < len(nums):
            if nums[index] == 1:
                count += 1;
                index += 1;
            elif nums[index] == 0 and count_zero == 0:
                count += 1;
                count_zero += 1;
                index += 1;
                max_index = index;
            else:
                index = max_index;
                count = 0;
                count_zero = 0;

            if count > max_count:
                max_count = count;

        return max_count;