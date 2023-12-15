from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix);
        n = len(matrix[0]);
        result = [[0] * m for i in range(n)];

        for i in range(n):
            for j in range(m):
                result[i][j] = matrix[j][i];

        return result;
