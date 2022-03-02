def findInMountainArray(self, target: int, mountain: 'MountainArray') -> int:
        #seach for the peak in mountain array
        M = mountain.length()
        lo = 0
        hi = M -1
        while lo<hi:
            mid = lo + ((hi - lo)//2)
            if mountain.get(mid)<mountain.get(mid + 1):
                lo = mid + 1
                peak = mid + 1
            else:
                hi = mid
        # print(peak)
        #for first element in increasing
        lo = 0
        hi = peak
        while lo<=hi:
            mid = lo + ((hi - lo)//2)
            element = mountain.get(mid)
            if mountain.get(mid) == target:
                return mid
            elif element > target:
                hi = mid - 1
            else:
                lo = mid + 1
        #if not found search in decreasing
        lo = peak
        hi = M -1
        while lo<=hi:
            mid = lo + ((hi - lo)//2)
            element = mountain.get(mid)
            # print(hi, lo, mid, element)
            if mountain.get(mid) == target:
                return mid
            elif element < target:
                hi = mid - 1
            else:
                lo = mid + 1
        return -1