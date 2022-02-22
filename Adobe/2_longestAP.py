A = [2, 4, 6, 8, 10]
n = len(A)
def lengthOfLongestAP(self, A, n):
    dp = {}
    if n == 1:
        return 1
    for i in range(1,len(nums)):
        #second loop for checking all the elements before it
        for j in range(i):
            diff = nums[i] - nums[j]
            if (j, diff) in dp:
                dp[i, diff] = dp[j, diff] + 1
            else:
                dp[i, diff] = 2
            #print(dp)
    return max(dp.values())

