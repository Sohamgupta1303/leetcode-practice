# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    
        def helper(main: Optional[TreeNode], sub: Optional[TreeNode]) -> bool:
            if not main and sub:
                return False
            if main and not sub:
                return False
            if not main and not sub:
                return True
            if main.val == sub.val:
                if helper(main.right, sub.right) and helper(main.left, sub.left):
                    return True
            
            return False

        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            if node.right: q.append(node.right) 
            if node.left: q.append(node.left)
            if node.val == subRoot.val and helper(node, subRoot):
                return True
        
        return False
        
        

        
        
            
            

        
        