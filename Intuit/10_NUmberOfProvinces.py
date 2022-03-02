adj = [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
def findCircleNum( adj):
    seen = set()
    def magic(node):
        for i, val in enumerate(adj[node]):
            if i not in seen and val:
                seen.add(i)
                magic(i)
    
    ans = 0
    for i in range(len(adj)):
        if i not in seen:
            magic(i)
            print(seen)
            ans += 1
            
    return ans

print(findCircleNum(adj))