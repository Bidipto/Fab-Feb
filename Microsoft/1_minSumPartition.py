arr = [1, 6, 11, 5]
n = len(arr)
#IMPORTANT CONCEPT:
def minDifference(arr, n):
    s = sum(arr)
    half = s // 2
    dp = [[False for i in range(half + 1)] for j in range(n + 1)]
    for i in range(len(dp)):
        dp[i][0] = True

    for i in range(1, len(dp)):
        for j in range(1, len(dp[0])):
            val = arr[i - 1]
            if j < val:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i-1][j] or dp[i - 1][j - arr[i-1]]
    
    for j in range(len(dp[0]) - 1, -1, -1):
        if dp[n][j]:
            return s - 2 * j

print(minDifference(arr, n))