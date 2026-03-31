class Solution:
    
    def dfs(self, current_node, visited, stack, adj_list):
        visited[current_node] = 1
        
        for adj_node in adj_list[current_node]:
            if visited[adj_node] == 0:
                self.dfs(adj_node,visited, stack, adj_list)
                
        stack.append(current_node)
    
    
    
    def topoSort(self, V, edges):
        # Code here
        adj_list = [[] for _ in range (V)]
        for u,v in edges:
            adj_list[u].append(v)
        
        stack = []
        visited = [0 for _ in range (V)]
        for i in range (V):
            if visited[i] == 0:
                self.dfs(i, visited, stack, adj_list)
        
        return stack[::-1]
        
        