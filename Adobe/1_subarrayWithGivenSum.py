
A = [1,2,3,7,5]
n = len(A)
s = 12
def subArraySum(arr, n, s):
    summ = 0
    begin = 0
    for i in range(n):
        summ += arr[i]
        if summ == s:
            return [begin + 1, i + 1]
        elif summ > s:
            while summ > s:
                summ -= arr[begin]
                begin += 1
            if summ == s:
                return [begin + 1, i + 1]
        
print(subArraySum(A, n, s))