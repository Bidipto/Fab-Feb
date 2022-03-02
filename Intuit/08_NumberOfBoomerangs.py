#n2 solution where we use a dictionary to store the number of times a distace is repeated for every poin
def numberOfBoomerangs(self, points: List[List[int]]) -> int:
    res = 0
    for i in points:
        dic = {}
        for j in points:
            x = i[0] - j[0]
            y = i[1] - j[1]
            dic[pow(x,2) + pow(y,2)] = dic.get(pow(x,2) + pow(y,2), 0) + 1
        for i in dic:
            res += dic[i] * (dic[i] - 1)
    return res