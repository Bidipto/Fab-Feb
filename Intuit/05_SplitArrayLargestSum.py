#binary search on the range of possible answers
def splitArray(self, nums: List[int], m: int) -> int:
    hi = sum(nums)
    lo = max(nums)

    def check(summ):
        temp = 0
        res = 1
        for i in nums:
            temp += i
            if temp > summ:
                temp = i
                res += 1
        return res

    while lo < hi:
        mid = lo + ((hi - lo) // 2)
        num = check(mid)
        # print(lo,hi,mid,num)
        if num<=m:
            hi = mid
        else:
            lo = mid + 1
            
    return hi