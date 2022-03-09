#priority queue implementation
def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
    arr = []
    
    for eff, sp in zip(efficiency, speed):
        arr.append([eff, sp])
    
    arr.sort(reverse = True)
        
    heap = []
    summ = 0
    res = 0
    
    for i in range(n):
        heapq.heappush(heap, arr[i][1])
        summ += arr[i][1]
        if len(heap)>k:
            summ -= heapq.heappop(heap)
        res = max(res, (summ * arr[i][0]))
        
    return res%(pow(10,9)+7)