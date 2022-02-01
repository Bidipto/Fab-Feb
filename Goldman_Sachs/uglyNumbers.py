class Solution:
	def getNthUglyNo(self,n):
        dp = [0,0,0]
        lst = [1]
        for i in range(n-1):
            res = min((lst[dp[0]])*2 ,lst[dp[1]]* 3 ,lst[dp[2]]*5)
            
            if res == lst[dp[0]]* 2:
                dp[0] += 1
            if res == lst[dp[1]]* 3:
                dp[1] += 1
            if res == lst[dp[2]]* 5:
                dp[2] += 1
            lst.append(res)
        return lst[-1]

#  Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        ob = Solution()
        ans = ob.getNthUglyNo(n);
        print(ans)
        tc -= 1

# } Driver Code Ends