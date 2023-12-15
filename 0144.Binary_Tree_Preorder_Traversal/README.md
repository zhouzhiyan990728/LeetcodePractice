# 144.Binary Tree Preorder Traversal

## Question
Given the root of a binary tree, return the preorder traversal of its nodes' values.

### Example
```
Input: root = [1,null,2,3]
Output: [1,2,3]
```

## Solution
* The preorder traversal is to visit the root firstly ,then the left node and then the right node.

## Code
```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.preorder(root, result)
        return result
    
    def preorder(self,root: Optional[TreeNode],result:List[int]):
        if root is not None:
            result.append(root.val);
            self.preorder(root.left,result);
            self.preorder(root.right,result);
```