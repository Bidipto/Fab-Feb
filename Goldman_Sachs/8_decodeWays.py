#recursive approach 
class Solution:
    def numDecodings(self, s: str) -> int:
        s = [int(i) for i in s]
        dp = [-1] * len(s)
        #print(dp)
        
        if s[-1] != 0:
            dp[-1] = 1
        else:
            dp[-1] = 0
        #print(dp)
        
        def magic(num, dp):
            if num == len(s):
                return 1
            if dp[num] != -1:
                return dp[num]
            
            double = 0
            single = 0
            
            if s[num] != 0:
                single = magic(num + 1, dp)
                
            if s[num] == 1 or s[num ] == 2 and num != len(s) - 1:
                no = (s[num] * 10)  + s[num+1]
                if no <= 26:
                    double = magic(num + 2, dp)
            
            dp[num] = single + double
            #print(num, single, double, dp)
            return dp[num]
            
        return magic(0, dp)
#tabulation bottom-up
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0]*(len(s)+1)
        dp[0] = 1
        if s[0] == '0':
            return 0
        else:
            dp[1] = 1
        
        for i in range(2,len(s)+1):
            # print(dp, i, s[i-2:i], s[i-1])
            if int(s[i-2:i]) >= 10 and int(s[i-2:i])<= 26:
                dp[i] += dp[i-2]
            if s[i-1] != '0':
                dp[i] += dp[i-1]
                
        return dp[-1]

#tabulation with memory optimization
class Solution:
    def numDecodings(self, s: str) -> int:
        prev = 1
        if s[0] == '0':
            return 0
        else:
            now = 1
        for i in range(2,len(s)+1):
            temp = 0
            #list slicing takes more time 
            if s[i-2] == '1' or (s[i-2]=='2' and s[i-1]<'7'):
                temp = temp + prev
            if s[i-1] != '0':
                temp = temp + now
            prev = now
            now = temp
        return now