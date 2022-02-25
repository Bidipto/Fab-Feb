import math
arr1 = [1, 35]
arr2 = [6, 9, 13, 15, 20, 25, 29, 46]
n = len(arr1)
m = len(arr2)
def merge(arr1,arr2,n,m):
        ceil = math.ceil((n+m)/2)
        temp = -1
        while True:
            print(ceil, arr1, arr2)
            if ceil == temp:
                break
            else:
                temp = ceil
            
            for i in range(ceil, m + n ):
                first = i - ceil 
                second = i
                print(first, second)
                if first<n and second<n:
                    if arr1[first]>arr1[second]:
                        arr1[first],arr1[second] = arr1[second], arr1[first]
                elif second >= n and first<n:
                    second -= n
                    if arr1[first]>arr2[second]:
                        arr1[first],arr2[second] = arr2[second], arr1[first]
                else:
                    first -= n
                    second -= n
                    if arr2[first]>arr2[second]:
                        arr2[first],arr2[second] = arr2[second], arr2[first]
            #updated ceil
            ceil = math.ceil(ceil/2)
merge(arr1, arr2, n, m)
print(arr1, arr2)