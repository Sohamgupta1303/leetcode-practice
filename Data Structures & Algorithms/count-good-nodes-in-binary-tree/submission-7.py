class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_nodes = []

        def dfs(node: TreeNode, max_so_far: int):
            if not node:
                return

            if node.val >= max_so_far:   # check “goodness”
                good_nodes.append(node.val)

            new_max = max(max_so_far, node.val)
            dfs(node.left, new_max)
            dfs(node.right, new_max)

        dfs(root, root.val)
        return len(good_nodes)