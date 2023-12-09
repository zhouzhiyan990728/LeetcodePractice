class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum_left, sum_right = [None] * len(nums), [None] * len(nums);
        sum_num = 0;
        for i in range(len(nums)):
            sum_left[i] = sum_num;
            sum_num += nums[i];

        sum_num = 0;
        for i in range(len(nums) - 1, -1, -1):
            sum_right[i] = sum_num;
            sum_num += nums[i];

        for i in range(len(nums)):
            if sum_left[i] == sum_right[i]:
                return i;

        return -1;