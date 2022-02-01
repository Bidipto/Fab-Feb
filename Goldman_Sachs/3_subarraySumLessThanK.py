from collections import deque
from curses import window


class Solution:
    def countSubArrayProductLessThanK(self, arr, n, k):
        #we are calculating the product of the deque in s and the len of the deque in length
        window = deque()
        s = 1
        length = 0
        res = 0
        for i in arr:
            window.append(i)
            s *= i
            length += 1
            while s>=k:
                s //= window.popleft()
                length -= 1
            res += length
        return res

def main():

    T = int(input())

    while(T > 0):
        n, k = [int(x) for x in input().strip().split()]
        arr = [int(x) for x in input().strip().split()]
        
        print(Solution().countSubArrayProductLessThanK(arr, n, k))

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends