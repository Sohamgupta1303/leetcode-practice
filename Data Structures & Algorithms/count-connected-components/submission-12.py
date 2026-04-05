class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i : [] for i in range(n)}
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        
        visited = set()
        # so this function takes in a root and should add everything in its lineage to 
        # the visited set. 
        def dfs(root: int):
            if root in visited:
                return
            visited.add(root)
            for nei in adj[root]:
                dfs(nei)
            
            return
        
        count = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1
        
        return count
        
            



            