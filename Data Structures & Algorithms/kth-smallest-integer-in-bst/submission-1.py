# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        vals = []

        def dfs (root: Optional[TreeNode]):
            nonlocal vals
            if not root:
                return;
            if not root.left and not root.right:
                vals.append(root.val)
                return;
            
            dfs(root.left)
            vals.append(root.val)
            dfs(root.right);
            return;

        dfs(root)
        return vals[k - 1];
            
        