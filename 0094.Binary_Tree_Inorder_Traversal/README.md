# 94.Binary Tree Inorder Traversal

## Question
Given the root of a binary tree, return the inorder traversal of its nodes' values.

### Example
```
Input: root = [1,null,2,3]
Output: [1,3,2]
```

## Solution
* The inorder traversal is to visit the left node firstly ,then the e and then the right node.

## Code
```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.inorder(root, result)
        return result

    def inorder(self,root: Optional[TreeNode],result:List[int]):
        if root is not None:
            self.inorder(root.left,result);
            result.append(root.val);
            self.inorder(root.right,result);
```