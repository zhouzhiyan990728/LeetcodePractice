from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        self.checkLastElement(nums, val);
        index = 0;
        for i in nums:
            if nums and i == val:
                nums[index] = nums[-1];
                nums.pop(-1);
                self.checkLastElement(nums, val);
            index += 1;
        return len(nums);

    def checkLastElement(self, nums: List[int], val: int):
        while nums and nums[-1] == val:
            nums.pop(-1);


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0;
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j];
                i += 1;
        return i;