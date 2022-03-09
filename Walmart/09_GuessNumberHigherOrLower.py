def getMoneyAmount(self, n: int) -> int:
    dp = {}
    
    def magic(s, e):
        if (s, e) in dp:
            return dp[(s,e)]
        
        if s>=e:
            return 0
        
        res = math.inf
        
        for i in range(s,e):
            temp = max(magic(s,i-1), magic(i+1,e))
            res = min(temp + i, res)
            
        dp[(s, e)] = res
        return res
    
    return magic(0,n)
    