def minEatingSpeed(self, piles: List[int], h: int) -> int:
    def check(mid):
        res = 0
        for i in piles:
            res += (i//mid) + (i%mid != 0)
            
        if res<=h:
            return True
        else:
            return False
        
    lo = 1
    hi = max(piles)

    while lo<hi:
        mid = lo + ((hi-lo)//2)
        flag = check(mid)
        # print(hi,lo,mid,flag)
        if flag:
            hi = mid
        else:
            lo = mid + 1
        # print(hi,lo)

    return hi