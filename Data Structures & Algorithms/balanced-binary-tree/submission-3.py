# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs (root: Optional[TreeNode]) -> int:
            if not root: 
                return 0
            if not root.left and not root.right:
                return 1
            
            right_dfs = dfs(root.right)
            left_dfs = dfs(root.left)
            if (right_dfs == -1 or left_dfs == -1):
                return -1

            dfs_diff = max(right_dfs, left_dfs) - min(right_dfs, left_dfs)
            if dfs_diff == 0 or dfs_diff == 1:
                return max(right_dfs, left_dfs) + 1
            else:
                return -1
        
        return dfs(root) > -1

            