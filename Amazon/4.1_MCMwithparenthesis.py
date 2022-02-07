import math
arr = [3, 3, 3]
N = len(arr)
dp = [[math.inf for i in range(N)] for j in range(N)]
bracket = [[0 for i in range(N)] for j in range(N)]
name = [65]
res = []
def br(i, j, bracket, name, res):
    if i == j:
        res.append(chr(name[0]))
        name[0] += 1
        return
    res.append("(")
    br(i, bracket[i][j], bracket, name, res)
    br(bracket[i][j] + 1, j, bracket, name, res)
    res.append(")")

def magic(i, j, dp, bracket):
    if i == j:
        return 0
    
    if dp[i][j] != math.inf:
        return dp[i][j]
    # the magic happens here
    for k in range(i, j):
        temp =  magic(i, k, dp, bracket) + magic(k + 1, j, dp, bracket) + arr[i-1]*arr[k]*arr[j]
        if dp[i][j] > temp:
            dp[i][j] = temp
            bracket[i][j] = k
    return dp[i][j]

print(magic(1, N-1, dp, bracket))
print(bracket)
br(1, N-1, bracket, name, res)
print("".join(res))

