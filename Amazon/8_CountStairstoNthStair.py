m = 4
#similar to coin change 2
def countWays(m):
        
        mod = 1000000007
        # code here
        dp = [0]*(m+1)
        dp[0] = 1
        for i in range(1,3):
            for j in range(1,m + 1):
                if j - i >= 0:
                    dp[j] += dp[j-i]%mod
        return dp[-1]%mod

print(countWays(m))