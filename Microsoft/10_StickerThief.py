#house robber on leetcode

def FindMaxSum(self,a, n):
        curr = 0
        prev = 0
        for i in a:
            temp = max(prev + i,curr)
            prev = curr
            curr = temp
        return curr