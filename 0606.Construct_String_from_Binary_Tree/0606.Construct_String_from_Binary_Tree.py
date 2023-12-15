# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from idlelib.tree import TreeNode
from typing import Optional


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
