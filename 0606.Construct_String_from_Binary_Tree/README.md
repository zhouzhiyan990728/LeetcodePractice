# 606.Construct String from Binary Tree

## Question
Given the root of a binary tree, construct a string consisting of parenthesis and integers from a binary tree with the preorder traversal way, and return it.

Omit all the empty parenthesis pairs that do not affect the one-to-one mapping relationship between the string and the original binary tree.

### Example
```
Input: root = [1,2,3,4]
Output: "1(2(4))(3)"
Explanation: Originally, it needs to be "1(2(4)())(3()())", but you need to omit all the unnecessary empty parenthesis pairs. And it will be "1(2(4))(3)"
```

## Solution
* The preorder traversal is to visit the root firstly ,then the left node and then the right node.
* Note that even if the left node is None, there is still a "()".

## Code
```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ""
        return self.dfs(root)

    def dfs(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ""
        result = str(root.val)

        left = self.dfs(root.left)
        right = self.dfs(root.right)

        if left or right:
            result += f"({left})"
        if right:
            result += f"({right})"

        return result
```