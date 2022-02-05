prices = [1,4,5,2,9,7]
k = 2
def maxProfit(self, K, N, prices):
    dp = [[[-1 for i in range(K)] for _ in range(2)] for j in range(len(prices) - 1)]
    def magic(num, buy, k, dp):
        if k == K:
            return 0
        if num == len(prices) - 1:
            if buy:
                return 0
            if not buy:
                return prices[-1]

        if dp[num][buy][k] != -1:
            return dp[num][buy][k]

        if buy:
            take = magic(num + 1, not buy, k, dp) - prices[num]
            # print(num, take, buy)    
        else:
            take = magic(num + 1, not buy, k + 1, dp) + prices[num]
            # print(num, take, buy)

        nottake = magic(num + 1, buy, k, dp)
        # print(num, take, nottake)

        dp[num][buy][k] = max(take, nottake)
        # print(num, buy, dp, take, nottake, k)

        return dp[num][buy][k]

    return magic(0, True, 0, dp)

print(maxProfit(prices, k))

