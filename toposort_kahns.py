from collections import deque
class Solution:
    
    def topoSort(self, V, edges):
        # Code here
        adj_list = [[] for _ in range (V)]
        in_degress= [0 for _ in range(V)]
        for u,v in edges:
            adj_list[u].append(v)
            in_degress[v] +=1
            
        queue = deque()
        result = []
        
        for i in range (V):
            if in_degress[i] == 0:
                queue.append(i)
        
        while len(queue) !=0:
            current_node = queue.popleft()
            result.append(current_node)
            for adj_node in adj_list[current_node]:
                in_degress[adj_node] -=1
                if in_degress[adj_node] == 0:
                    queue.append(adj_node)
        return result