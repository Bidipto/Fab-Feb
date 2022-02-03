# heap maintains the highest 10 elements 

import heapq
arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
heap = []
for i in arr:
    heapq.heappush(heap, i)
    if len(heap)>10:
        heapq.heappop(heap)

for i in range(10):
    print(heapq.heappop(heap))