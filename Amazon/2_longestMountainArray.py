arr = [2,2,2]
#O(n) time and O(n) space
j = 0
while j < len(arr):
    if arr[j] < arr[j-1]:
        break
    else:
        j += 1
if j == len(arr):
    print(0)
stack = [arr[j]]
temp = arr[j]
flag = True
res = 0
size = 1

for i in range(j, len(arr)):
    #when the current element is greater than the previous element
    # and the elements are increasing
    if arr[i] > temp:
        if flag == True:
            stack.append(arr[i])
            temp = arr[i]
            size += 1
        # we have found a valley
        else:
            res = max(res, size)
            stack = [temp]
            size = 1
            flag = True

            temp = arr[i]
            size += 1
            stack.append(arr[i])
               
    #when the current element is less than the previous element
    # and the elements are increasing, then we have found a peak
    elif arr[i] < temp:
        if flag == True:
            stack.append(arr[i])
            flag = False
            size += 1
            temp = arr[i]
        else:
            stack.append(arr[i])
            size += 1
            temp = arr[i]
print(res)

#O(n) time and O(1) space
def longestMountain(self, arr: List[int]) -> int:
    i = 0
    while i < len(arr)-1:
        if arr[i] < arr[i+1]:
            break
        else:
            i += 1
    if i == len(arr)-1:
        return 0
    temp = arr[i]
    flag = True
    res = 0
    size = 1

    while i<len(arr):
        #when the current element is greater than the previous element
        # and the elements are increasing
        if arr[i] > temp:
            if not flag:
            # we have found a valley
                res = max(res, size)
                size = 1
                flag = True
            temp = arr[i]
            size += 1
        #when the current element is less than the previous element
        # and the elements are increasing, then we have found a peak
        elif arr[i] < temp:
            if flag:
                flag = False
            size += 1
            temp = arr[i]
            res = max(res, size)
        else:
            while i < len(arr)-1:
                if arr[i] < arr[i+1]:
                    break
                else:
                    i += 1
            
            temp = arr[i]
            size = 1
            flag = True

        i += 1
    return res
    