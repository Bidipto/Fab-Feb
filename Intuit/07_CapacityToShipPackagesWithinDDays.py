def shipWithinDays(self, weights: List[int], days: int) -> int:
    def count(mid):
        day = 1
        temp = 0
        for i in weights:
            temp += i
            if temp > mid:
                temp = i
                day += 1
        return day
    lo = max(weights)
    hi = sum(weights) + 1
    res = -1
    while hi>lo:
        mid = lo + ((hi-lo)//2)
        day = count(mid)
        if  day <= days:
            res = mid
            hi = mid
        else:
            lo = mid + 1
    
    return res