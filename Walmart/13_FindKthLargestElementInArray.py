def kthLargestNumber(self, nums: List[str], k: int) -> str:
    arr = [-int(i) for i in nums]
    heapq.heapify(arr)
    for i in range(k):
        res = heapq.heappop(arr)
    return str(-1*res)
        