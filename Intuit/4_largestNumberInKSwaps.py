class Solution:
    
    #Function to find the largest number after k swaps.
    def findMaximumNum(self,s,k):
        self.maxx = s
        def swap (i, j, s):
            now = [i for i in s]
            now[i], now[j] = now[j], now[i]
            return "".join(now)
        def magic(s, i, k):
            if s>self.maxx:
                self.maxx = s
            
            if i >= len(s) - 1:
                return
            
            if k == 0:
                return
            
            m = max(s[i+1:])
            if s[i] >= m:
                magic(s, i + 1, k)
            else:  
                for j in range(i + 1, len(s)):
                    if s[j] == m:
                        s = swap(i, j, s)
                        magic(s, i + 1, k-1)
                        s = swap(j, i, s)
                        
        magic(s, 0, k)
        return self.maxx

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(1):
        k = 4
        s = "1234567"
        ob=Solution()
        print(ob.findMaximumNum(s,k))