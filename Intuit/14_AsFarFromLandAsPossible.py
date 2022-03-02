#simple bfs, dfs wont work cause the search algo will get complex
#life it we reach the end the land might exist piche
def maxDistance(self, grid: List[List[int]]) -> int:
    N = len(grid)
    land = deque([(m,n) for m in range(N) for n in range(N) if grid[m][n] == 1])
    
    if not land:
        return -1
    
    if len(land) == pow(N,2):
        return -1
    
    res = -1
    while land:
        for q in range(len(land)):
            m,n = land.popleft()
            for x,y in [[1,0], [0,1], [-1,0], [0,-1]]:
                mi = m + x
                ni = n + y
                if 0<= mi< N and 0<= ni < N and grid[mi][ni] == 0:
                    land.append((mi,ni))
                    grid[mi][ni] = 1
                    
        res += 1
        
    return res