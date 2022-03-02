#topological sort
def findOrder(self, numCourses: int, prereq: List[List[int]]) -> List[int]:
    adj = { i:set() for i in range(numCourses)}
        
    for course,pre in prereq:
        adj[course].add(pre)
    
    res = []
    visited = set()
    cycle = set()
    
    def magic(node):
        if node in visited:
            return True
        
        if node in cycle:
            return False
        
        cycle.add(node)
        
        for i in adj[node]:
            if not magic(i):
                return False
            
        cycle.remove(node)
        visited.add(node)
        res.append(node)
        return True
    
    for j in adj:
        if not magic(j):
            return []
        
    return res