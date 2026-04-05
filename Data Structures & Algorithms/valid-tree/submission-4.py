class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i : [] for i in range(n)}
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        
        visited = set()
        def dfs(root: int, parent: int) -> bool:
            if root in visited:
                return False
            visited.add(root)
            for nei in adj[root]:
                if nei == parent:
                    continue
                if not dfs(nei, root): return False
            
            return True
            
        
        if not dfs(0 , -1): return False
        
        return len(visited) == n and len(edges) == n - 1

        