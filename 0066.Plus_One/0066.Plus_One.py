from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        index = len(digits) - 1;
        if digits[index] != 9:
            digits[index] += 1;
            return digits;

        digits[index] += 1;
        while digits[index] == 10 and index > 0:
            digits[index] = 0;
            index -= 1;
            digits[index] += 1;

        if digits[index] == 10 and index == 0:
            digits[index] = 0;
            digits.insert(0, 1);

        return digits;