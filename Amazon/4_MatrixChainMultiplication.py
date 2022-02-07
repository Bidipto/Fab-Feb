import math
arr = [3, 3, 3]
N = len(arr)
dp = [[math.inf for i in range(N)] for j in range(N)]

def magic(i, j, dp):
    if i == j:
        return 0
    
    if dp[i][j] != math.inf:
        return dp[i][j]
    # the magic happens here
    # we are tring to partition into and then find the the partion in which we have the 
    # least number of multiplications
    # for the inpput array [1, 2, 3, 4, 5] we partition it into
    # [1, 2] and [2, 3, 4, 5],[1, 2, 3] and [3, 4, 5],[1, 2, 3, 4] and [4, 5] 
    for k in range(i, j):
        #k denotes the the common element or range
        dp[i][j] = min(dp[i][j], magic(i, k, dp) + magic(k + 1, j, dp) + arr[i-1]*arr[k]*arr[j])
    print(dp)
    return dp[i][j]

print(magic(1, N-1, dp))
name = 65
name += 1
print(chr(name))