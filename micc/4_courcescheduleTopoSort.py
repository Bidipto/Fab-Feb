def findOrder(self, numCourses: int, prereq: List[List[int]]) -> List[int]:
        adj = {i:set() for i in range(numCourses)}
        
        for course, pre in prereq:
            adj[course].add(pre)
        # print(adj)    
        
        visited = set()
        cycle = set()
        res = []
        
        def topo(root):
            if root in cycle:
                return False
            if root in visited:
                return True
            
            
            cycle.add(root)
            for i in adj[root]:
                if not topo(i):
                    return False
                
            cycle.remove(root)
            visited.add(root)
            res.append(root)
            return True
        
        for i in adj:
            a = topo(i)
            print(a)
            if not a:
                return []
        
        return res