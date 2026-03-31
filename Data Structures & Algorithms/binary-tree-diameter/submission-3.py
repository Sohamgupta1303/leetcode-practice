# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def dfs(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            if (not root.left and not root.right):
                return 1
            
            left_depth = dfs(root.left)
            right_depth = dfs(root.right)
            nonlocal diameter
            diameter = max(left_depth + right_depth, diameter)
            return max(left_depth, right_depth) + 1
            

        dfs(root)   
        return diameter


