from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort(reverse = True);
        max = nums[0];
        count = 1;

        for i in nums:
            if i != max:
                max = i;
                count += 1;
            if count == 3:
                break;

        if count<3:
            return nums[0];

        return max;