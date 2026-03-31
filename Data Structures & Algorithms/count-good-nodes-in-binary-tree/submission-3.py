# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_nodes = []
        family_nodes = []

        def dfs(root: TreeNode, path_nodes: List[int]):
            nonlocal good_nodes
            if not root:
                return;
            
            # check if its good
            is_max = True
            for i in path_nodes:
                if i.val > root.val :
                    is_max = False
            if (is_max):
                good_nodes.append(root.val)
            
            # make new_path_nodes
            new_path_nodes = []
            for i in path_nodes:
                new_path_nodes.append(i)
            new_path_nodes.append(root)

            # recurse other nodes
            dfs(root.left, new_path_nodes)
            dfs(root.right, new_path_nodes)
            return;
        
        dfs(root, family_nodes)
        print(good_nodes)
        return len(good_nodes)

