N = 1
K = 0
def kvowelwords( N, K):
    mod = 1000000007
    dp = [[0 for i in range(K+1)] for j in range(N+1)]
    summ = 1
    #dp[i][j] 
    #i represents the length of the arr
    #j represents the length of the continous vowel length 
    for i in range(1,N + 1):
        #since j is zero ie all the values will have just a consonect at the end
        #ie total number of combinations upto now * 21 
        dp[i][0] = (summ * 21) % mod
        for j in range(1, K +1):
            if i == j:
                #when length of string is equal to number of vowels
                dp[i][j] = pow(5, i, mod)
            elif j > i:
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i][j-1] * 21
            
            summ += dp[i][j]
            summ %= mod
    print(dp)
    return summ
print(kvowelwords( N, K))