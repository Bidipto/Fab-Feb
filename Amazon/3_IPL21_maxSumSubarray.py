arr = [8, 5, 10, 7, 9, 4, 3, 15, 12, 90, 13]
n = len(arr)
k = 4
#monotonic stack approach where we are storing [element, index]
#and if index is less than i - k, we are removing the element, ie out of the range
from collections import deque
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

print(max_of_subarrays(arr,n,k))    
