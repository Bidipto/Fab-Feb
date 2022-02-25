#maintain a set with or without take ing a number
def equalPartition(self, N, arr):
        summ = sum(arr)
        if summ % 2:
            return False
        target = summ // 2
        dp = set()
        dp.add(0)
        
        for i in range(len(arr) -1, -1, -1):
            nextdp = set()
            for j in dp:
                if j + arr[i] == target:
                    return True
                nextdp.add(j + arr[i])
                nextdp.add(j)
            
            dp = nextdp
        return False if target not in dp else True