#dfs on all 1s
grid = [[int(i) for i in input().split()] for j in range(5)]
# 0 0 1 0 0 0 1 1 0 0
# 0 0 0 0 1 0 1 0 0 0
# 1 1 0 1 0 0 1 0 0 0
# 1 0 1 0 0 0 0 1 0 0
# 1 1 0 0 0 0 0 0 0 1


def findMaxArea(grid):
    M = len(grid)
    N = len(grid[0])
    res = 0
    i = []
    def magic(m,n):
        if m < M and n < N and grid [m][n] == 1:
            grid[m][n] = 0
            #top
            val = 1
            if m != 0:
                val += magic(m-1, n)
            #down
            if m != M:
                val += magic(m+1, n)
            #right
            if n != N:
                val += magic(m, n+1)
            #left
            if n != 0:
                val += magic(m, n-1)
            #top left
            if m != 0 and n != 0:
                val += magic(m-1, n-1)
            #top right
            if m != 0 and n != N:
                val += magic(m-1, n+1)
            #down left
            if m != M and n != 0:
                val += magic(m+1, n-1)
            #down right
            if m != M and n != N:
                val += magic(m+1, n+1)
            return val
        else:
            return 0
    for i in range(M):
        for j in range(N):
            if grid[i][j] == 1:
                res = max(res, magic(i,j))
                print(grid, i, j, res)
    return res
    
print(findMaxArea(grid))
