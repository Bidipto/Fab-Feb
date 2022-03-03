def height(self, N):
    res = 0
    if N == 1:
        return 1
    for i in range(1,N):
        N -= i
        if N>=0:
            res += 1
        else:
            return res
    return res      
