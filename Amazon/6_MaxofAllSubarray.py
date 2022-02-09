#input
arr = [1, 2, 3, 1, 4, 5, 2, 3, 6]
K = 3
N = len(arr)

from collections import deque
#monotonnic queuwe implementation
def max_of_subarrays(arr,n,k):
    i = 0
    queue = deque()
    while i < k:
        while queue and queue[-1][0] <= arr[i]:
            queue.pop()
        queue.append([arr[i], i])
        i += 1
    res = [queue[0][0]]
    #making the first k elements🐱‍👤 
    while i < n:
        element = arr[i]
        while queue and queue[-1][0] <= element:
            queue.pop()
        queue.append([element, i])
        if queue[0][1] <= i-k:
            queue.popleft()
        res.append(queue[0][0])
        i += 1
    return res

print(max_of_subarrays(arr,N,K)) 
