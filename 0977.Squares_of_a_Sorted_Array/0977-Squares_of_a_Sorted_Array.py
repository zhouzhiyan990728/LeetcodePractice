class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        index = 0;
        for i in nums:
            nums[index] = i*i;
            index += 1;
        new_nums = sorted(nums);
        return new_nums;