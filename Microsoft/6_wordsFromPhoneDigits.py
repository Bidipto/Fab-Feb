
def possibleWords(arr):
    words = {
        2: 'abc',
        3: 'def',
        4: 'ghi',
        5: 'jkl',
        6: 'mno',
        7: 'pqrs',
        8: 'tuv',
        9 : 'wxyz'
    }
    res = []
    def magic(m, curr):
        if m == len(arr):
            res.append(curr)
            return
        for i in words[arr[m]]:
            magic(m+1, curr+i)
    magic(0, '')
    return res

print(possibleWords([5,8,8,9,8]))