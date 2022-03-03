def NumberOfPaths(self, M, N):
    dp = [[-1 for i in range(N)] for j in range(M)]
    for m in range(M):
        for n in range(N):
            if m == 0 and n == 0:
                dp[m][n] = 1
            elif m == 0:
                dp[m][n] = dp[m][n-1]
            elif n == 0:
                dp[m][n] = dp[m-1][n]
            else:
                dp[m][n] = dp[m-1][n] + dp[m][n-1]
    return dp[-1][-1]