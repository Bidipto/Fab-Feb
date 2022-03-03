#look for gold pot solution for optimal solution here is the best case senerio for the first player
def stoneGame(self, nums1: List[int]) -> bool:
        #best case senerio
        nums2 = nums1[::-1] 
        M = len(nums1)
        dp = [[-1 for i in range(M)] for j in range(M)]
        
        def magic(m, n, dp):
            moves = m + n 
            
            if moves == M-1:
                return nums2[m]
            elif moves >= M:
                return 0
            
            # print(moves,M)
            if dp[m][n] != -1:
                return dp[m][n]
            
            dp[m][n] = max(nums1[n] + max(magic(m, n+2, dp),magic(m+1, n+1, dp)) ,nums2[m] + max(magic(m + 2, n, dp),magic(m+1, n+1, dp)))
            # print(dp, m, n)
            return dp[m][n]
            
        alice = magic(0, 0, dp)
        print(alice)
        if sum(nums1)-alice<alice:
            return True
        else:
            return False