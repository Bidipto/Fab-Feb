def minSwaps(self, grid: List[List[int]]) -> int:
    right=[]
    N = len(grid)
    
    for i in range(N):
        temp = 0
        for j in range(N - 1, -1, -1):
            if grid[i][j]:
                right.append(temp)
                break
            else:
                temp += 1
    
    sortedright = sorted(right)
    # print(right, sortedright)
    for i, val in enumerate(sortedright):
        # print(i,val)
        if i > val:
            return -1
    
    res = 0
    
    #agar darkar se zada zeros hai we do nothing cause agge jake need for 0s will decrease
    #and since we already check if its possible therefore there exists a solution for future needs
    #also jo ans can fulfill current need can fulfill future needs too cause decreasin
    for i in range(len(right)):
        if right[i]>=N-i-1:
            continue
        
        for j in range(i + 1, len(right)):
            if right[j]>=N-i-1:
                # print(i,j,right)
                res += j - i
                k = right[j]
                right[i+1:j+1] = right[i:j]
                right[i] = k
                # print(right)
                break
    # print(right)
    return res