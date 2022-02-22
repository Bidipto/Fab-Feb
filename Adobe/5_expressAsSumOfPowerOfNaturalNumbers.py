target = 5
x = 2

def numOfWays(target, x):
    mod = 1000000007
    maxx = int(pow(target, 1/x))
    dp = [[-1 for i in range(target)] for j in range(maxx+1)] 
    def magic(m, currsum):
        if m>maxx:
            return 0
            
        if dp[m][currsum] != -1:
            return dp[m][currsum]
            
        res = 0
        p = pow(m, x)
        while p + currsum < target and m<maxx:
            res += (magic(m + 1, currsum + p)%mod)
            m += 1
            p = pow(m, x)
        
        if p + currsum == target:
            res += 1
        
        dp[m][currsum] = res%mod
        
        return dp[m][currsum]
        
    return magic(1, 0)

print(numOfWays(target, x))