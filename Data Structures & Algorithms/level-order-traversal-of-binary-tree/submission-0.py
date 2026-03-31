# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        result_values = []
        if len(result) == 0:
            result.append([root])
            result_values.append([root.val])
        
        for res in result:
            level = []
            level_vals = []
            for node in res:
                if node.left:
                    level.append(node.left)
                    level_vals.append(node.left.val)
                if node.right:
                    level.append(node.right)
                    level_vals.append(node.right.val)
            if (level):
                result.append(level)
                result_values.append(level_vals)

        
        return result_values



        