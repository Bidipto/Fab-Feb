from collections import deque
import math
target = 15
nums = [1,2,3,4,5]

def minSubArrayLen(target, nums):
    que = deque()
    s = 0
    l = 0
    res = math.inf
    for i in nums:
        que.append(i)
        l += 1
        s += i
        while s >= target and que:
            res = min(res, l)
            s -= que.popleft()
            l -= 1
            
    return res if res != math.inf else 0

print(minSubArrayLen(target, nums))