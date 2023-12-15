# 867. Transpose Matrix

## Question
Given a 2D integer array matrix, return the transpose of matrix.

The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

### Example
```
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]
```

## Solution
* Create a m*n matrix to store the result.
* matrix[i][j] = result[j][i]

## Code
```python3
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix);
        n = len(matrix[0]);
        result = [[0]*m for i in range(n)];

        for i in range(n):
            for j in range(m):
                result[i][j] = matrix[j][i];
        
        return result;
```