class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
      #define required Data Structure
        g = defaultdict(list)
        courses = prerequisites

      #build adjacency list
        for a, b in courses:
            g[a].append(b)
        
        #now define states:
        unvisited = 0
        visiting = 1
        visited = 2
        states = [unvisited] * numCourses

        #define dfs
        def dfs(node):
            state = states[node]
            if state == visited :
                return True
            elif state == visiting :
                return False

            states[node] = visiting
            
            for pre in g[node]:
                if not dfs(pre):
                    return False
            states[node] = visited
            return True
            
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True




       

        