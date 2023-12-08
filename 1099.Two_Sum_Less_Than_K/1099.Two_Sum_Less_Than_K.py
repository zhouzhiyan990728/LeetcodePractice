from typing import List


class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        left = 0;
        right = len(nums) - 1;
        nums.sort();
        result = -1;

        while left < right:
            sum = nums[left] + nums[right];
            if sum < k:
                result = max(sum, result);
                left += 1;
            else:
                right -= 1;

        return result;
